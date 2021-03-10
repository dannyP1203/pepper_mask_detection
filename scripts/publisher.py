#!/usr/bin/env python

import rospy
import random
import os
import cv2
import numpy as np
from rospkg import RosPack

from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge, CvBridgeError



rp = RosPack()
pkg_path = rp.get_path('mask_detection')
samples_path = pkg_path + "/samples"

def talker():
    pub = rospy.Publisher('chatter', CompressedImage, queue_size=10)
    rate = rospy.Rate(1) # 1hz: 1 img/s

    while not rospy.is_shutdown():
        img_name = random.choice([x for x in os.listdir(samples_path) if os.path.isfile(os.path.join(samples_path, x))])
        img = cv2.imread(os.path.join(samples_path, img_name))
        img_msg = CvBridge().cv2_to_compressed_imgmsg(img)
        # rospy.loginfo(img_msg)
        pub.publish(img_msg)
        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('talker', anonymous=True)
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
