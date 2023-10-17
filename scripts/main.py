#!/usr/bin/env python  

import rospy
import tf2_ros

if __name__ == '__main__':
  rospy.init_node('tf_echo_node')

  tf_buffer = tf2_ros.Buffer()
  tf_listener = tf2_ros.TransformListener(tf_buffer)

  # Create a tf2_ros.StampedTransform object

  # Get the transform between the two frames
  try:
    stamped_transform = tf_buffer.lookup_transform('source_frame', 'target_frame', rospy.Time())
  except (tf2_ros.LookupException, tf2_ros.ExtrapolationException):
    rospy.logerr('Failed to get transform between source_frame and target_frame')
    exit()
