#!/usr/bin/env python3

import rospy
from dummy_gas_detector.srv import AddInts
from dummy_gas_detector.srv import AddIntsRequest
from dummy_gas_detector.srv import AddIntsResponse
from rospy.exceptions import ROSInterruptException


def addIntsServer():
    rospy.init_node("add_ints_server")
    rospy.Service("add_ints", AddInts, add_ints)
    rospy.loginfo("Ready to add Ints...")
    rospy.spin()


def add_ints(req):
    # req.x + req.y
    result = req.x + req.y
    rospy.loginfo("{} + {} = {}".format(req.x, req.y, result))
    return AddIntsResponse(result)


if __name__ == "__main__":
    try:
        addIntsServer()
    except ROSInterruptException:
        pass

    
