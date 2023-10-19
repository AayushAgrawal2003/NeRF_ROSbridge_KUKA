#!/usr/bin/env python  
import rospy
import tf2_ros
import numpy as np
import json


from tf.transformations import translation_matrix, quaternion_matrix



def get_camera_transform():
    rospy.init_node('tf_echo_node')
    tfbuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfbuffer)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            transform_msg = tfbuffer.lookup_transform('base_link', 'iiwa_link_7', rospy.Time(0) , rospy.Duration(1))
            translation = [transform_msg.transform.translation.x, transform_msg.transform.translation.y, transform_msg.transform.translation.z]
            rotation = [transform_msg.transform.rotation.x, transform_msg.transform.rotation.y, transform_msg.transform.rotation.z, transform_msg.transform.rotation.w]

            # Create a 4x4 translation matrix
            matrix = translation_matrix(translation)

            # Create a 4x4 rotation matrix from the quaternion
            rotation_matrix = quaternion_matrix(rotation)

            # Combine the translation and rotation matrices to get the 4x4 transformation matrix
            transformation_matrix = np.dot(matrix, rotation_matrix)
            final = []
            for i in transformation_matrix:
                final.append(list(i))

            return(final)
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
            print("Fail", e)
    
        rate.sleep()   


def create_json(dict):
    # import library to convert dict to json
    with open("/Users/aayushagrawal/Desktop/Abhiyaan/ros_ws/caktin_ws/src/ros_nerf_bridge/json/test.json", "w") as outfile: 
        json.dump(dict,outfile)
    return 


def dictionary_generate():

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


def get_frame():
    pass 

def frame_sharpness():
    pass
