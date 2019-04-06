#!/usr/bin/env python
""" For more info on the documentation go to https://www.decawave.com/sites/default/files/dwm1001-api-guide.pdf
"""

from dwm1001_systemDefinitions import SYS_DEFS


__author__     = SYS_DEFS.AUTHOR
__version__    = SYS_DEFS.VERSION
__maintainer__ = SYS_DEFS.MAINTAINER
__email__      = SYS_DEFS.EMAIL
__status__     = SYS_DEFS.STATUS


import rospy
from localizer_dwm1001.msg                          import Anchor
from localizer_dwm1001.msg                          import Tag
from localizer_dwm1001.srv      import Anchor_0
from localizer_dwm1001.srv      import Tag_srv
from localizer_dwm1001.srv      import Anchor_1
from localizer_dwm1001.srv      import Anchor_2
from localizer_dwm1001.srv      import Anchor_3
from std_srvs.srv import Trigger, TriggerResponse

anchor_0 = Anchor()
anchor_1 = Anchor()
anchor_2 = Anchor()
anchor_3 = Anchor()
tag      = Tag()


def triggerResponseAnchor0(request):
    """
    Service that will provide data for anchor 0

    :param data:  containing request from user

    :return service response, which anchor data

    """     
    return (anchor_0.x, anchor_0.y, anchor_0.z)

def triggerResponseAnchor1(request):
    """
    Service that will provide data for anchor 1

    :param data:  containing request from user

    :return service response, which anchor data

    """     
    return (anchor_1.x, anchor_1.y, anchor_1.z)

def triggerResponseAnchor2(request):
    """
    Service that will provide data for anchor 2

    :param data:  containing request from user

    :return service response, which anchor data

    """       
    return (anchor_2.x, anchor_2.y, anchor_2.z)

def triggerResponseAnchor3(request):
    """
    Service that will provide data for anchor 3

    :param data:  containing request from user

    :return service response, which anchor data

    """        
    return (anchor_3.x, anchor_3.y, anchor_3.z)

def triggerResponseTag(request):
    """
    Service that will provide data for tag

    :param data:  containing request from user

    :return service response, which tag data

    """    
    return (tag.x, tag.y, tag.z)




def Anchor0callback(data):
    """
    Callback for anchor 0

    :param data:  containing tag object

    """    
    global anchor_0
    anchor_0 = data

def Anchor1callback(data):
    """
    Callback for anchor 1

    :param data:  containing tag object

    """
    global anchor_1
    anchor_1 = data

def Anchor2callback(data):
    """
    Callback for anchor 2

    :param data:  containing tag object

    """
    global anchor_2
    anchor_2 = data

def Anchor3callback(data):
    """
    Callback for anchor 3 

    :param data:  containing tag object

    """    
    global anchor_3
    anchor_3 = data

def TagCallback(data):
    """
    Callback for tag 

    :param data:  containing tag object

    """
    global tag
    tag = data


# Initialise node 
rospy.init_node('dwm1001_service')
# Subscribe to anchors and tag topic
rospy.Subscriber("/dwm1001/anchor0", Anchor, Anchor0callback)
rospy.Subscriber("/dwm1001/anchor1", Anchor, Anchor1callback)
rospy.Subscriber("/dwm1001/anchor2", Anchor, Anchor2callback)
rospy.Subscriber("/dwm1001/anchor3", Anchor, Anchor3callback)
rospy.Subscriber("/dwm1001/tag",     Tag,    TagCallback)

# Declare services for tag and anchor
rospy.Service('/Anchor_0', Anchor_0, triggerResponseAnchor0)
rospy.Service('/Anchor_1', Anchor_1, triggerResponseAnchor1)
rospy.Service('/Anchor_2', Anchor_2, triggerResponseAnchor2)
rospy.Service('/Anchor_3', Anchor_3, triggerResponseAnchor3)
rospy.Service('/Tag',      Tag_srv,  triggerResponseTag)

# Spin ROS so it doesn'y stop
rospy.spin()

