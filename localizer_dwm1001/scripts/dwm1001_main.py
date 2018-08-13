#!/usr/bin/env python

import rospy
import serial
import time
import os
import sys
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist     
from dwm1001_serialPort import SERIAL_PORT_DETAILS
from dwm1001_apiCommands import DWM1001_API_COMMANDS
from dwm1001_anchors import DWM1001_ANCHORS
from dwm1001_network import DWM1001_NETWORK


from dynamic_reconfigure.server import Server
from localizer_dwm1001.cfg import DWM1001_Tune_SerialConfig

startButton = False

dynamicConfigOpenPort   = {"open_port" : False}
dynamicConfigClosePort  = {"close_port": False}
dynamicConfigSerialPort = {"serial_port": ""}

# initialize serial port connections
serialPortDWM1001 = serial.Serial(
    port     = SERIAL_PORT_DETAILS.name,
    baudrate = SERIAL_PORT_DETAILS.baudRate,
    parity   = SERIAL_PORT_DETAILS.parity,
    stopbits = SERIAL_PORT_DETAILS.stopbits,
    bytesize = SERIAL_PORT_DETAILS.bytesize
)


def main():
    global dynamicConfigOpenPort
    global dynamicConfigClosePort

    # initialize our topics
    pub_Network  = rospy.Publisher('DWM1001_Network',          String, queue_size=10)
    pub_Anchor_0 = rospy.Publisher('DWM1001_Network_Anchor_0', String, queue_size=10)
    pub_Anchor_1 = rospy.Publisher('DWM1001_Network_Anchor_1', String, queue_size=10)
    pub_Anchor_2 = rospy.Publisher('DWM1001_Network_Anchor_2', String, queue_size=10)
    pub_Tag      = rospy.Publisher('DWM1001_Network_Tag',      String, queue_size=10)

    # initialize the node
    rospy.init_node('Localizer_DWM1001', anonymous=False)

    # intialize dynamic configuration
    dynamicConfigServer = Server(DWM1001_Tune_SerialConfig, callbackDynamicConfig)
    dynamicConfigClosePort.update({"close_port": True })
    dynamicConfigOpenPort.update({"open_port" : False})
    dynamicConfigServer.update_configuration(dynamicConfigOpenPort)
    dynamicConfigServer.update_configuration(dynamicConfigClosePort)

    # initialize ros rate, this will be used for sleep
    rate = rospy.Rate(100)  # 10hz

    # close the serial port in case the previous run didn't closed it properly
    serialPortDWM1001.close()
    time.sleep(10)
    # open serial port
    serialPortDWM1001.open()


    # check if the serial port is opened
    if(serialPortDWM1001.isOpen()):

        dynamicConfigClosePort.update({"close_port": False})
        dynamicConfigOpenPort.update({"open_port": True})
        dynamicConfigSerialPort = {"serial_port": str(SERIAL_PORT_DETAILS.name)}
        dynamicConfigServer.update_configuration(dynamicConfigOpenPort)
        dynamicConfigServer.update_configuration(dynamicConfigClosePort)
        dynamicConfigServer.update_configuration(dynamicConfigSerialPort)

        rospy.loginfo("Port opened: "+ str(SERIAL_PORT_DETAILS.name) );
        serialPortDWM1001.write(DWM1001_API_COMMANDS.SingleEnter)
        time.sleep(0.5)
        serialPortDWM1001.write(DWM1001_API_COMMANDS.SingleEnter)

    # check if the serial port is not open
    else:
        rospy.loginfo("Can't open port: "+ str(SERIAL_PORT_DETAILS.name))

    # give some time to DWM1001 to wake up
    time.sleep(5)
    # send command lec, so we can get positions is CSV format
    serialPortDWM1001.write(DWM1001_API_COMMANDS.LecPlusEnter)
    rospy.loginfo("Reading DWM1001 coordinates")


    while True:
        serialReadLine = serialPortDWM1001.read_until()
        rospy.loginfo("Waiting for DWM1001 to wake up " + str(serialReadLine))
        rate.sleep()
        if "Command not found" in serialReadLine:
            rospy.loginfo("Command not found trying again")
            pub_Network.publish("Command not found trying again")
            serialPortDWM1001.write(DWM1001_API_COMMANDS.SingleEnter)
            serialPortDWM1001.write(DWM1001_API_COMMANDS.SingleEnter)
            time.sleep(1.5)
            serialPortDWM1001.write(DWM1001_API_COMMANDS.LecPlusEnter)
            time.sleep(2.5)
        elif "dwm>" in serialReadLine:
            rospy.loginfo("DWM1001 API is ready to receive commands")
            pub_Network.publish("DWM1001 API is ready to receive commands")
            #serialPortDWM1001.reset_input_buffer()
            serialPortDWM1001.write(DWM1001_API_COMMANDS.SingleEnter)
            time.sleep(0.2)
            break
        elif "" in serialReadLine :
            rospy.loginfo("DWM1001 is not responding, received nothing, trying again")
            serialPortDWM1001.reset_input_buffer()
            serialPortDWM1001.write(DWM1001_API_COMMANDS.LecPlusEnter)
            serialPortDWM1001.write(DWM1001_API_COMMANDS.SingleEnter)
            time.sleep(0.1)
            serialPortDWM1001.write(DWM1001_API_COMMANDS.SingleEnter)
        elif"dwm> lec" in serialReadLine:
            rospy.loginfo("DWM1001 is not responding, received dwm>lec but not position, trying again")
            pub_Network.publish("DWM1001 is not responding, received dwm>lec but not position, trying again")
            serialPortDWM1001.write(DWM1001_API_COMMANDS.SingleEnter)
            serialPortDWM1001.write(DWM1001_API_COMMANDS.SingleEnter)
            time.sleep(2.5)
            serialPortDWM1001.write(DWM1001_API_COMMANDS.LecPlusEnter)
            time.sleep(2.5)
        elif"DIST" in serialReadLine:
            break
        elif "License" in serialReadLine:
            break
        else:
            break



    try:

        while not rospy.is_shutdown():
            serialReadLine = serialPortDWM1001.read_until()
            serialPortDWM1001.reset_input_buffer()

            rate.sleep()

            arr = []

            # split serial port message by comma ','
            arr = [ x.strip() for x in serialReadLine.strip().split(',') ]



            try:
                DWM1001_NETWORK.anchors = arr[1]
                rospy.loginfo("Number(s) of Anchors: " + arr[1])
                rospy.loginfo("Length of array: " + str(len(arr)))

                ##########################################
                # Publish coordinates of tag and anchors #
                ##########################################
                pub_Network.publish( str("x:" + arr[4] + "y:" + arr[5] + " z: " + arr[6]))
                pub_Anchor_0.publish(str(arr[4] + " " + arr[5] + " " + arr[6]))
                pub_Anchor_1.publish(str(arr[10]+ " " + arr[11]+ " " + arr[12]))
                pub_Anchor_2.publish(str(arr[16]+ " " + arr[17]+ " " + arr[18]))
                pub_Tag.publish(str(arr[21]+ " " + arr[22]+ " " + arr[23]))
                # flush buffer of serial port
                #serialPortDWM1001.flush()

            except IndexError:
                DWM1001_NETWORK.anchors = ''

            rospy.loginfo(arr)


    except KeyboardInterrupt:
        rospy.loginfo("Quitting DWM1001 Shell Mode and closing port, allow 1 second for UWB recovery")

    finally:
        rospy.loginfo("Trying to quit, but is not easy!!!")
        serialPortDWM1001.reset_input_buffer()
        serialPortDWM1001.write(DWM1001_API_COMMANDS.Quit)
        serialPortDWM1001.write(DWM1001_API_COMMANDS.SingleEnter)
        rate.sleep()
        if "bye" in serialReadLine:
            rospy.loginfo("succesfully closed ")
            serialPortDWM1001.close()



# Receives joystick messages (subscribed to Joy topic)
def JoyCallback(data):
    global startButton

    #That's the select button
    if(data.buttons[11] == 1):
        startButton = True
    else:
        startButton = False

def callbackDynamicConfig(config, leve):
    global serialPortDWM1001
    rospy.loginfo("""Reconfigure Request: {dwm1001_network_info}, {open_port},\ 
          {serial_port}, {close_port}""".format(**config))

    if config["quit_dwm1001_api"]:
        rospy.loginfo("Trying to quit from dynamic config!!")
        serialPortDWM1001.write(DWM1001_API_COMMANDS.Quit)
        config["quit_dwm1001_api"] = False

    if config["close_port"]:
        rospy.loginfo("Closing port!!")
        serialPortDWM1001.close()
        config["close_port"] = False

    if config["exit"]:
        rospy.loginfo("System exit!!")
        config["exit"] = False
        sys.exit()


    return config

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

