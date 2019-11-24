#!/usr/bin/env python
import rospy
#import IPython
from geometry_msgs.msg import PoseStamped, TwistStamped, Twist, Vector3, Pose
from mavros_msgs.msg import PositionTarget, AttitudeTarget, State
from mavros_msgs.srv import SetMode, SetModeRequest
from std_msgs.msg import Float64



class Tuner():

    def __init__(self):
        self.pos = None
        self.vel = None
        self.att = None
        self.rate = None
        self.pos_sp_read = None
        self.vel_sp_read = None
        self.att_sp_read = None
        self.rate_sp_read = None

        self.state = "INIT"


    def init(self):
        #Start node
        rospy.init_node('tuner', anonymous=True)

        # Set mode service
        rospy.wait_for_service('/mavros/set_mode')  #Wait until the service is available
        self.set_mode_srv = rospy.ServiceProxy('/mavros/set_mode', SetMode)  #Making a service proxy

        # Set position and velocity setpoint
        self.set_pose_pub = rospy.Publisher('/mavros/setpoint_position/local', PoseStamped, queue_size=10)
        self.set_vel_pub = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel', TwistStamped, queue_size=10)

        # Set attitude and rates setpoint
        self.set_att_pub = rospy.Publisher('/mavros/setpoint_attiude/attitude', PoseStamped, queue_size=10)
        self.set_thr_pub = rospy.Publisher('/mavros/setpoint_attiude/att_throttle', Float64, queue_size=10)
        self.set_rate_pub = rospy.Publisher('/mavros/setpoint_attiude/cmd_vel', TwistStamped, queue_size=10)

        # View position and velocity setpoint
        rospy.Subscriber("/mavros/setpoint_raw/local", PositionTarget , self.pose_sp_callback)                # View setpoint
        # View attitude and rate setpoint
        rospy.Subscriber("/mavros/setpoint_raw/attitude", AttitudeTarget , self.att_sp_callback)

        # View actual position and atttitde
        rospy.Subscriber("/mavros/local_position/pose", PoseStamped , self.pose_callback)
        # View actual velocity and rates
        rospy.Subscriber("/mavros/local_position/velocity", TwistStamped , self.vel_callback)

        rospy.Subscriber("/mavros/state",State, self.state_callback)

    def run(self):
        count = 0
        rate = rospy.Rate(100)
        while not rospy.is_shutdown():
            att_cmd = PoseStamped()
            att_cmd.pose = Pose()
            att_cmd.pose.position.x = 0
            att_cmd.pose.position.y = 0
            att_cmd.pose.position.z = 0
            if self.state == "INIT":
                for i in range(0,100):
                    #self.set_pose_pub.publish(att_cmd)
                    self.set_att_pub.publish(att_cmd)
                    self.set_thr_pub.publish(Float64(0.5))
                    rate.sleep()
                self.state = "MODE"
            elif self.state == "MODE":
                self.set_mode_srv(0,"OFFBOARD")
                self.state = "MAIN"

            elif self.state =="MAIN":
                #self.set_pose_pub.publish(att_cmd)
                self.set_att_pub.publish(att_cmd)
                self.set_thr_pub.publish(Float64(0.5))

                #rospy.loginfo(pos_cmd)
            rate.sleep()



    def state_callback(self,mav_state):
        rospy.loginfo(mav_state)


    def pose_callback(self,mav_pose):
        #rospy.loginfo(mav_pose)
        #IPython.embed()
        self.pos = mav_pose.pose.position
        self.att = mav_pose.pose.orientation

    def vel_callback(self,mav_vel):
        #rospy.loginfo(mav_vel)
        self.vel = mav_vel.twist.linear
        self.rate = mav_vel.twist.angular

    def pose_sp_callback(self,target_pose):
        self.pos_sp_read = target_pose.position
        self.vel_sp_read = target_pose.velocity

    def att_sp_callback(self,target_att):
        self.att_sp_read = target_att.orientation
        self.rate_sp_read = target_att.body_rate



if __name__ == '__main__':
    node = Tuner()
    node.init()
    node.run()