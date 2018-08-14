[![Build Status](http://94.2.115.49:8080/buildStatus/icon?job=testing)](http://94.2.115.49:8080/job/testing/)
![HitCount](https://img.shields.io/badge/ROS%20version-kinetic-blue.svg)
![HitCount](https://img.shields.io/badge/Supported%20OS-Ubuntu%2016.04-orange.svg)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)
[![HitCount](http://hits.dwyl.io/20chix/https://github.com/20chix/FYP_Autonomus_Drone_DWM1001.svg)](http://hits.dwyl.io/20chix/https://github.com/20chix/FYP_Autonomus_Drone_DWM1001)

# FYP_Autonomus_Drone_DWM1001

Final year project that consist in autonomus drone, developed in ROS using UWB DWM1001 dev board

# We have 4 DWM1001 3 anchors and 1 tag
 The tag will be attached to a drone and  3 anchors will be placed on the ground, which will create a triangle.
 The goal is to make the ARDrone follow each anchor and one imaginary anchor which will be placed across coordinates 0,0.

# Abstract 
![alt text](https://raw.githubusercontent.com/20chix/FYP_Autonomus_Drone_DWM1001/master/FYP_Diagram.png?token=AO45C05pXrDjVLWjscxHtIeme5V2u6LIks5bdegywA%3D%3D)

## Dynamic reconfigure DWM1001
In this package we want to be able to change some variable from ground station, while the drone is flying.

![alt text](https://raw.githubusercontent.com/20chix/FYP_Autonomus_Drone_DWM1001/master/dynamic_config.png?token=AO45C_U_21l0DxnwtksrGWyNPu9QgesEks5bezMowA%3D%3D)

## DWM1001 Network example with RVIZ
In this package we visualize the DWM1001 network coordinates in RVIZ, using simple marker tutorial. 

![alt text](https://raw.githubusercontent.com/20chix/FYP_Autonomus_Drone_DWM1001/master/DWM1001_Network.png?token=AO45CyLgBJfEUZWnWtPbS663cFn77bhjks5bfHnDwA%3D%3D)


### Roadmap
- [x] Create RTLS network from Android App
- [x] Access DWM1001 API via UART
- [x] Get Anchor coordinates in Python
- [x] Get Tag position in Python
- [x] Display Anchors in RViz
- [x] Display Tag in RViz
- [ ] Calculate shortest path from Tag to a Anchor using A* Algorithm
- [ ] Display shortest path in RViz
- [ ] Display actual path in RViz
- [x] Dynamic configuration for DWM1001 dev board
- [ ] Dynamic configuration for drone
- [ ] Joystick controls for emergency takeoff and land
- [ ] Neural Network/AI that will manage flight controller after couple of laps
- [ ] Statistics for each lap
- [ ] Statistics for Neural Network/AI
