/**
 * This file is part of ORB-SLAM2.
 *
 * Copyright (C) 2014-2016 Raúl Mur-Artal <raulmur at unizar dot es> (University of Zaragoza)
 * For more information see <https://github.com/raulmur/ORB_SLAM2>
 *
 * ORB-SLAM2 is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * ORB-SLAM2 is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with ORB-SLAM2. If not, see <http://www.gnu.org/licenses/>.
 */


#include <iostream>
#include <algorithm>
#include <fstream>
#include <random>
#include <chrono>
#include <time.h>
#include <math.h>

#include <ros/ros.h>

#include <sensor_msgs/PointCloud.h>
#include <cv_bridge/cv_bridge.h>
#include <geometry_msgs/PoseWithCovarianceStamped.h>
#include <tf2/LinearMath/Quaternion.h>
#include <tf2/LinearMath/Vector3.h>
#include <tf2/convert.h>
#include <tf2/LinearMath/Transform.h>

#include<opencv2/core/core.hpp>

#include <System.h>
#include <tf/transform_broadcaster.h>
#include <tf/transform_listener.h>
#include <tf2_ros/transform_broadcaster.h>
#include <geometry_msgs/TransformStamped.h>
#include <tf/transform_datatypes.h>
#include <tf2/LinearMath/Matrix3x3.h>

using namespace std;

class ImageGrabber {
public:
     ImageGrabber ( ORB_SLAM2::System *pSLAM ) : mpSLAM ( pSLAM ), pc() {
          pc.header.frame_id = "/first_keyframe_cam";
          pose_out_.header.frame_id = "nav";
     }
     void GrabImage ( const sensor_msgs::ImageConstPtr &msg );
     geometry_msgs::TransformStamped toTFStamped ( tf2::Transform in , ros::Time t, string frame_id, string child_frame_id );
     tf::Transform cvMatToTF ( cv::Mat Tcw );

     ORB_SLAM2::System *mpSLAM;

     bool initialized = false;
     bool debug_mode = false;

     sensor_msgs::PointCloud pc;
     geometry_msgs::PoseWithCovarianceStamped pose_out_;

     tf::TransformListener tf_listener;

     tf::TransformBroadcaster br;

     tf::StampedTransform base_link_to_camera_transform;
     tf::StampedTransform odom_to_second_keyframe_base_transform;
     tf::Transform second_keyframe_cam_to_first_keyframe_cam_transform;
     tf::StampedTransform base_link_to_camera_transform_no_translation;
};

int main ( int argc, char **argv )
{
     ros::init ( argc, argv, "Mono" );
     ros::start();

     if ( argc != 3 ) {
          cerr << endl << "Usage: rosrun ORB_SLAM2 Mono path_to_vocabulary path_to_settings" << endl;
          ros::shutdown();
          return 1;
     }

     // Create SLAM system. It initializes all system threads and gets ready to process frames.
     ORB_SLAM2::System SLAM ( argv[1], argv[2], ORB_SLAM2::System::MONOCULAR, true );

     ImageGrabber igb ( &SLAM );

     ros::NodeHandle nodeHandler;
     ros::Subscriber sub = nodeHandler.subscribe ( "/camera/image_raw", 1, &ImageGrabber::GrabImage, &igb );
     ros::Publisher pc_pub = nodeHandler.advertise<sensor_msgs::PointCloud> ( "/orb/point_cloud", 2 );
     ros::Publisher pose_pub = nodeHandler.advertise<geometry_msgs::PoseWithCovarianceStamped> ( "/orb/pose_unscaled", 2 );

     ros::Rate loop_rate ( 30 );

     while ( ros::ok() ) {
          ros::spinOnce();
          if ( igb.initialized ) {
               pc_pub.publish ( igb.pc );
               pose_pub.publish ( igb.pose_out_ );
          }
          loop_rate.sleep();
     }

     // Stop all threads
     SLAM.Shutdown();

     ros::shutdown();

     return 0;
}

