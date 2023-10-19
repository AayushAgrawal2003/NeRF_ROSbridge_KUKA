#!/usr/bin/env python  

import rospy
from utils import get_camera_transform, create_json, dictionary_generate



# Create the dictonary in the format of sample.json 

dict = dictionary_generate()
for i in range(1): 
    frame = {
        # TODO: Get image form the camera
        "file_path": "images/0001.jpg",
        # TODO: calculate this value using blur detection
        "sharpness": 31.752987436300323,
        # Get the transformation matrix using the heleper function
        "transform_matrix": get_camera_transform()
    } 
    dict["frames"].append(frame)

create_json(dict)