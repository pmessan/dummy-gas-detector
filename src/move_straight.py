#!/usr/bin/env python3
import sys
import rospy
import time
import math
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

# Global variables
x = None
y = None
yaw = None

def poseCallback(pose_message):
    global x, y, yaw
    # update the pose for the other functions
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta

def move(vel_pub, speed, distance, forward):
    global x, y
    # init twist object to send velocity message
    vel_message = Twist()

    #initial pose
    x0 = x
    y0 = y

    #determine direction
    if (forward):
        vel_message.linear.x = abs(speed)
    else:
        vel_message.linear.x = -abs(speed)

    # set rate
    rate = rospy.Rate(10)
    dist_moved = 0


    while dist_moved < distance:
        # publish
        vel_pub.publish(vel_message)
        rate.sleep()

        # track distance moved
        dist_moved = math.sqrt((x-x0)**2 + (y-y0)**2)
        print(dist_moved, end="\r")
        sys.stdout.flush()
    print(dist_moved)
    rospy.loginfo("Distance covered!")





if __name__ == "__main__":
    rospy.init_node("move_straight_node")

    vel_publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    pose_subscriber = rospy.Subscriber("/turtle1/pose", Pose, poseCallback)
    
    time.sleep(2)
    
    try :
        move(vel_publisher, float(sys.argv[1]), float(sys.argv[2]), forward=bool(sys.argv[3]))

    except rospy.ROSInterruptException:
        pass