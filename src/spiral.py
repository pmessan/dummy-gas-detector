#!/usr/bin/env python3

import rospy, sys, math, time

from geometry_msgs.msg import Twist
from rospy.exceptions import ROSInterruptException
from turtlesim.msg import Pose

x = None
y = None

def poseUpdate(pose_msg):
    global x, y
    x = pose_msg.x
    y = pose_msg.y

def spiral(vel_publisher, lin_vel, ang_vel):
    global x, y
    vel_msg = Twist()
    
    vel_msg.angular.z = ang_vel
    rate = rospy.Rate(1)

    while (x<10 and y<10):
        lin_vel+=0.5
        vel_msg.linear.x = lin_vel
        vel_publisher.publish(vel_msg)
        rate.sleep()

    # publish message
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    vel_publisher.publish(vel_msg)


if __name__ == "__main__":
    rospy.init_node("spiral_motion")
    vel_publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    pose_publisher = rospy.Subscriber("/turtle1/pose", Pose, poseUpdate)
    time.sleep(2)
    try :
        spiral(vel_publisher, float(sys.argv[1]), math.radians(float(sys.argv[2])))

    except ROSInterruptException:
        exit()