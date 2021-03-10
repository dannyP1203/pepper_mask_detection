#!/usr/bin/env python

import rospy
import cv2
import skimage
import time
import numpy as np
from rospkg import RosPack

from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge, CvBridgeError

import mrcnn.model as modellib
from mrcnn.config import Config
from mrcnn import visualize
from skimage.util import img_as_float

import sys
import os
import matplotlib.pyplot as plt

class image_converter:

	def __init__(self):
		# print ("passaggio: __init__")
		self.bridge = CvBridge()

		self.rp = RosPack()
		self.pkg_path = self.rp.get_path('mask_detection')
		self.img_path = self.pkg_path + "/image/detection_image.jpg"

		self.image_topic = rospy.get_param('~image_topic')

		# self.image_sub = rospy.Subscriber("chatter",Image,self.callback)
		self.image_sub = rospy.Subscriber(self.image_topic, CompressedImage, self.callback)

	def callback(self, data):
		# print ("passaggio: callback")

		try:
			cv_image = self.bridge.compressed_imgmsg_to_cv2(data, "passthrough")
		except CvBridgeError as e:
			print("CvBridgeError: " + str(e))

		cv2.imshow("Video stream", cv_image)
		cv2.waitKey(3)
		cv2.imwrite(self.img_path, cv_image)

def main(args):
	rospy.init_node('image_converter', anonymous=True)
	ic = image_converter()

	try:
		# print("passaggio: spin")
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main(sys.argv)
