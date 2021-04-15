# this is a ros node controller for my robotic arm 
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20210415

# ros setup
import rospy
import math
import time
from time import sleep
# this is the only one of intrest its allows me to have an array of 
#   arm angles ex: [90,23,180,0]
from std_msgs.msg import Int16MultiArray

# hardware setup
from adafruit_servokit import ServoKit
# Set channels to the number of servo channels on your PCA9685.
kit = ServoKit(channels=16)



def position_arm(msg: Int16MultiArray)->None:
    print(msg)
    print(msg.data)

    base_angle = msg.data[0] 
    sholder_angle = msg.data[1]
    lifter_angle = msg.data[2]
    gripper_angle = msg.data[4]

    kit.servo[0].angle = base_angle
    kit.servo[1].angle = sholder_angle
    kit.servo[2].angle = lifter_angle
    kit.servo[3].angle = gripper_angle
    time.sleep(1)





if __name__ == "__main__":
    # start ros node, meaning tell the ros master of its excistance
    rospy.init_node("arm_mover")

    # tell the ros master that there is a topic avaible and it uses Int16MultiArray
    # and the callback that is fired when the function is called is named  
    sub=rospy.Subscriber("/pose", Int16MultiArray, position_arm)
    
    rate=rospy.Rate(10)
    
    print("Arm Mover: Running")
    while not rospy.is_shutdown():
        rate.sleep()
    