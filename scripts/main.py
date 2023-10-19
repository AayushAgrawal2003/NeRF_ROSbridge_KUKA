#!/usr/bin/env python  

import time
import rospy
from utils import get_camera_transform, create_json, dictionary_generate, get_frame, image_callback



# Create the dictonary in the format of sample.json 

rospy.init_node('data_gen')

# get_frame()
dict = dictionary_generate()
start_time = time.time()
rate = rospy.Rate(0.2)
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
    rate.sleep()

    itr += 1 

create_json(dict)