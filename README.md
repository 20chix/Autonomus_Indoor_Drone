# Autonomus indoor drone

[![Build Status](http://http://90.198.211.77:8080/buildStatus/icon?job=testing)](http://94.2.115.49:8080/job/testing/)
![HitCount](https://img.shields.io/badge/ROS%20version-kinetic-blue.svg)
![HitCount](https://img.shields.io/badge/Supported%20OS-Ubuntu%2016.04-orange.svg)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)
[![HitCount](http://hits.dwyl.io/20chix/https://github.com/20chix/FYP_Autonomus_Drone_DWM1001.svg)](http://hits.dwyl.io/20chix/https://github.com/20chix/FYP_Autonomus_Drone_DWM1001)

## Intro

The aim of this project is to provide a solution for autonomous indoor drone (AID). AID involves localization, control, path planning and autonomous landing/take-off. A robust localization method was used, using GPS-like device called DWM1001 provided by Decawave . This device is especially useful for indoor applications as it a has a high accuracy and can only be used in confined spaces.

### Simulation results in Gazebo

For the Gazebo simulation I have used mavros and iris drone. The drone is following waypoints that have been defined in this [xml file](https://github.com/20chix/Autonomus_Indoor_Drone/blob/master/fyp/src/waypoints/waypoints.xml). For simulation purpose I only have 4 waypoints that are placed in a square shape. 
A GUI provided by dynamic reconfigure RQT (bottom left) is provided for debugging purpose. I might keep it in the future, don't know yet.

![alt text](https://github.com/20chix/Autonomus_Indoor_Drone/blob/master/resources/mavros_followFlightPath.gif)

### Installation

This project currently works for **Kinetic**.

### Install ROS Kinetic

Install ROS from this link into your PC http://wiki.ros.org/kinetic/Installation/Ubuntu and all the dependencies 

**NOTE:** if you install kinetic you need have ubuntu 16.04, if you want to install the latest ROS which is Meldic then you need to have uybuntu 18.04.

### Create a ROS workspace

Follow this short tutorial to create a ROS workspace http://wiki.ros.org/catkin/Tutorials/create_a_workspace

### Download current GitHub project

Navigate to your workspace ``` ~/catkin_ws/``` and run:

```

#!/bin/bash
git clone https://github.com/20chix/Autonomus_Indoor_Drone.git
```

Delete the src folder when you created the workspace and rename Autonomus_Indoor_Drone to src

### Build the workspace

Navigate to your workspace ``` ~/catkin_ws/```  and run:

```

#!/bin/bash
catkin_make
```

### Download ardupilot_gazebo

In my repo you can see ardupilot_gazebo, this is cloned from [here](https://github.com/khancyr/ardupilot_gazebo). Clone the repo and follow the installation instructions. If you installed everything correctly, run this command.

```

#!/bin/bash
gazebo --verbose ~/catkin_ws/src/ardupilot_gazebo/worlds/iris_ardupilot.world
```

You will see gazebo with an IRIS drone in a runway.

### Download MAVROS

Follow [this link](https://ardupilot.org/dev/docs/ros-install.html#installing-mavros) to install MAVROS.

### Download Ardupilot

Clone Ardupilot from [this link](https://github.com/ArduPilot/ardupilot).
Once installed run the following command in a separate terminal tab

```

#!/bin/bash
<PATH_TO_YOUR_ARDUPILOT>/ardupilot/Tools/autotest/sim_vehicle.py --map --console  -v ArduCopter -f gazebo-iris
```

### Run MAVROS
Now run ardupilotMavros launch file so we can link IRIS drone in gazebo to ROS. Run the following command to do so in a new terminal tab.

```

#!/bin/bash
roslaunch ardupilotMavros apm.launch
```

*Remeber to source into your workspace

### Run fyp for autonomus flight

Now run fyp, this package have few features, most of them are for debugging purpose. The main one is follow waypoint from xml file and follow waypoint from DWM1001 waypoint(not simulated).

To control the drone from this package run from a new terminal tab

```

#!/bin/bash
rosrun fyp aid_main.py
```

A message should come up saying "Waiting for a command"

*Remeber to source into your workspace


### Run ROS dynamic reconfigure
In order to manage the drone I linked most of the functionality to RQT reconfigure 
```

#!/bin/bash
rosrun rqt_reconfigure rqt_reconfigure
```

You should see this:

![alt text](https://github.com/20chix/Autonomus_Indoor_Drone/blob/master/resources/rqt.png)

- Press takeoff to takeoff the IRIS drone
- Press followFlightPathWaypoints in order to start an autonomus flight

Other buttons works, but there is still some bugs in the code. Feel free to contribute however you want to.

## Hardware

Coming soon...

### DWM1001 network Rviz visualization

We have created an interface between DWM1001 and ROS, which allowed us to visualize all the waypoints from Rviz.

![alt text](https://github.com/20chix/FYP_Autonomus_Drone_DWM1001/blob/master/resources/DWMNetwor_with_description.png?raw=true)

## DWM1001 dev-boards used as waypoints

In this project we used 4 of those as anchor(waypoint) and one as the master(tag), which will be attached into the drone 

![alt text](https://github.com/20chix/FYP_Autonomus_Drone_DWM1001/blob/master/resources/decawave-dwm1001-dev-large.jpg?raw=true)

### Packages

**`localizer_dwm1001`** This package is responsible on getting the network coordinates (tag and anchors) from dwm1001 dev board via USB, and pubblish in coordinates in topics.

**`fyp`** This package is responsible on controlling the drone, reading waypoints from xml file, process joystick input, land and takeoff the drone.

**`ardrone_simulator`** This package is responsible on simulating the ardrone on gazebo7.

**`joy`** This package is responsible on interfacing joystick.

**`generate_map`** This package is responsible on creating markers in Rviz.


Other packages were made for testing(I will remove them once I get a working prototype on the real drone)


## Dynamic reconfigure of DWM1001
In this package we want to be able to change some variable from ground station, while the drone is flying.

![alt text](https://github.com/20chix/FYP_Autonomus_Drone_DWM1001/blob/master/resources/dynamic_config.png?raw=true)



## ROS Topic monitor
![alt text](https://github.com/20chix/FYP_Autonomus_Drone_DWM1001/blob/master/resources/Screenshot%20from%202018-10-07%2014-02-37.png?raw=true)




### Roadmap
- [x] Create RTLS network from Android App
- [x] Access DWM1001 API via UART
- [x] Get Anchor coordinates in Python
- [x] Get Tag position in Python
- [x] Display Anchors in RViz
- [x] Display Tag in RViz
- [x] Calculate shortest path from Tag to a Anchor using A* Algorithm
- [x] Display shortest path in RViz
- [x] Display actual path in RViz
- [x] Dynamic configuration for DWM1001 dev board
- [x] Dynamic configuration for drone
- [x] Joystick controls for emergency takeoff and land
- [ ] Setup continuos integration for simulation
- [ ] Neural Network/AI that will manage flight controller after couple of laps
- [ ] Statistics for each lap
- [ ] Statistics for Neural Network/AI
- [ ] BOM for hardware components
- [ ] Get all hardware components
- [ ] Document or video wiring 
- [ ] First test flight
- [ ] Rework from test flight
- [ ] Setup continuos integration for hardware
- [ ] Cloud statics for continuos improvment





