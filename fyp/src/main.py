#!/usr/bin/env python
import rospy
from std_msgs.msg import String
# Load the DroneController class, which handles interactions with the drone, and the DroneVideoDisplay class, which handles video display
from drone_controller import BasicDroneController
import roslib
import rospy
# Import the joystick message
from sensor_msgs.msg import Joy
import time
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
# An enumeration of Drone Statuses
from drone_status import DroneStatus
import position_functions as pf

# define the default mapping between joystick buttons and their corresponding actions of autonomus flight
AutonomousFlight 		= 11
StopAutonomousFlight    = 7
EmergencyStop           = 6


vx = vy = vz = ax = ay = az = 0.0
x = y = z = alfa = betta = gamma = 0.0


command = Twist()

pub_takeoff = rospy.Publisher('/ardrone/takeoff', Empty)
pub_land = rospy.Publisher('/ardrone/land', Empty)
pub_position = rospy.Publisher('/cmd_vel', Twist, queue_size=10)


# -linear.x: move backward
# +linear.x: move forward
# -linear.y: move right
# +linear.y: move left
# -linear.z: move down
# +linear.z: move up
# -angular.z: turn right
# +angular.z: turn left

# Button 6 is when we start autonomus flight, GOOD LUCK!!!
def ReceiveJoystickMessage(data):
    global pitch

    if data.buttons[AutonomousFlight] == 1:
        rospy.loginfo("STARTING Autonomous Flight, button " + str(AutonomousFlight) + " pressed!")

        copter = pf.DroneMaster()
        functionList = (
            ('move_right_left', 0.5),
            ('move_left_right', 0.5),
            ('move_up_down', 0.3),
            ('move_down_up', 0.3),
            ('move_yaw_left_right', 5),
            ('move_yaw_right_left', 5)
        )



        copter.takeoff()
        time.sleep(5)
        copter.clear()
        copter.goTo(0.5, 0.00, 0.00, 0.02)
        rospy.loginfo('x=' + str(round(copter.x, 3)) + '; y=' + str(round(copter.y, 3)) + '; z=' + str(round(copter.z, 3)))

        #rospy.loginfo("Go Back ")
        #copter.goTo(0.00, 0.00, 0.00, 0.02)

        if 1.00 <= copter.x  <= 1.10:
            copter.land()

        #time.sleep(2)
        #copter.land()



       # if controller.status == DroneStatus.Emergency:
        #    controller.SendEmergency()
        """
        rospy.loginfo("ready!")
        rospy.sleep(1.0)

        rospy.loginfo("takeoff..")
        pub_takeoff.publish(Empty())

        rospy.loginfo("move x positive")

        command.linear.x = 1
        pub_position.publish(command)

        rospy.sleep(2.0)

        rospy.loginfo("land..")
        pub_land.publish(Empty())

        rospy.loginfo("done!")
        
        elif controller.status == DroneStatus.Flying or controller.status == DroneStatus.GotoHover or controller.status == DroneStatus.Hovering:
            rospy.loginfo("Drone is flying")
            time.sleep(2)
            controller.SendEmergency()


        controller.SendTakeoff()
        time.sleep(4)

        if controller.status == DroneStatus.Flying or controller.status == DroneStatus.GotoHover or controller.status == DroneStatus.Hovering:
            command = Twist()
            command.linear.x = 0
            command.linear.y = 0
            command.linear.z = 1

            command.angular.x = 0
            command.angular.y = 0
            command.angular.z = 0
            pub_position.publish(command)

            # rospy.loginfo("Sending__ " + str(command))

            for x in range(0, 9):
                command.linear.x += 0.1
                #command.angular.z += 0.1
                rospy.loginfo("Sending command: " + str(command))
                pub_position.publish(command)
                time.sleep(1)

            rospy.loginfo("Sending__emergency ")
            controller.SendEmergency()


"""

        # controller.SendEmergency()
        # time.sleep(2)
        # controller.SendTakeoff()

    elif data.buttons[StopAutonomousFlight] == 1:
        rospy.loginfo("STOPPING Autonomous Flight, button " + str(AutonomousFlight) + " pressed!")
        controller.SendLand()
    elif data.buttons[EmergencyStop] == 1:
        rospy.loginfo("EMERGENCY, STOPPING Autonomous Flight, button " + str(AutonomousFlight) + " pressed!")
        controller.SendEmergency()



# Setup the application
if __name__ == '__main__':
    # Firstly we setup a ros node, so that we can communicate with the other packages
    rospy.init_node('fyp', anonymous=False)

    # Now we construct our controllers
    controller = BasicDroneController()

    # subscribe to the /joy topic and handle messages of type Joy with the function ReceiveJoystickMessage
    subJoystick = rospy.Subscriber('/joy', Joy, ReceiveJoystickMessage)




    rospy.spin()