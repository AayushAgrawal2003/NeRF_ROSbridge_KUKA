#!/usr/bin/env python  
import roslib
import rospy
import math
import tf2_ros
import PyKDL
import geometry_msgs.msg
from math import pi
import numpy as np
from tf import transformations

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

            print(transformation_matrix)
            break
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
            print("Fail", e)
    
        rate.sleep()   

get_camera_transform()