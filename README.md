[![Build Status](http://90.211.148.158:8080/buildStatus/icon?job=testing)](http://94.2.115.49:8080/job/testing/)
![HitCount](https://img.shields.io/badge/ROS%20version-kinetic-blue.svg)
![HitCount](https://img.shields.io/badge/Supported%20OS-Ubuntu%2016.04-orange.svg)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)
[![HitCount](http://hits.dwyl.io/20chix/https://github.com/20chix/FYP_Autonomus_Drone_DWM1001.svg)](http://hits.dwyl.io/20chix/https://github.com/20chix/FYP_Autonomus_Drone_DWM1001)

# Abstract

The aim of my final year project consists in a development of a system that involve the use of a drone that would have to fly indoor autonomously, around waypoints(anchors) based on the shortest path calculated and stream all the information via network to a ground station. Without any human interaction.

In order to make the drone fly autonomously I’ll need some hardware to start with. For example, in order to get all the coordinates of all the anchors I’ll need few dev-boards provided by Decawave called dwm1001. These dev-boards can be used as anchors or as a tag. A tag is the master dev-board, is the one that we will use to receive all the coordinates and distances from all the anchors. We will then pass these coordinates and distances to the raspberry pi via UART or SPI. The raspberry pi will then filter all these coordinates and pass it into ROS (Robot Operating System)

# 4 DWM1001, 3 anchors and 1 tag
 The tag will be attached to a drone and  3 anchors will be placed on the ground, which will create a triangle.
 The goal is to make the ARDrone follow each anchor and one imaginary anchor which will be placed across coordinates 0,0.

# Top Level 
![alt text](https://github.com/20chix/FYP_Autonomus_Drone_DWM1001/blob/master/resources/FYP_Diagram.png?raw=true)

![alt text](https://github.com/20chix/FYP_Autonomus_Drone_DWM1001/blob/master/resources/decawave-dwm1001-dev-large.jpg?raw=true)

# Packages
## localizer_dwm1001
This package is responsible on getting the network coordinates (tag and anchors) from dwm1001 dev board via USB.
![alt text](https://github.com/20chix/FYP_Autonomus_Drone_DWM1001/blob/master/resources/FYP_Diagram_dev_board.png?raw=true)

## shortest_path 
This package is responsible for calculating the shortest, using a* algorithm, from the tag to a anchor at the time, this package will publish a string of directions for example 777788888844444442222222111111. We will use these directions to control the drone.

![alt text](https://github.com/20chix/FYP_Autonomus_Drone_DWM1001/blob/master/resources/Shortest_Path.png?raw=true)

## Dynamic reconfigure DWM1001
In this package we want to be able to change some variable from ground station, while the drone is flying.

![alt text](https://github.com/20chix/FYP_Autonomus_Drone_DWM1001/blob/master/resources/dynamic_config.png?raw=true)

## DWM1001 Network example with RVIZ
In this package we visualize the DWM1001 network coordinates in RVIZ, using simple marker tutorial. 

![alt text](https://github.com/20chix/FYP_Autonomus_Drone_DWM1001/blob/master/resources/Screenshot%20from%202018-10-07%2013-31-00.png?raw=true)


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
