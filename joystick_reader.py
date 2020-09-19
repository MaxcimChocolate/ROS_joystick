
#include <ros/ros.h>
#include <sensor_msgs/Joy.h>

import rospy 
from std_msgs.msg import String 



def talker():

	rospy.init_node('joystick_reader')

	publisher = rospy.Publisher("/joystick_data", String, queue_size=10)


	rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		publisher.publish('Hey!')
		rate.sleep()


if __name__ == '__main__':
	talker()
