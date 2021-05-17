#!/usr/bin/python3

import rospy 
from std_msgs.msg import String
# custom message

def talker():
    rospy.init_node("my_talker", anonymous=True)
    pub = rospy.Publisher("/my_topic", String, queue_size=10)
    r = rospy.Rate(0.5)

    while not rospy.is_shutdown():
        hello = "Hi thereeeee!"
        rospy.loginfo(hello)
        pub.publish(hello)
        r.sleep()

try: 
    talker()

except rospy.ROSInterruptException:
    pass