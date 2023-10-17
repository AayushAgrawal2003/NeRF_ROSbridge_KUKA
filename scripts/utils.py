#!/usr/bin/env python  
import roslib
import rospy
import math
import tf2_ros
import PyKDL
import geometry_msgs.msg
from math import pi


if __name__ == '__main__':
    rospy.init_node('tf_echo')

    tfbuffer = tf2_ros.Buffer()

    listener = tf2_ros.TransformListener(tfbuffer)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            trans = tfbuffer.lookup_transform('base_link', 'iiwa_link_7', rospy.Time(0) , rospy.Duration(1))
            print(trans)
            trans = trans.transform
            rot = PyKDL.Rotation.Quaternion(* [ eval('trans.rotation.'+c) for c in 'xyzw'] )
            print(' '.join( [ str(eval('trans.rotation.'+c)) for c in 'xyzw'] ))
            ypr = [ i  / pi * 180 for i in rot.GetEulerZYX() ]

        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
            print("Fail", e)
    
        rate.sleep()