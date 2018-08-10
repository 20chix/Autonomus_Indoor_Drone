#!/usr/bin/env python

import rospy
import serial
import time
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







def main():
    
    pub_Network  = rospy.Publisher('DWM1001_Network', String, queue_size=10)
    pub_Anchor_0 = rospy.Publisher('DWM1001_Network_Anchor_0', String, queue_size=10)
    pub_Anchor_1 = rospy.Publisher('DWM1001_Network_Anchor_1', String, queue_size=10)
    pub_Anchor_2 = rospy.Publisher('DWM1001_Network_Anchor_2', String, queue_size=10)
    pub_Tag = rospy.Publisher('DWM1001_Network_Tag', String, queue_size=10)

    
    rospy.init_node('Localizer_DWM1001', anonymous=False)
    Server(DWM1001_Tune_SerialConfig, tuneSerial)

    # serial port
    # configure the serial connections (the parameters differs on the device you are connecting to)
    serialPortDWM1001 = serial.Serial(
        port=SERIAL_PORT_DETAILS.name,
        baudrate=SERIAL_PORT_DETAILS.baudRate,
        parity=SERIAL_PORT_DETAILS.parity,
        stopbits=SERIAL_PORT_DETAILS.stopbits,
        bytesize=SERIAL_PORT_DETAILS.bytesize
    )

    rate = rospy.Rate(100)  # 10hz


    serialPortDWM1001.close()
    serialPortDWM1001.open()


    if(serialPortDWM1001.isOpen()):
        rospy.loginfo("Port opened: "+ str(SERIAL_PORT_DETAILS.name) );

        serialPortDWM1001.write(DWM1001_API_COMMANDS.SingleEnter)
        time.sleep(0.5)
        serialPortDWM1001.write(DWM1001_API_COMMANDS.SingleEnter)





        #Give time to the pi to read from serial  
        #time.sleep(3)
        #Assign read line to variable 
        #serialReadLine = serialPortDWM1001.readline()
        #rospy.loginfo(str(serialReadLine));

    else:
        rospy.loginfo("Can't open port: "+ str(SERIAL_PORT_DETAILS.name))

    time.sleep(5)
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

            #rospy.loginfo( str(startButton))
            #if "Distance :" in serialReadLine:
            #rospy.loginfo(serialReadLine)
            #map(lambda s:s.strip(), serialReadLine.split(','))
            #arr = [ x.strip() for x in serialReadLine.strip('[]').split(',') ]
            #rospy.loginfo(arr)
            #pub.publish(arr)

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
# then converts the joysick inputs into Twist commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed
def JoyCallback(data):
    global startButton
    #twist.linear.x = 4*data.axes[7]
    #twist.angular.z = 4*data.axes[6]
    #twist.buttons = data.buttons
    #startButton = data.buttons[11]


    #That's the select button
    if(data.buttons[11] == 1):
        startButton = True
    else:
        startButton = False

# Joy node
def subscribeToJoy():
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, JoyCallback)


def tuneSerial(config, leve):

    default_colors = config["Low_v"]

    rospy.loginfo("Dynamic config working!! " + str(default_colors))

    config["Low_v"] =20

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

