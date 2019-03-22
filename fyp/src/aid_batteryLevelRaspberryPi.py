#!/usr/bin/env python

# Raspi UPS Hat
# We only provide 2 interfave to get battery information;
#
#Interface 1:
#Function: get current battery voltage
#Return value: battery voltage;
#float getv();

#Interface 2:
#Function:    get battery capacity
#Return value: 0~100
#float getsoc();
#


from aid_systemDefinitions       import SYS_DEFS
__author__     = SYS_DEFS.AUTHOR
__version__    = SYS_DEFS.VERSION
__maintainer__ = SYS_DEFS.MAINTAINER
__email__      = SYS_DEFS.EMAIL
__status__     = SYS_DEFS.STATUS

import struct
import smbus
import sys
import time
import os
import rospy
from std_msgs.msg import Int16

state_charge = (3.622, 3.832, 4.043, 4.182, 4.21)
state_discharge = (4.17, 3.74751, 3.501, 3.35, 2.756)
state_charging = False;
v_current = 0;
v_old = 0;
capacity = 0;


rospy.init_node('aid', anonymous=False)
rate = rospy.Rate(10)  # 10hz
publisherAidBatteryLevelRaspberryPi = rospy.Publisher('aid/batteryLevelRaspberryPi', Int16, queue_size=10 )
publisherAidVoltageLevelRaspberryPi = rospy.Publisher('aid/voltageLevelRaspberryPi', Int16, queue_size=10 )


def readVoltage(bus):

    "This function returns as float the voltage from the Raspi UPS Hat via the provided SMBus object"
    address = 0x36
    read = bus.read_word_data(address, 2)
    swapped = struct.unpack("<H", struct.pack(">H", read))[0]
    voltage = swapped * 78.125 / 1000000
    return voltage


def readCapacity(bus):
    "This function returns as a float the remaining capacity of the battery connected to the Raspi UPS Hat via the provided SMBus object"
    address = 0x36
    read = bus.read_word_data(address, 4)
    swapped = struct.unpack("<H", struct.pack(">H", read))[0]
    capacity = swapped / 256
    return capacity


bus = smbus.SMBus(1)  # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

v_old = readVoltage(bus)
v_current = v_old



if (v_current > state_charge[4]):
    capacity = 100
elif ((v_current < state_charge[4]) and (v_current >= state_charge[3])):
    capacity = (v_current - state_charge[3]) / ((state_charge[4] - state_charge[3]) / 25) + 75
elif ((v_current < state_charge[3]) and (v_current >= state_charge[2])):
    capacity = (v_current - state_charge[2]) / ((state_charge[3] - state_charge[2]) / 25) + 50
elif ((v_current < state_charge[2]) and (v_current >= state_charge[1])):
    capacity = (v_current - state_charge[1]) / ((state_charge[2] - state_charge[1]) / 25) + 25
elif ((v_current < state_charge[1]) and (v_current >= state_charge[0])):
    capacity = (v_current - state_charge[0]) / ((state_charge[1] - state_charge[0]) / 25)
else:
    capacity = 0

while not rospy.is_shutdown():

    # Get info
    rospy.loginfo("Voltage:%5.2fV" % readVoltage(bus))
    rospy.loginfo("Battery:%5i%%" % capacity)

    publisherAidBatteryLevelRaspberryPi.publish(capacity)
    publisherAidVoltageLevelRaspberryPi.publish(readVoltage(bus))

    if capacity == 100:
        rospy.loginfo("Battery FULL")
    if capacity < 20:
        rospy.loginfo("Battery LOW")
    if capacity < 5:
    	rospy.loginfo("System will shutdown now,bye!")
        os.system("sudo shutdown")

    rate.sleep()

