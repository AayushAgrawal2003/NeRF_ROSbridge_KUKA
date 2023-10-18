#!/usr/bin/env python  

import rospy
from utils import get_camera_transform, create_json


# Create the data generation pipeline

get_camera_transform()

# Create the dictonary in the format of sample.json 

dict = {
    "camera_angle_x": 0.7481849417937728,
    "camera_angle_y": 1.2193576119562444,
    "fl_x": 1375.52,
    "fl_y": 1374.49,
    "k1": 0.0578421,
    "k2": -0.0805099,
    "p1": -0.000980296,
    "p2": 0.00015575,
    "cx": 554.558,
    "cy": 965.268,
    "w": 1080.0,
    "h": 1920.0,
    "aabb_scale": 4,
    "frames": []
}

frame = {
        # TODO: Get image form the camera
        "file_path": "images/0001.jpg",

        # TODO: figure out how to set sharpness
        "sharpness": 31.752987436300323,

        # Get the transformation matrix using the heleper function
        "transform_matrix": get_camera_transform()
} 

for i in range(1): 
    dict["frames"].append(frame)

create_json(dict)