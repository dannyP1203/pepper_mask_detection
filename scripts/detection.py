#!/usr/bin/env python

import rospy
import cv2
import skimage
import time
import numpy as np
from rospkg import RosPack

from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
from numpy import random

import sys
import os

import mrcnn.model as modellib
from mrcnn.config import Config
from mrcnn import visualize

import tensorflow as tf

import keras
from keras.backend import clear_session
from keras.backend import set_session
from skimage import data
from skimage.viewer import ImageViewer
from skimage.util import img_as_float

import matplotlib.pyplot as plt



sess = tf.Session()
graph = tf.get_default_graph()
class_names = ['BG', 'face_mask', 'face']

rp = RosPack()
pkg_path = rp.get_path('mask_detection')
img_path = pkg_path + "/image/detection_image.jpg"
weights_path = pkg_path + "/weights.h5"


# define a configuration for the model
class PredictConfig(Config):
	# Give the configuration a recognizable name
	NAME = "mask_config"

	# Number of classes (background + without_mask and with_mask)
	NUM_CLASSES = 1 + 2

	# Number of images trained per GPU
	IMAGES_PER_GPU = 1

	# Skip detection with <90% confidence
	DETECTION_MIN_CONFIDENCE = 0.9

def talker():
	global sess
	global graph

	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():
		cv_image = cv2.imread(img_path)

		if (cv_image is not None):
			with graph.as_default():
				set_session(sess)
				if (cv_image.shape[0]>1024 or cv_image.shape[1]>1024):
					max_dim=np.maximum(cv_image.shape[0],cv_image.shape[1])
					perc=100*max_dim/1024
					height=int(cv_image.shape[0]*(100-(perc-100))/100)
					width=int(cv_image.shape[1]*(100-(perc-100))/100)
					cv_image=cv2.resize(cv_image,(width,height))

				results = model.detect([cv_image], verbose=0)

				r = results[0]

				final_image=visualize.display_instances(cv_image, r['rois'], r['masks'], r['class_ids'],
					    class_names, r['scores'])
				cv2.imshow("Detection",final_image)
				cv2.waitKey(3)


			output_string = "Numero persone: " + str(len(r["class_ids"])) + " || "
			i=0
			for elem in r["class_ids"]:
				if elem == 1:
					output_string += "Persona con mascherina (confidenza: " + str(r["scores"][i]) + ") || "
				if elem == 2:
					output_string += "Persona senza mascherina (confidenza: " + str(r["scores"][i]) + ") || "
				i+=1

			pub = rospy.Publisher('detection_pub', String, queue_size=10)
			rospy.loginfo(output_string)
			pub.publish(output_string)
			rate.sleep()

if __name__ == '__main__':

	rospy.init_node('talker', anonymous=True)

	# create config
	cfg = PredictConfig()
	# define the model
	global model
	set_session(sess)
	model = modellib.MaskRCNN(mode='inference', model_dir='./', config=cfg)
	# load model weights
	model.load_weights(weights_path, by_name=True)

	model.keras_model._make_predict_function()

	try:
		talker()
	except rospy.ROSInterruptException:
		pass