//callback
void ImageGrabber::GrabImage ( const sensor_msgs::ImageConstPtr &msg )
{

     // Copy the ros image message to cv::Mat.
     cv_bridge::CvImageConstPtr cv_ptr;
     try {
          cv_ptr = cv_bridge::toCvShare ( msg );
     } catch ( cv_bridge::Exception &e ) {
          ROS_ERROR ( "cv_bridge exception: %s", e.what() );
          return;
     }
     //     Main slam routine. Extracts new pose
     // (from ORB_SLAM2 API)
     // Proccess the given monocular frame
     // Input images: RGB (CV_8UC3) or grayscale (CV_8U). RGB is converted to grayscale.
     // Returns the camera pose (empty if tracking fails).
     cv::Mat Tcw = mpSLAM->TrackMonocular ( cv_ptr->image, cv_ptr->header.stamp.toSec() );
     ros::Time t = msg->header.stamp;


     //////////////////////////////////TRANSFORMATIONS//////////////////////////////////////////////////////////////////
     //To fuse the orb SLAM pose estimate with the Kalman Filter of the robot_localization package, it is
     //necessary to publish any other sensor data and the orb SLAM data in a conforming parent frame which is typically
     //called 'odom'. See REP105 and REP103 on ros.org for further details on the concept.
     //
     //The final transformation for the orb SLAM looks like this:
     //
     //		odom --> first_keyframe (orb initialization) --> orb_pose --> correction
     //
     //odom is defined by the IMU at startup (this is not the startup time of the driver node but the time the plug
     //of the drone is connected) and published by the ardrone driver. Odom must not be changed at any time afterwards.
     //
     //The first keyframe transformation is set once the orb slam initializes (meaning it is able to estimate a position
     //for the first time). It is set to be the transformation from odom to ardrone_base_frontcam (published by the driver).
     //Odom is defined relative to the real world in a way that g(ravitation) is facing in negative z direction. This means
     //that 0 roll and 0 pitch ALWAYS means that the drone is in the horizontal plane of the earth. Since the IMU is not
     //able to make a reasonable yaw estimate itself, it uses the (arbitrary) direction of the drone at the time point where
     //the plug on the drone is connected as 0 yaw. This value will not change until the drone itself is shut off (regardless
     //of the driver node being turned on and off).
     //
     //Camera frames for some reason always come in a way such that the z axis is pointing forwards while the y axis is
     //facing downwards. This has to be corrected through a manual rotation such that eventually the orb pose values
     //which are beeing publsihed to a PoseWithCovarianceStamped topic represent the correct pose within the odom frame.
     //See the rqt_tf_tree for further calrification on the single transformations this code is performing.
     //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


     // if points can be tracked then broadcast the pose
     if ( not Tcw.empty() ) {

          if ( not initialized ) { // TODO: find first keyframe from first pose by
               //Initialization - set link between 'odom' and 'first_keyframe' frames

               try {
                    tf_listener.lookupTransform ( "nav", "/base_link", ros::Time ( 0 ), odom_to_second_keyframe_base_transform );
                    tf_listener.lookupTransform ( "/base_link", "/ardrone_base_frontcam", ros::Time ( 0 ), base_link_to_camera_transform );
                    second_keyframe_cam_to_first_keyframe_cam_transform = cvMatToTF ( Tcw );

                    odom_to_second_keyframe_base_transform.setOrigin ( tf::Vector3 ( 0, 0, 0 ) );

               } catch ( tf::LookupException e ) {
                    cout << e.what() << endl;
               }

               base_link_to_camera_transform_no_translation = base_link_to_camera_transform;
               base_link_to_camera_transform_no_translation.setOrigin ( tf::Vector3 ( 0.0, 0.0, 0.0 ) );

               initialized = true;
          }


          //tf::Transform cam_to_first_keyframe_transform = cvMatToTF ( Tcw );
          tf::Transform orb_pose_unscaled_cam_to_first_keyframe_cam = cvMatToTF ( Tcw );




          //if ( debug_mode ) {
               // odom to second_keyframe_base_link
               br.sendTransform ( tf::StampedTransform ( odom_to_second_keyframe_base_transform, t, "nav", "/second_keyframe_base_link" ) );

               // second_keyframe_base_link to second_keyframe_cam
               br.sendTransform ( tf::StampedTransform ( base_link_to_camera_transform_no_translation, t, "/second_keyframe_base_link", "/second_keyframe_cam" ) );

               // second_keyframe_cam to first_keyframe_cam
               br.sendTransform ( tf::StampedTransform ( second_keyframe_cam_to_first_keyframe_cam_transform.inverse(), t, "/second_keyframe_cam", "/first_keyframe_cam" ) );

               // first_keyframe_cam to first_keyframe_base_link
               br.sendTransform ( tf::StampedTransform ( base_link_to_camera_transform_no_translation.inverse(), t, "/first_keyframe_cam", "/first_keyframe_base_link" ) );

               // first_keyframe_cam to orb_pose_unscaled_cam
               br.sendTransform ( tf::StampedTransform ( orb_pose_unscaled_cam_to_first_keyframe_cam, t, "/first_keyframe_cam", "/orb_pose_unscaled_cam" ) );

               // orb_pose_unscaled_cam to orb_pose_unscaled
               br.sendTransform ( tf::StampedTransform ( base_link_to_camera_transform_no_translation.inverse(), t, "/orb_pose_unscaled_cam", "/orb_pose_unscaled" ) );
         // } else {
               tf::Transform output = odom_to_second_keyframe_base_transform
                                      * base_link_to_camera_transform_no_translation
                                      * second_keyframe_cam_to_first_keyframe_cam_transform.inverse()
                                      * base_link_to_camera_transform_no_translation.inverse();
               //br.sendTransform(tf::StampedTransform(output , t, "nav", "/first_keyframe_base_link"));
         // }

          tf::Transform pose_out = odom_to_second_keyframe_base_transform
                                   * base_link_to_camera_transform_no_translation
                                   * second_keyframe_cam_to_first_keyframe_cam_transform.inverse()
                                   * orb_pose_unscaled_cam_to_first_keyframe_cam
                                   * base_link_to_camera_transform_no_translation.inverse();

          //generate pose for robot_localization EKF sensor fusion
          //the pose is simply generated from the above derived transformations
          pose_out_.header.stamp = t;

          tf::Quaternion pose_orientation = pose_out.getRotation();
          tf::Vector3 pose_origin = pose_out.getOrigin();
          pose_out_.pose.pose.orientation.x = pose_orientation.getX();
          pose_out_.pose.pose.orientation.y = pose_orientation.getY();
          pose_out_.pose.pose.orientation.z = pose_orientation.getZ();
          pose_out_.pose.pose.orientation.w = pose_orientation.getW();
          pose_out_.pose.pose.position.x = pose_origin.getX();
          pose_out_.pose.pose.position.y = pose_origin.getY();
          pose_out_.pose.pose.position.z = pose_origin.getZ();

          ///////////////////////////////////////////////////////////////////////////////////////////////////////77
          //TODO: Set covariance
          /////////////////////////////////////////////////////////////////////////////////////////////////////////
          for ( auto & x : pose_out_.pose.covariance ) {
               x = 0.0;
          }

          pose_out_.pose.covariance[0] = 1;
          pose_out_.pose.covariance[7] = 1;
          pose_out_.pose.covariance[14] = 1;
          pose_out_.pose.covariance[21] = 1;
          pose_out_.pose.covariance[28] = 1;
          pose_out_.pose.covariance[35] = 1;
     }

// gets points from most recent frame
// gets all points
     const std::vector<ORB_SLAM2::MapPoint *> &point_cloud = mpSLAM->mpMap->GetAllMapPoints();
// TODO: make efficient (use mpSLAM->GetTrackedMapPoints() to get most recent points)
     pc.points.clear();
     for ( size_t i = 0; i < point_cloud.size(); i++ ) {
          if ( point_cloud[i]->isBad() /* or spRefMPs.count(vpMPs[i])*/ ) {
               continue;
          }
          cv::Mat pos = point_cloud[i]->GetWorldPos();
          geometry_msgs::Point32 pp;
          pp.x = pos.at<float> ( 0 );
          pp.y = pos.at<float> ( 1 );
          pp.z = pos.at<float> ( 2 );

          pc.points.push_back ( pp );
     }

}

tf::Transform ImageGrabber::cvMatToTF ( cv::Mat Tcw )
{
     tf::Transform cam_to_first_keyframe_transform;
     // invert since Tcw (transform from world to camera)
     cv::Mat pose = Tcw.inv();

     //Extract transformation from the raw orb SLAM pose
     tf::Vector3 origin;
     //tf::Quaternion transform_quat;
     tf::Matrix3x3 transform_matrix;

     origin.setValue ( pose.at<float> ( 0, 3 ), pose.at<float> ( 1, 3 ), pose.at<float> ( 2, 3 ) );

     transform_matrix.setValue ( pose.at<float> ( 0, 0 ), pose.at<float> ( 0, 1 ), pose.at<float> ( 0, 2 ),
                                 pose.at<float> ( 1, 0 ), pose.at<float> ( 1, 1 ), pose.at<float> ( 1, 2 ),
                                 pose.at<float> ( 2, 0 ), pose.at<float> ( 2, 1 ), pose.at<float> ( 2, 2 ) );

     //transform_matrix.getRotation(transform_quat);
     cam_to_first_keyframe_transform.setOrigin ( origin );
     cam_to_first_keyframe_transform.setBasis ( transform_matrix );

     return cam_to_first_keyframe_transform;
}

