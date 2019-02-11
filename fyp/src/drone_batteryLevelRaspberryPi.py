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

import os
import rospy
# import Raspi UPS Hat library
import raspiupshat


publisherAidBatteryLevelRaspberryPi  = rospy.Publisher('aid/batteryLevelRaspberryPi', int, queue_size=10)
publisherAidVoltageLevelRaspberryPi  = rospy.Publisher('aid/voltageLevelRaspberryPi', int, queue_size=10)

# init Raspi UPS Hat
raspiupshat.init();

rate = rospy.Rate(10) # 10hz

while not rospy.is_shutdown():

    # Get info
    rospy.loginfo("Voltage:%5.2fV" % raspiupshat.getv())
    rospy.loginfo("Battery:%5i%%" % raspiupshat.getsoc())

    publisherAidBatteryLevelRaspberryPi.publish(raspiupshat.getsoc())
    publisherAidVoltageLevelRaspberryPi.publish(raspiupshat.getv())

    if raspiupshat.getsoc() == 100:
        rospy.loginfo("Battery FULL")
    if raspiupshat.getsoc() < 20:
        rospy.loginfo("Battery LOW")
    while 1:
        if raspiupshat.getsoc() < 5:
            rospy.loginfo("System will shutdown now,bye!")
            os.system("sudo shutdown")

    rate.sleep()