#!/usr/bin/env python
import rospy

from std_msgs.msg import String

def talker():

    pub = rospy.Publisher('hello_pub', String, queue_size=10)

    rospy.init_node('hello_world_publisher', anonymous=True)

    r = rospy.Rate(1)

    while not rospy.is_shutdown():
        msg = "Test message. Time now: " + str(rospy.get_time())[:-3]

        rospy.loginfo(msg)

        pub.publish(msg)

        r.sleep()

if __name__ == '__main__':
    try: 
        talker()
    except rospy.ROSInterruptException: pass