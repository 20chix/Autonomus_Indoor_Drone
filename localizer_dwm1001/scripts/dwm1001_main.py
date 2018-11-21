#!/usr/bin/env python
""" For more info on the documentation go to https://www.decawave.com/sites/default/files/dwm1001-api-guide.pdf
"""
#!/usr/bin/env python

__author__     = "Hadi Elmekawi"
__version__    = "1.0"
__maintainer__ = "Hadi Elmekawi"
__email__      = "w1530819@my.westminster.ac.uk"
__status__     = "Development"


import rospy, sys, time, serial
from std_msgs.msg               import String
from dwm1001_serialPort         import SERIAL_PORT_DETAILS
from dwm1001_apiCommands        import DWM1001_API_COMMANDS
from dwm1001_sys_defs           import SYS_DEFS
from dynamic_reconfigure.server import Server
from localizer_dwm1001.cfg      import DWM1001_Tune_SerialConfig

# initialize the node
rospy.init_node('Localizer_DWM1001', anonymous=False)

# TODO decide what to do with joystick button in the furture
startButton = False

dynamicConfig_OPEN_PORT   = {"open_port": False}
dynamicConfig_CLOSE_PORT  = {"close_port": False}
dynamicConfig_SERIAL_PORT = {"serial_port": ""}

# initialize ros rate 10hz
rate = rospy.Rate(200)

# initialize serial port connections
serialPortDWM1001 = serial.Serial(
    port     = SERIAL_PORT_DETAILS.name,
    baudrate = SERIAL_PORT_DETAILS.baudRate,
    parity   = SERIAL_PORT_DETAILS.parity,
    stopbits = SERIAL_PORT_DETAILS.stopbits,
    bytesize = SERIAL_PORT_DETAILS.bytesize
)

# initialize topics
pubblisher_Network  = rospy.Publisher('DWM1001_Network', String, queue_size=10)
pubblisher_Anchor_0 = rospy.Publisher('DWM1001_Network_Anchor_0', String, queue_size=10)
pubblisher_Anchor_1 = rospy.Publisher('DWM1001_Network_Anchor_1', String, queue_size=10)
pubblisher_Anchor_2 = rospy.Publisher('DWM1001_Network_Anchor_2', String, queue_size=10)
pubblisher_Anchor_3 = rospy.Publisher('DWM1001_Network_Anchor_3', String, queue_size=10)
pubblisher_Tag      = rospy.Publisher('DWM1001_Network_Tag', String, queue_size=10)



def main():

    #update dynamic configuratio
    updateDynamicConfiguration_SERIALPORT()
    # close the serial port in case the previous run didn't closed it properly
    serialPortDWM1001.close()
    # sleep for one sec
    time.sleep(1)
    # open serial port
    serialPortDWM1001.open()

    # check if the serial port is opened
    if(serialPortDWM1001.isOpen()):
        rospy.loginfo("Port opened: "+ str(SERIAL_PORT_DETAILS.name) );
        # start sending commands to the board so we can initialize the board
        initializeDWM1001API()
        # give some time to DWM1001 to wake up
        time.sleep(2)
        # send command lec, so we can get positions is CSV format
        serialPortDWM1001.write(DWM1001_API_COMMANDS.LEC)
        serialPortDWM1001.write(DWM1001_API_COMMANDS.SINGLE_ENTER)
        rospy.loginfo("Reading DWM1001 coordinates")
    else:
        rospy.loginfo("Can't open port: "+ str(SERIAL_PORT_DETAILS.name))

    try:

        while not rospy.is_shutdown():
            # just read everything from serial port
            serialReadLine = serialPortDWM1001.read_until()
            # sleep for 10Hz - because why not
            rate.sleep()

            """" Declare array that will hold network data such us coordinates of anchor and tag
                 split serial port message by comma ',' """
            networkDataArray = [ x.strip() for x in serialReadLine.strip().split(',') ]

            try:
                pubblishCoordinatesIntoTopics(networkDataArray)

            except IndexError:
                rospy.loginfo("Found index error in the network array!DO SOMETHING!")
            # print coordinates and info of the network
            rospy.loginfo(networkDataArray)


    except KeyboardInterrupt:
        rospy.loginfo("Quitting DWM1001 Shell Mode and closing port, allow 1 second for UWB recovery")
        serialPortDWM1001.write(DWM1001_API_COMMANDS.RESET)
        serialPortDWM1001.write(DWM1001_API_COMMANDS.SINGLE_ENTER)

    finally:
        rospy.loginfo("Quitting, and sending reset command to dev board")
        # serialPortDWM1001.reset_input_buffer()
        serialPortDWM1001.write(DWM1001_API_COMMANDS.RESET)
        serialPortDWM1001.write(DWM1001_API_COMMANDS.SINGLE_ENTER)
        rate.sleep()
        if "reset" in serialReadLine:
            rospy.loginfo("succesfully closed ")
            serialPortDWM1001.close()



