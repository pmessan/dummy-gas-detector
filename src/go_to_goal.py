#!/usr/bin/env python3
import rospy 
import sys
import math
import time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

x=None
y=None
yaw=None

def go_to_goal(x_goal, y_goal, vel_publisher):
    # point is a dict object with x and y keys representing coordinates
    global x, y, yaw
    print
    #save initial points
    # x, y = x, y
    print(f"x={x}, y={y}")

    # create Twist() message object to send the generate_messages
    vel_msg = Twist()

    linear_dist = 0
    while True:
        # prepare data 

        # linear speed 
        kL = 0.5
        linear_dist = math.sqrt((x-x_goal)**2 + (y-y_goal)**2)
        vel_msg.linear.x = kL * linear_dist

        # angular speed
        kA = 4.0
        diff_vector = (x_goal-x, y_goal-y)
        diff_vector_ang = math.atan2(diff_vector[1], diff_vector[0])
        ang_dist = diff_vector_ang - yaw
        vel_msg.angular.z = ang_dist * kA

        # publish message
        vel_publisher.publish(vel_msg)

        print(f"x={x}, y={y}, dist_to_goal={linear_dist}", end="\r")

        if (linear_dist <0.09):
            break
    
    print(f"x={x}, y={y}, dist_to_goal={linear_dist}")
    rospy.loginfo("Destination Reached!")


def updatePose(pose_msg):
    global x, y, yaw

    x = pose_msg.x
    y = pose_msg.y
    yaw = pose_msg.theta



if __name__ == "__main__":

    try :
        rospy.init_node("go_to_goal_node")

        vel_publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

        pose_subscriber = rospy.Subscriber("/turtle1/pose", Pose, updatePose)

        time.sleep(2)

        go_to_goal(float(sys.argv[1]), float(sys.argv[2]), vel_publisher)

    except rospy.ROSInterruptException:
        pass