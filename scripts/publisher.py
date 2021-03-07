#!/usr/bin/env python
# license removed for brevity
import rospy
from sensor_msgs.msg import Image
import random
import os
import cv2
from cv_bridge import CvBridge, CvBridgeError
import numpy as np

def talker():
    pub = rospy.Publisher('chatter', Image, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
	img_name = random.choice([x for x in os.listdir("/home/robotics/Scrivania/imgs") if os.path.isfile(os.path.join("/home/robotics/Scrivania/imgs", x))])
        img = cv2.imread("/home/robotics/Scrivania/imgs/"+img_name)
	img_msg=CvBridge().cv2_to_imgmsg(img)
        rospy.loginfo(img_msg)
        pub.publish(img_msg)
        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('talker', anonymous=True)
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
