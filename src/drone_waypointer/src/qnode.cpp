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
#ifndef Q_MOC_RUN
#include <ros/ros.h> 
#include <ros/network.h>
#include <ardrone_autonomy/Navdata.h>
#include <geometry_msgs/Twist.h>
#include "../include/drone_waypointer/qnode.hpp"
#include <std_msgs/Empty.h>
#include <std_msgs/String.h>

#endif

#include <string>
#include <sstream>

#define _USE_MATH_DEFINES
namespace drone_waypointer {

QNode::QNode(int argc, char** argv ) :
	init_argc(argc),
	init_argv(argv)
	{}

QNode::~QNode() {
    if(ros::isStarted()) {
      ros::shutdown(); // explicitly needed since we use ros::start();
      ros::waitForShutdown();
    }
	wait();
}

// Constructor
bool QNode::init() {
	ros::init(init_argc,init_argv,"drone_waypointer");
	if ( ! ros::master::check() ) {
		return false;
	}
	ros::start(); // explicitly needed since our nodehandle is going out of scope.
	ros::NodeHandle n;
	// Publishers
	pub_takeoff = n.advertise<std_msgs::Empty>("/ardrone/takeoff",1);
	pub_land = n.advertise<std_msgs::Empty>("/ardrone/land",1);
	pub_twist = n.advertise<geometry_msgs::Twist>("/cmd_vel",1);
	pub_reset = n.advertise<std_msgs::Empty>("ardrone/reset",1);
	// Subscribers
	sub_navData = n.subscribe("/ardrone/navdata" , 1 , &QNode::navDataCallback, this );
	sub_image_front = n.subscribe("ardrone/front/image_raw" ,1 , &QNode::frontImageCallback, this);
	sub_image_bottom = n.subscribe("ardrone/bottom/image_raw" ,1 , &QNode::bottomImageCallback, this);
	sub_real_pose = n.subscribe("/ground_truth/state" ,1 , &QNode::realPoseCallBack, this);
	sub_external_estimator = n.subscribe(estimatorTopic, 1, &QNode::estimatedPoseCallback, this);
	// Initial Conditions
	msg_twist = setupTwist(0,0,0,0,0,0);
	navDataRotZ = 0;
	navDataRotZ360 = 0;
	actionCode = 0;
	targetInMap.position.x = 0;
	targetInMap.position.y = 0;
	targetInMap.position.z = 0;
	targetInMap.orientation.x = 0;
	targetInMap.orientation.y = 0;
	targetInMap.orientation.z = 0;
	lastSavedWaypoint.position.x = 0;
	lastSavedWaypoint.position.y = 0;
	lastSavedWaypoint.position.z = 0;
	currentWaypointPtr = -1;
	currentSavedWaypointPtr = 0;
	angleAccuracy = 10;
	waypointAccuracy = 0.15;
	pointGain = 0.5;
	angleGain = 0.5;
	recordFlightPath = false;
	recordData = true;
	recordImages = true;
	lastDroneData.xRot = 0;
	lastDroneData.yRot = 0;
	lastDroneData.zRot = 0;
	firstTimeSamplingData = true;
	latched = false;
	lastDataSampleTime = ros::Time::now();
	samplingFrontCamera = false;
	poseEstimationMethod = 3;
	estimatedPoseDR.position.x = 0;
	estimatedPoseDR.position.y = 0;
	estimatedPoseDR.position.z = 0;
	externalEstimatedPose.pose.position.x = 0;
	externalEstimatedPose.pose.position.y = 0;
	externalEstimatedPose.pose.position.z = 0;
	// Safety-Loop Defines
	batteryLandThreshold = 5;
	batteryGoHomeThreshold = 50;
	wayHomePtr = -1;
	lastSavedWayHomePoint.position.x = 0;
	lastSavedWayHomePoint.position.y = 0;
	lastSavedWayHomePoint.position.z = 0.1;
	wasGoingBack = false;
	start();
	return true;
}
// Alternative constructor for remote master and host
bool QNode::init(const std::string &master_url, const std::string &host_url) {
	std::map<std::string,std::string> remappings;
	remappings["__master"] = master_url;
	remappings["__hostname"] = host_url;
	ros::init(remappings,"drone_waypointer");
	if ( ! ros::master::check() ) {
		return false;
	}
	ros::start(); // explicitly needed since our nodehandle is going out of scope.
	ros::NodeHandle n;
	// Publishers
	pub_takeoff = n.advertise<std_msgs::Empty>("/ardrone/takeoff",1);
	pub_land = n.advertise<std_msgs::Empty>("/ardrone/land",1);
	pub_twist = n.advertise<geometry_msgs::Twist>("/cmd_vel",1);
	pub_reset = n.advertise<std_msgs::Empty>("ardrone/reset",1);

	// Subscribers
	sub_navData = n.subscribe("/ardrone/navdata" , 1 , &QNode::navDataCallback, this );
	sub_image_front = n.subscribe("ardrone/front/image_raw" ,1 , &QNode::frontImageCallback, this);
	sub_image_bottom = n.subscribe("ardrone/bottom/image_raw" ,1 , &QNode::bottomImageCallback, this);
	sub_real_pose = n.subscribe("/ground_truth/state" ,1 , &QNode::realPoseCallBack, this);
	sub_external_estimator = n.subscribe(estimatorTopic, 1, &QNode::estimatedPoseCallback, this);
	// Initial Conditions
	msg_twist = setupTwist(0,0,0,0,0,0);
	navDataRotZ = 0;
	navDataRotZ360 = 0;
	actionCode = 0;
	targetInMap.position.x = 0;
	targetInMap.position.y = 0;
	targetInMap.position.z = 0;
	targetInMap.orientation.x = 0;
	targetInMap.orientation.y = 0;
	targetInMap.orientation.z = 0;
	lastSavedWaypoint.position.x = 0;
	lastSavedWaypoint.position.y = 0;
	lastSavedWaypoint.position.z = 0;
	currentWaypointPtr = -1;
	currentSavedWaypointPtr = 0;
	angleAccuracy = 10;
	waypointAccuracy = 0.15;
	pointGain = 0.5;
	angleGain = 0.5;
	recordFlightPath = false;
	recordData = true;
	recordImages = true;
	lastDroneData.xRot = 0;
	lastDroneData.yRot = 0;
	lastDroneData.zRot = 0;
	firstTimeSamplingData = true;
	latched = false;
	lastDataSampleTime = ros::Time::now();
	samplingFrontCamera = false;
	poseEstimationMethod = 3;
	estimatedPoseDR.position.x = 0;
	estimatedPoseDR.position.y = 0;
	estimatedPoseDR.position.z = 0;
	externalEstimatedPose.pose.position.x = 0;
	externalEstimatedPose.pose.position.y = 0;
	externalEstimatedPose.pose.position.z = 0;
	// Safety-Loop Defines
	batteryLandThreshold = 5;
	batteryGoHomeThreshold = 50;
	wayHomePtr = -1;
	lastSavedWayHomePoint.position.x = 0;
	lastSavedWayHomePoint.position.y = 0;
	lastSavedWayHomePoint.position.z = 0.1;
	wasGoingBack = false;
	start();
	return true;
}

void QNode::run() {
	ros::Rate loop_rate(50); // maximum speed for looping
	ros::Duration latchTime(5.0);
	// ROS Loop
	while ( ros::ok() ) {
		// Decide Safety Action if Safety-Loops are enables
		if(safeFlight){
			decideSafetyAction();
		}
		// Reset the latch time
		if(actionCode == 0){
			latched = false;
		}
		// Take off
		else if (actionCode == 1){
			if(!latched){
				latchStartTime = ros::Time::now();
				latched = true;
			}
			if(ros::Time::now() < latchStartTime + latchTime){
				pub_takeoff.publish(emp_msg);
			}
			else{
				command(0,0,0,0,0,0);
				actionCode = 0;
			}
		}
		// Land
		else if(actionCode == 2){
			if(currentDroneData.z <= 0.5){
				if(!latched){
					latchStartTime = ros::Time::now();
					latched = true;
				}
				if(ros::Time::now() < latchStartTime + latchTime){
					pub_land.publish(emp_msg);
				}
				else{
					actionCode = 0;
				}
			}
			else{
				command(0,0,-1,0,0,0);
				actionCode = 2;
			}
		}
		// Reset
		else if(actionCode == 3){
				pub_reset.publish(emp_msg);
				actionCode = 0;
		}
		// Go to Waypoint
		else if(actionCode == 4){
			returnTargetInDrone(targetInMap);
			float xAct,yAct,zAct;
			float gain=0.3;
			xAct = (targetInDrone.position.x*gain);
			yAct = (targetInDrone.position.y*gain);
			zAct = (targetInDrone.position.z*gain);
			command(xAct,yAct,zAct,0,0,0);
		}
		// Look At Waypoint
		else if(actionCode == 5){
			returnTargetInDrone(targetInMap);
			float zRotAct; 
			float gain = 0.5; // Proportional Gain
			// Actuation Force
			zRotAct = targetInDrone.orientation.z*gain;
			command(0,0,0,0,0,zRotAct);
		}
		// Get Waypoint
		else if(actionCode == 6){
			returnTargetInDrone(targetInMap);
		}
		// Look and Go to wypoint
		else if(actionCode == 7){
			returnTargetInDrone(targetInMap);
			if(!wayPointReached(waypointAccuracy)){
				if(wayPointFaced(angleAccuracy)){
					float xAct,yAct,zAct,zRotAct;
					zRotAct = targetInDrone.orientation.z*angleGain;
					xAct = (targetInDrone.position.x*pointGain);
					yAct = (targetInDrone.position.y*pointGain);
					zAct = (targetInDrone.position.z*pointGain);
					command(xAct,yAct,zAct,0,0,zRotAct);
					printf("Going to  : X: %f  Y:%f  Z:%f \n",
							 realPose.pose.position.x, realPose.pose.position.y, realPose.pose.position.z);
				}
				else{
					float zRotAct;
					zRotAct = targetInDrone.orientation.z*angleGain;
					command(0,0,0,0,0,zRotAct);
				}
			}
			else{
				printf("Waypoint Reached \n");
				command(0,0,0,0,0,0);
				actionCode = 0;
			}
		}
		// Follow Flightpath
		else if(actionCode == 8){
			returnTargetInDrone(targetInMap);
			if(currentWaypointPtr > -1){
				// If Waypoint reached
				if(!wayPointReached(waypointAccuracy)){
					// If waypoint faced
					if(wayPointFaced(angleAccuracy)){
						float xAct,yAct,zAct,zRotAct;
						zRotAct = targetInDrone.orientation.z*angleGain;
						xAct = (targetInDrone.position.x*pointGain);
						yAct = (targetInDrone.position.y*pointGain);
						zAct = (targetInDrone.position.z*pointGain);
						command(xAct,yAct,zAct,0,0,zRotAct);
					}
					else{
						float zRotAct;
						zRotAct = targetInDrone.orientation.z*angleGain;
						command(0,0,0,0,0,zRotAct);
					}
				}
				else{
					printf("Waypoint [%d] Reached : X: %f  Y:%f  Z:%f \n", currentWaypointPtr,
								 targetInMap.position.x, targetInMap.position.y, targetInMap.position.z);
					command(0,0,0,0,0,0);
					Q_EMIT requestNewWaypoint();
				}
			}
			else{
				command(0,0,0,0,0,0);
				Q_EMIT requestNewWaypoint();
			}
		}
		// Go Home
		else if(actionCode == 9){
			returnTargetInDrone(targetInMap);
			if(!wayPointReached(waypointAccuracy)){
				if(wayPointFaced(angleAccuracy)){
					float xAct,yAct,zAct,zRotAct;
					zRotAct = targetInDrone.orientation.z*angleGain;
					xAct = (targetInDrone.position.x*pointGain);
					yAct = (targetInDrone.position.y*pointGain);
					zAct = (targetInDrone.position.z*pointGain);
					command(xAct,yAct,zAct,0,0,zRotAct);
				}
				else{
					float zRotAct;
					zRotAct = targetInDrone.orientation.z*angleGain;
					command(0,0,0,0,0,zRotAct);
				}
			}
			// Waypoint Reached
			else{
				if(wayHomePtr - 1 >= 0){
					printf("Waypoint [%d] Reached : X: %f  Y:%f  Z:%f \n", wayHomePtr,
							 targetInMap.position.x, targetInMap.position.y, targetInMap.position.z);
					wayHomePtr--;
					command(0,0,0,0,0,0);
				}
				else{
					// Last waypoint in the WayHome.txt file reached
					printf("Home Sweet Home! \n");
					actionCode = 2; // Land
					command(0,0,0,0,0,0);
				}

			}
		}
		pub_twist.publish(msg_twist);
		// Save Waypoint if recording is enabled
		if(recordFlightPath){
			saveFlightPath();
		}
		if(recordData){
			sampleData();
		} // Sample Data
		if(recordImages){
			sampleImage();
		} // Sample Image
		ros::spinOnce();
		loop_rate.sleep();
	}// ros::ok()
	std::cout << "Ros shutdown, proceeding to close the gui." << std::endl;
	Q_EMIT rosShutdown(); // used to signal the gui for a shutdown (useful to roslaunch)
}// QNode::run()

// NavData readings
void QNode::navDataCallback(const ardrone_autonomy::Navdata& nav_msg){
	currentDroneData.timeStamp = nav_msg.header.stamp;
	droneState = nav_msg.state;
	battery = nav_msg.batteryPercent;
	navDataRotZ =  nav_msg.rotZ;

	if (nav_msg.rotZ < 0){
		navDataRotZ360 = nav_msg.rotZ + 360;
	}
	else{
		navDataRotZ360 = nav_msg.rotZ;
	}

	// Linear Velocities
	currentDroneData.xVel = nav_msg.vx/1000; // [m/sec]
	currentDroneData.yVel = nav_msg.vy/1000; // [m/sec]
	currentDroneData.zVel = nav_msg.vz/1000; // [m/sec]

	// Linear Accelerations
	currentDroneData.xAcc = nav_msg.ax*9.81; // [m/s^2]
	currentDroneData.yAcc = nav_msg.ay*9.81; // [m/s^2]
	currentDroneData.zAcc = nav_msg.az*9.81; // [m/s^2]

	// Angular Rotations
	currentDroneData.xRot = nav_msg.rotX; // Degrees
	currentDroneData.yRot = nav_msg.rotY; // Degrees
	currentDroneData.zRot = nav_msg.rotZ; // Degrees

	// Angular Velocities
	if(!firstTimeSamplingData){
		std::cout << "currentDroneData "<< currentDroneData.timeStamp  << std::endl;
		std::cout << "lastDroneData "<< lastDroneData.timeStamp  << std::endl;

					
		double dt = (currentDroneData.timeStamp - lastDroneData.timeStamp).toSec();
		currentDroneData.xRotVel = (currentDroneData.xRot - lastDroneData.xRot)/dt; // Degrees/Sec
		currentDroneData.yRotVel = (currentDroneData.yRot - lastDroneData.yRot)/dt; // Degrees/sec
		currentDroneData.zRotVel = (currentDroneData.zRot - lastDroneData.zRot)/dt; // Degrees/sec

		if(poseEstimationMethod == 1){
			currentDroneData.x = realPose.pose.position.x; // meters [m]
			currentDroneData.y = realPose.pose.position.y; // meters [m]
			currentDroneData.z = realPose.pose.position.z; // meters [m]
		}
		else if(poseEstimationMethod == 2){
			currentDroneData.x = externalEstimatedPose.pose.position.x; // meters [m]
			currentDroneData.y = externalEstimatedPose.pose.position.y; // meters [m]
			currentDroneData.z = externalEstimatedPose.pose.position.z; // meters [m]
		}
		else if(poseEstimationMethod == 3){
			estimatePoseDeadReckoning();
			currentDroneData.x = estimatedPoseDR.position.x; // m
			currentDroneData.y = estimatedPoseDR.position.y; // m
			currentDroneData.z = estimatedPoseDR.position.z; // m
		}
	}
	/*
	// Motor PWM values (not available in tum_simulator)
	currentDroneData.motor1 = nav_msg.motor1;
	currentDroneData.motor2 = nav_msg.motor2;
	currentDroneData.motor3 = nav_msg.motor3;
	currentDroneData.motor4 = nav_msg.motor4;
	*/
	firstTimeSamplingData = false;
	lastDroneData = currentDroneData;
	Q_EMIT dataUpdated();
}

// Read front Image Data
void QNode::frontImageCallback(const sensor_msgs::ImageConstPtr& front_image_msg){
	    try
	    {
	      CV_bottom_image_ptr = cv_bridge::toCvCopy(front_image_msg, enc::BGR8);
	    }
	    catch (cv_bridge::Exception& e)
	    {
	      ROS_ERROR("cv_bridge exception: %s", e.what());
	      return;
	    }

	    Q_EMIT imageUpdated();
}

// Read Bottom Image Data
void QNode::bottomImageCallback(const sensor_msgs::ImageConstPtr& bottom_image_msg){
	    try
	    {
	      CV_bottom_image_ptr = cv_bridge::toCvCopy(bottom_image_msg, enc::BGR8);
	    }
	    catch (cv_bridge::Exception& e)
	    {
	      ROS_ERROR("cv_bridge exception: %s", e.what());
	      return;
	    }

	    Q_EMIT imageUpdated();
}


// Real Position of the Drone (from simulated Data)
void QNode::realPoseCallBack(const nav_msgs::Odometry& realPoseData){
	realPose = realPoseData.pose;

	Q_EMIT realPoseUpdated();

}
// Recieve the estimated Pose from an external node
void QNode::estimatedPoseCallback(const nav_msgs::Odometry& pose_msg){
	externalEstimatedPose = pose_msg.pose;

	Q_EMIT externalEstimatedPoseUpdated();
}

// Estimate the Pose internaly using Dead Reckoning
void QNode::estimatePoseDeadReckoning(){
	float zRot = navDataRotZ360*M_PI/180;
	float dt = (currentDroneData.timeStamp - lastDroneData.timeStamp).toSec();
	float xd1 = estimatedPoseDR.position.x;
	float xd2 = currentDroneData.xVel*dt;
	float yd1 = estimatedPoseDR.position.y;
	float yd2 = currentDroneData.yVel*dt;

	estimatedPoseDR.position.x = xd1 + (cos(zRot)*(xd2) - sin(zRot)*(yd2));
	estimatedPoseDR.position.y = yd1 + (sin(zRot)*(xd2) + cos(zRot)*(yd2));
	estimatedPoseDR.position.z = estimatedPoseDR.position.z + currentDroneData.zVel*dt;	// m

	Q_EMIT estimatedPoseUpdated();
}
// Convert the Co-ordinates of the target in the Drone Frame
void QNode::returnTargetInDrone(geometry_msgs::Pose target){
	// XYZ co-ordinates of the target and the drone
	float xd,xt,yd,yt,zd,zt;
	//geometry_msgs::Pose target2;
	// Degrees to rads
	float zRot = -navDataRotZ360*M_PI/180;

	// Target XYZ to the Map frame
	xt = target.position.x;
	yt = target.position.y;
	zt = target.position.z;
	xd = currentDroneData.x;
	yd = currentDroneData.y;
	zd = currentDroneData.z;

	// Translation of position
	targetInDrone.position.x = cos(zRot)*(xt - xd) - sin(zRot)*(yt - yd);
	targetInDrone.position.y = sin(zRot)*(xt - xd) + cos(zRot)*(yt - yd);
	targetInDrone.position.z = zt - zd;
	targetInDrone.orientation.x = 0;
	targetInDrone.orientation.y = 0;

	// Angle from the Drone X-axis (Roll axis) to the point vector in the drone frame
	if(targetInDrone.position.x != 0){
		// atan2() returns a value in all 4 quadrants given the x,y vectors 
		targetInDrone.orientation.z = atan2(targetInDrone.position.y, targetInDrone.position.x);
	}
	// Precaution not to devide by zero
	else
	{
		if(targetInDrone.position.y > 0)
		{
			targetInDrone.orientation.z = M_PI/2;
		}
		else if(targetInDrone.position.y < 0)
		{
			targetInDrone.orientation.z = -M_PI/2;
		}
	}
	
	Q_EMIT targetUpdated();
}

// Determine if the waypoint has been reached with a tolerance level
bool QNode::wayPointReached(float tolerance){
	if(qAbs(targetInDrone.position.x) < tolerance)
	{
		if(qAbs(targetInDrone.position.y) < tolerance)
		{
			if(qAbs(targetInDrone.position.z) < tolerance)
			{
				return true;
			}
		}
	}
	return false;
}

// Determine if the waypoint is being faced with a tolerance level
bool QNode::wayPointFaced(float tolerance){
	if(qAbs(targetInDrone.orientation.z) < tolerance)
	{
		return true;
	}
	return false;
}

// Function to generate Twist messages
geometry_msgs::Twist QNode::setupTwist(float xv, float yv, float zv, float xr, float yr, float zr){
	geometry_msgs::Twist msg;
	
	msg.linear.x=xv;
	msg.linear.y=yv;
	msg.linear.z=zv;
	msg.angular.x=xr;
	msg.angular.y=yr;
	msg.angular.z=zr;

	return msg;
}

// Function to generate twist commands
void QNode::command(float xv, float yv, float zv, float xr, float yr, float zr){
	msg_twist = setupTwist(xv, yv, zv, xr, yr, zr);
}
// Sampling Flightpath
void QNode::saveFlightPath(){
	ros::Time nowTime = ros::Time::now();
	ros::Duration samplingTime(0.5);
	if(currentSavedWaypointPtr == 0){
		lastFlightpathSampleTime = ros::Time::now();
		currentSavedWaypointPtr ++;
		Q_EMIT sampleFlightpath();
	}
	else if(lastFlightpathSampleTime <= nowTime - samplingTime){
			currentSavedWaypointPtr++;
			lastFlightpathSampleTime = ros::Time::now();
			Q_EMIT sampleFlightpath();
	}
}

// Function called to sample data
void QNode::sampleData(){
	ros::Time nowTime = ros::Time::now();
	ros::Duration samplingTime(0.02);
	if(!firstTimeSamplingData){
		if(lastDataSampleTime <= nowTime - samplingTime)
		{
			lastDataSampleTime = ros::Time::now();
			Q_EMIT dataReady();
		}
	}
}

// Funcation called to sample image
void QNode::sampleImage(){
	ros::Time nowTime = ros::Time::now();
	ros::Duration samplingTime(imageSamplingTime);
	if(!firstTimeSamplingData){
		if(lastImageSampleTime <= nowTime - samplingTime)
		{
			lastImageSampleTime = ros::Time::now();
			samplingFrontCamera = !samplingFrontCamera;
			Q_EMIT imageReady();
		}
	}
}
// Decide on what safety action to follow
void QNode::decideSafetyAction(){
	// Emergency Land
	if(battery <= batteryLandThreshold || testBatteryBellowLand){
		actionCode = 2;
	}
	else{
		if(battery <= batteryGoHomeThreshold || testBatteryBellowGoHome){
			wasGoingBack = true;
			Q_EMIT goHome();
		}
		else if(noWifi || testNoWifi){
			wasGoingBack = true;
			Q_EMIT goHome();
		}
		else{
			if(wasGoingBack){
				wasGoingBack = false;
				actionCode = 0;
				command(0,0,0,0,0,0);
				Q_EMIT updateWayHomeFinalPoint();
			}
			if(qAbs(currentDroneData.x - lastSavedWayHomePoint.position.x) >= 0.5 ||
				qAbs(currentDroneData.y - lastSavedWayHomePoint.position.y) >= 0.5 ||
				qAbs(currentDroneData.z - lastSavedWayHomePoint.position.z) >= 0.5){
				if(wayHomePtr >= 0){
					lastSavedWayHomePoint.position.x = currentDroneData.x;
					lastSavedWayHomePoint.position.y = currentDroneData.y;
					lastSavedWayHomePoint.position.z = currentDroneData.z;
				}
				else{
					lastSavedWayHomePoint.position.x = 0;
					lastSavedWayHomePoint.position.y = 0;
					lastSavedWayHomePoint.position.z = 0.2;
				}
				Q_EMIT sampleWayHome();
			}
		}
	}

}
}  // namespace drone_waypointer
