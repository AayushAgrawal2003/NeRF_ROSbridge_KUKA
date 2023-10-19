#!/usr/bin/env python  

import time
import rospy
from utils import get_camera_transform, create_json, dictionary_generate
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
# Create the dictonary in the format of sample.json 
rospy.init_node('data_gen')


class ImageGenerator():
    def __init__(self):
        self.image_number = 0
        
    def image_callback(self,msg):
        bridge = CvBridge()
        if self.ref != 1: return
        try:
            # Convert the ROS Image message to a OpenCV image
            print("image added")
            cv_image = bridge.imgmsg_to_cv2(msg)
            cv2.imwrite("/home/inspire_01/catkin_ws/src/NeRF_ROSbridge_KUKA/data/test/" + str(self.image_number).zfill(3)+ ".jpg" , cv_image)
            self.ref = 0
        except Exception as e:
            rospy.logerr("Error converting ROS Image to OpenCV image: %s", str(e))
        
        return
        

    def get_frame(self):
        self.image_number += 1
        self.ref = 1
        rospy.Subscriber("/rgb", Image, self.image_callback)
        return

image = ImageGenerator()



dict = dictionary_generate()
start_time = time.time()
rate = rospy.Rate(0.1)
itr = 1
while time.time() < start_time + 60:
    frame = {
        # TODO: Get image form the camera
        "file_path": "data/test/" + str(itr).zfill(3) + ".jpg",
        # TODO: calculate this value using blur detection
        "sharpness": 30,
        # Get the transformation matrix using the heleper function
        "transform_matrix": get_camera_transform()
    } 
    dict["frames"].append(frame)
    image.get_frame()

    rate.sleep()

    itr += 1 

create_json(dict)