def pubblishCoordinatesIntoTopics(networkDataArray):
    # Get numbers of anchors
    # DWM1001_NETWORK.anchors = networkDataArray[1]
    # TODO delete this after debugging
    rospy.loginfo("Number(s) of Anchors: " + networkDataArray[1])
    # TODO delete this after debugging
    rospy.loginfo("Length of array: " + str(len(networkDataArray)))


    # publish coordinates and info of the network
    pubblisher_Network.publish(str(networkDataArray))
    # pubblish coordinates for first anchor
    pubblisher_Anchor_0.publish(str(networkDataArray[SYS_DEFS.INDEX_22] + " "
                                    + networkDataArray[SYS_DEFS.INDEX_23] + " "
                                    + networkDataArray[SYS_DEFS.INDEX_24]))
    # publish coordinates for second anchor
    pubblisher_Anchor_1.publish(str(networkDataArray[SYS_DEFS.INDEX_16] + " "
                                    + networkDataArray[SYS_DEFS.INDEX_17] + " "
                                    + networkDataArray[SYS_DEFS.INDEX_18]))
    # publish coordinates for third anchor
    pubblisher_Anchor_2.publish(str(networkDataArray[SYS_DEFS.INDEX_4] + " "
                                    + networkDataArray[SYS_DEFS.INDEX_5] + " "
                                    + networkDataArray[SYS_DEFS.INDEX_6]))
    # publish coordinates for fourth anchor
    pubblisher_Anchor_3.publish(str(networkDataArray[SYS_DEFS.INDEX_10] + " "
                                    + networkDataArray[SYS_DEFS.INDEX_11] + " "
                                    + networkDataArray[SYS_DEFS.INDEX_12]))
    # publish coordinates for tag
    pubblisher_Tag.publish(str(networkDataArray[SYS_DEFS.INDEX_27] + " "
                               + networkDataArray[SYS_DEFS.INDEX_28] + " "
                               + networkDataArray[SYS_DEFS.INDEX_29]))



def updateDynamicConfiguration_SERIALPORT():
    global dynamicConfig_SERIAL_PORT

    # intialize dynamic configuration
    dynamicConfigServer = Server(DWM1001_Tune_SerialConfig, callbackDynamicConfig)
    # set close port to true
    dynamicConfig_CLOSE_PORT.update({"close_port": True})
    # set the open port to false
    dynamicConfig_OPEN_PORT.update({"open_port" : False})
    # update the server
    dynamicConfigServer.update_configuration(dynamicConfig_OPEN_PORT)
    dynamicConfigServer.update_configuration(dynamicConfig_CLOSE_PORT)
    # update the server with opened port
    dynamicConfig_CLOSE_PORT.update({"close_port": False})
    # update the server with close port
    dynamicConfig_OPEN_PORT.update({"open_port": True})
    # update name of serial port in dynamic configuration
    dynamicConfig_SERIAL_PORT = {"serial_port": str(SERIAL_PORT_DETAILS.name)}
    # now update server configuration
    dynamicConfigServer.update_configuration(dynamicConfig_OPEN_PORT)
    dynamicConfigServer.update_configuration(dynamicConfig_OPEN_PORT)
    dynamicConfigServer.update_configuration(dynamicConfig_CLOSE_PORT)
    dynamicConfigServer.update_configuration(dynamicConfig_SERIAL_PORT)

def initializeDWM1001API():
    # reset incase previuos run didn't close properly
    serialPortDWM1001.write(DWM1001_API_COMMANDS.RESET)
    # send ENTER two times in order to access api
    serialPortDWM1001.write(DWM1001_API_COMMANDS.SINGLE_ENTER)
    # sleep for half a second
    time.sleep(0.5)
    serialPortDWM1001.write(DWM1001_API_COMMANDS.SINGLE_ENTER)
    # sleep for half second
    time.sleep(0.5)
    # send a third one - why not
    serialPortDWM1001.write(DWM1001_API_COMMANDS.SINGLE_ENTER)



""" TODO use this for future maintanance, when you want to control DWM from joy
    Receives joystick messages (subscribed to Joy topic) """
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


