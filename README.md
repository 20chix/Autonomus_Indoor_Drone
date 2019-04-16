[![Build Status](http://http://90.198.211.77:8080/buildStatus/icon?job=testing)](http://94.2.115.49:8080/job/testing/)
![HitCount](https://img.shields.io/badge/ROS%20version-kinetic-blue.svg)
![HitCount](https://img.shields.io/badge/Supported%20OS-Ubuntu%2016.04-orange.svg)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)
[![HitCount](http://hits.dwyl.io/20chix/https://github.com/20chix/FYP_Autonomus_Drone_DWM1001.svg)](http://hits.dwyl.io/20chix/https://github.com/20chix/FYP_Autonomus_Drone_DWM1001)

# Abstract 

The aim of this project is to provide a solution for autonomous indoor drone (AID). AID involves localization, control, path planning and autonomous landing/take-off. A robust localization method was used, using GPS-like device called DWM1001 provided by Decawave . This device is especially useful for indoor applications as it a has a high accuracy and can only be used in confined spaces.

### Aim

![alt text](https://github.com/20chix/FYP_Autonomus_Drone_DWM1001/blob/master/resources/FYP_Diagram.png?raw=true)


### Prototype in Gazebo 7

![](resources/AID_working_prototype.gif)

### Rviz visualization of DWM1001 network 

![alt text](https://github.com/20chix/FYP_Autonomus_Drone_DWM1001/blob/master/resources/DWMNetwor_with_description.png?raw=true)

## DWM1001 dev-boards

![alt text](https://github.com/20chix/FYP_Autonomus_Drone_DWM1001/blob/master/resources/decawave-dwm1001-dev-large.jpg?raw=true)

# Packages
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
- [ ] Display actual path in RViz
- [x] Dynamic configuration for DWM1001 dev board
- [ ] Dynamic configuration for drone
- [ ] Joystick controls for emergency takeoff and land
- [ ] Neural Network/AI that will manage flight controller after couple of laps
- [ ] Statistics for each lap
- [ ] Statistics for Neural Network/AI
