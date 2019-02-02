/**
*	This file is part of Drone WayPointer.
*	
*   Copyright 2014 The University of Sheffield (www.sheffield.ac.uk)
*	Copyright 2014 Stefanos Giagkiozis < SteveGiagkiozis@gmail.com >
*
*    Drone WayPointer is free software: you can redistribute it and/or modify
*    it under the terms of the GNU General Public License as published by
*    the Free Software Foundation, either version 3 of the License, or
*    (at your option) any later version.
*
*    Drone WayPointer is distributed in the hope that it will be useful,
*    but WITHOUT ANY WARRANTY; without even the implied warranty of
*    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*    GNU General Public License for more details.
*
*    You should have received a copy of the GNU General Public License
*    along with Drone WayPointer.  If not, see <http://www.gnu.org/licenses/>.
**/

#ifndef drone_waypointer_QNODE_HPP_
#define drone_waypointer_QNODE_HPP_

#ifndef Q_MOC_RUN
#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <geometry_msgs/Pose.h>
#include <std_msgs/Empty.h>
#include <ardrone_autonomy/Navdata.h>
#include <nav_msgs/Odometry.h>
#include <sensor_msgs/Image.h>
#include <image_transport/image_transport.h>
#include <sensor_msgs/image_encodings.h>
#include <math.h>
#include <cv_bridge/cv_bridge.h>
#include <opencv/cv.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <image_transport/image_transport.h>
#endif

#include <string>
#include <QThread>
#include <QStringListModel>


namespace enc = sensor_msgs::image_encodings;
namespace drone_waypointer {

class QNode : public QThread {
    Q_OBJECT
public:
	QNode(int argc, char** argv );
	virtual ~QNode();
	bool init();
	bool init(const std::string &master_url, const std::string &host_url);
	void run();

	// Callbacks
	void navDataCallback(const ardrone_autonomy::Navdata& nav_msg);
	void frontImageCallback(const sensor_msgs::ImageConstPtr& front_image_msg);
	void bottomImageCallback(const sensor_msgs::ImageConstPtr& bottom_image_msg);
	void realPoseCallBack(const nav_msgs::Odometry& realPoseData);
	void estimatedPoseCallback(const nav_msgs::Odometry& pose_msg);

	void command(float xv,float yv,float zv, float xr, float yr, float zr);
	// Public attributes
	int actionCode;
	int droneState;
	int battery;
 	int currentWaypointPtr; // Waypoint reached counter
 	int currentSavedWaypointPtr;// Saved waypoints counter

 	//std::string realPoseTopic;
	cv_bridge::CvImagePtr CV_front_image_ptr;
	cv_bridge::CvImagePtr CV_bottom_image_ptr;





	// Target Co-ordinates
	geometry_msgs::Pose targetInMap;
	geometry_msgs::Pose targetInDrone; // Also used as the error for the controllers
	
	// Z-axis Rotation from NavData
	float navDataRotZ360;
	float navDataRotZ;

	// Real and Estimated Position of Drone
 	geometry_msgs::PoseWithCovariance realPose;
 	geometry_msgs::PoseWithCovariance externalEstimatedPose;
	geometry_msgs::Pose estimatedPoseDR;
 	std::string estimatorTopic;
 	int poseEstimationMethod; // 1 - Simulation, 2 - External, 3 - Internal Dead Reckoning

 	// Last Saved Waypoint to determine the next point that we want to save
 	geometry_msgs::Pose lastSavedWaypoint;
 	bool recordFlightPath;
 	bool recordData;
	bool recordImages;

 	// Controller Attributes
 	float angleAccuracy;
 	float waypointAccuracy;
 	float pointGain;
 	float angleGain;

 	// A collection of Data and measurements of the state of the drone
 	struct droneMeasurementData{

 		ros::Time timeStamp;
 		// ACtual Drone Position
 		float x;
 		float y;
 		float z;

 		// Measured Drone Velocities
 		float xVel;
 		float yVel;
 		float zVel;

 		// Measured Drone Accelerations
 		float xAcc;
 		float yAcc;
 		float zAcc;

 		//Measured Drone Orientation
 		float xRot;
 		float yRot;
 		float zRot;

 		// Measured Dron Angular Velocities
 		float xRotVel;
 		float yRotVel;
 		float zRotVel;
 		/*
 		// Motor PWM values
 		float motor1;
 		float motor2;
 		float motor3;
 		float motor4;
 		*/
 	} currentDroneData, lastDroneData;

 	// Sampling Flags
 	bool firstTimeSamplingData;
 	bool samplingFrontCamera;

 	// Sampling times
 	ros::Time lastDataSampleTime;
 	ros::Time lastFlightpathSampleTime;
 	ros::Time lastImageSampleTime;
 	float imageSamplingTime;
 	//-------------
 	// Safety-Loops
 	//-------------
 	int wayHomePtr;
 	geometry_msgs::Pose lastSavedWayHomePoint;

 	// Thresholds and test Signals
 	bool wasGoingBack;
 	bool safeFlight;
 	bool noWifi;
 	float batteryLandThreshold;
 	float batteryGoHomeThreshold;
 	bool testBatteryBellowLand;
 	bool testBatteryBellowGoHome;
 	bool testNoWifi;

Q_SIGNALS:
	void dataUpdated();
	void imageUpdated();
    void rosShutdown();
    void realPoseUpdated();
    void targetUpdated();
    void requestNewWaypoint();
    void dataReady();
	void imageReady();
    void sampleFlightpath();
    void estimatedPoseUpdated();
    void externalEstimatedPoseUpdated();
    void sampleWayHome();
    void goHome();
    void updateWayHomeFinalPoint();
    
private:
	int init_argc;
	char** init_argv;
    // Publishers
    ros::Publisher pub_takeoff;
	ros::Publisher pub_twist;
	ros::Publisher pub_land;
	ros::Publisher pub_reset;
	ros::Publisher pub_camSelect;

	// Subscribers
	ros::Subscriber sub_navData;
	ros::Subscriber sub_image_front;
	ros::Subscriber sub_image_bottom;
	ros::Subscriber sub_real_pose;
	ros::Subscriber sub_external_estimator;

	// Message Constants
	geometry_msgs::Twist msg_twist;
	std_msgs::Empty emp_msg;

	bool latched;
	ros::Time latchStartTime;

	geometry_msgs::Twist setupTwist(float xv,float yv,float zv, float xr, float yr, float zr);
	void returnTargetInDrone(geometry_msgs::Pose target);
	
 	// Waypoint Functions
 	bool wayPointReached(float tolerance);
 	bool wayPointFaced(float tolerance);
 	void saveFlightPath();
 	void sampleData();
    void sampleImage();
    void estimatePoseDeadReckoning();

    // Safety-Loops
    void decideSafetyAction();

};
}  // namespace drone_waypointer
#endif /* drone_waypointer_QNODE_HPP_ */
/*Control_QNODE_HPP_ */
