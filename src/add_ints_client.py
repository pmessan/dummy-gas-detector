#!/usr/bin/env python3

import rospy, sys

from dummy_gas_detector.srv import AddInts
from dummy_gas_detector.srv import AddIntsRequest
from dummy_gas_detector.srv import AddIntsResponse
from rospy.exceptions import ROSInterruptException

def add_ints_client(x, y):
    rospy.wait_for_service("add_ints")

    try:
        add_ints = rospy.ServiceProxy("add_ints", AddInts)
        res = add_ints(x, y)
        return res.sum
    except rospy.service.ServiceException(e):
        print("Service call failed\n")


if __name__ == "__main__":
    try: 
        print(add_ints_client(int(sys.argv[1]), int(sys.argv[2])))
    except ROSInterruptException:
        print("Exiting...")
        sys.exit(1)