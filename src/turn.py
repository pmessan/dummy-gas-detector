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



def rotate(vel_pub, angular_speed, target_angle, clockwise=False):
    global x, y
    # init twist object to send velocity message
    vel_message = Twist()

    #initial pose
    x0 = x
    y0 = y
    t0 = rospy.Time.now().to_sec()

    #determine direction
    if (clockwise):
        vel_message.angular.z = -abs(angular_speed)
    else:
        vel_message.angular.z = abs(angular_speed)

    # set rate
    rate = rospy.Rate(10)
    ang_turned = 0


    while ang_turned < target_angle:
        # publish
        vel_pub.publish(vel_message)
        rate.sleep()

        # track angle covered
        t1 = rospy.Time.now().to_sec()
        ang_turned = (t1-t0) * angular_speed
        print(math.degrees(ang_turned), end="\r")
        sys.stdout.flush()
    print(math.degrees(ang_turned))
    rospy.loginfo("Angle turned")





if __name__ == "__main__":
    rospy.init_node("move_straight_node")

    vel_publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    pose_subscriber = rospy.Subscriber("/turtle1/pose", Pose, poseCallback)
    
    time.sleep(2)
    
    try :
        rotate(vel_publisher, math.radians(float(sys.argv[1])), math.radians(float(sys.argv[2])), clockwise=False)

    except rospy.ROSInterruptException:
        sys.exit(1)