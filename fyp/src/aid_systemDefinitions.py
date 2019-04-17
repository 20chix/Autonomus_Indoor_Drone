#!/usr/bin/env python

__author__     = "Hadi Elmekawi"
__version__    = "1.0"
__maintainer__ = "Hadi Elmekawi"
__email__      = "w1530819@my.westminster.ac.uk"
__status__     = "Development"


class SYS_DEFS:

    AUTHOR          = "Hadi Elmekawi"
    VERSION         = "1.0"
    MAINTAINER      = "Hadi Elmekawi"
    EMAIL           = "w1530819@my.westminster.ac.uk"
    STATUS          = "Development"

    # Action states
    RESET_LATCH_TIME_ACTION_STATE                = 0
    TAKE_OFF_ACTION_STATE                        = 1
    LAND_ACTION_STATE                            = 2
    RESET_DRONE_ACTION_STATE                     = 3
    GO_TO_WAYPOINT_WITHOUT_LOOKING_ACTION_STATE  = 4
    LOOK_AT_WAYPOINT_ACTION_STATE                = 5
    LOOK_AND_GO_TO_WAYPOINT_ACTION_STATE         = 7
    FOLLOW_FLIGHT_PATH_WAYPOINTS_ACTION_STATE    = 8
    FOLLOW_FLIGHT_PATH_DWM1001_ACTION_STATE      = 9

    POINT_GAIN                      = 0.5
    ANGLE_GAIN                      = 0.5
    ANGLE_ACCURACY                  = 10
    WAYPOINT_ACCURACY               = 0.50
    LINEAR_ACCELLERATION_M_PER_SEC  = 9.81
    LINEAR_VELOCITY_KPS             = 1000


    # define the default mapping between joystick buttons and their corresponding actions
    BUTTON_EMERGENCY                    = 7
    BUTTON_LOAD_DWM1001                 = 6
    BUTTON_LAND                         = 1
    BUTTON_TAKEOFF                      = 0
    BUTTON_HOVER                        = 4
    BUTTON_FOLLOW_FLIGHT_PATH_DWM1001   = 10
    BUTTON_FOLLOW_FLIGHT_PATH_XML       = 11

    # define the default mapping between joystick axes and their corresponding directions
    AXIX_ROLL                   = 0
    AXIS_PITCH                  = 1
    AXIS_YAW                    = 2
    AXIS_Z                      = 3

    # define the default scaling to apply to the axis inputs. useful where an axis is inverted
    SCALE_ROLL                  = 1.0
    SCALE_PITCH                 = 1.0
    SCALE_YAW                   = 1.0
    SCALE_Z                     = 1.0



    INDEX_0     = 0
    INDEX_1     = 1
    INDEX_2     = 2
    INDEX_3     = 3
    INDEX_4     = 4
    INDEX_5     = 5
    INDEX_6     = 6
    INDEX_7     = 7
    INDEX_8     = 8
    INDEX_9     = 9
    INDEX_10    = 10
    INDEX_11    = 11
    INDEX_12    = 12
    INDEX_13    = 13
    INDEX_14    = 14
    INDEX_15    = 15
    INDEX_16    = 16
    INDEX_17    = 17
    INDEX_18    = 18
    INDEX_19    = 19
    INDEX_20    = 20
    INDEX_21    = 21
    INDEX_22    = 22
    INDEX_23    = 23
    INDEX_24    = 24
    INDEX_25    = 25
    INDEX_26    = 26
    INDEX_27    = 27
    INDEX_28    = 28
    INDEX_29    = 29
    INDEX_30    = 30
    INDEX_31    = 31
    INDEX_32    = 32
    INDEX_33    = 33
    INDEX_34    = 34
    INDEX_35    = 35
    INDEX_36    = 36
    INDEX_37    = 37
    INDEX_38    = 38
    INDEX_39    = 39
    INDEX_40    = 40

