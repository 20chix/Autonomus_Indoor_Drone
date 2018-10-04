[![Build Status](http://94.2.115.49:8080/buildStatus/icon?job=testing)](http://94.2.115.49:8080/job/testing/)
![HitCount](https://img.shields.io/badge/ROS%20version-kinetic-blue.svg)
![HitCount](https://img.shields.io/badge/Supported%20OS-Ubuntu%2016.04-orange.svg)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)
[![HitCount](http://hits.dwyl.io/20chix/https://github.com/20chix/FYP_Autonomus_Drone_DWM1001.svg)](http://hits.dwyl.io/20chix/https://github.com/20chix/FYP_Autonomus_Drone_DWM1001)

# FYP_Autonomus_Drone_DWM1001_

Final year project that consist in autonomus drone, developed in ROS using UWB DWM1001 dev board

# 4 DWM1001, 3 anchors and 1 tag
 The tag will be attached to a drone and  3 anchors will be placed on the ground, which will create a triangle.
 The goal is to make the ARDrone follow each anchor and one imaginary anchor which will be placed across coordinates 0,0.

# Abstract 
![alt text](https://raw.githubusercontent.com/20chix/FYP_Autonomus_Drone_DWM1001/master/resources/FYP_Diagram.png?token=AO45C53xUIdrgVjp64R74f0K0lF9WtFIks5bsiPcwA%3D%3D)

![alt text](https://raw.githubusercontent.com/20chix/FYP_Autonomus_Drone_DWM1001/master/resources/decawave-dwm1001-dev-large.jpg?token=AO45C-eb6jv3Io3O_k6rf_wopKmkcU8jks5bsiQXwA%3D%3D)

# Packages
## localizer_dwm1001
This package is responsible on getting the network coordinates (tag and anchors) from dwm1001 dev board via USB.
![alt text](https://raw.githubusercontent.com/20chix/FYP_Autonomus_Drone_DWM1001/master/resources/FYP_Diagram_dev_board.png?token=AO45C6bm2Ham34bclDihkppyqwFIukuhks5bsiQzwA%3D%3D)

## shortest_path 
This package is responsible for calculating the shortest, using a* algorithm, from the tag to a anchor at the time, this package will publish a string of directions for example 777788888844444442222222111111. We will use these directions to control the drone.
![alt text](https://raw.githubusercontent.com/20chix/FYP_Autonomus_Drone_DWM1001/master/resources/Shortest_Path.png?token=AO45CwmqAOcbhsyQRIiNdp5qELCVVlyXks5bsiP5wA%3D%3D)

## Dynamic reconfigure DWM1001
In this package we want to be able to change some variable from ground station, while the drone is flying.

![alt text](https://raw.githubusercontent.com/20chix/FYP_Autonomus_Drone_DWM1001/master/resources/dynamic_config.png?token=AO45C0Uc6dBqRbTVSQo2o4rBIJkaLMGQks5blvCMwA%3D%3D)

## DWM1001 Network example with RVIZ
In this package we visualize the DWM1001 network coordinates in RVIZ, using simple marker tutorial. 

![alt text](https://raw.githubusercontent.com/20chix/FYP_Autonomus_Drone_DWM1001/master/resources/DWM1001_Network.png?token=AO45C4GEr4m26mhZ1Sk-E_s61FVpOPYCks5bsiPBwA%3D%3D)


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
