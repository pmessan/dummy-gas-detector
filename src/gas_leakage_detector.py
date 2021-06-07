#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from dummy_gas_detector.msg import GasSensor
from random import random, seed, randint

gases = ["LPG", "Methane", "Butane", "Nitrogen", "Ozone", "Tetrafluoromethane"]
def publisher():
    rospy.init_node("GasDetectorNode", anonymous=False)
    # it's a publisher node
    pub = rospy.Publisher("/gas_concentration", GasSensor, queue_size=10)
    rate = rospy.Rate(1)
    seed(1)
    m_id = randint(0, 10000)
    while not rospy.is_shutdown():
        message = GasSensor()
        #gen random id
        message.id = m_id
        message.concentration = random() * 100
        message.gasType = gases[randint(0, 6)-1]
        message.timestamp = rospy.Time.now()
        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()

if __name__ == '__main__':
    try: 
        publisher()

    except rospy.ROSInterruptException:
        pass
