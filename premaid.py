# 3d printed Robotic Arm Project 
# this is the code that moves the robotic arm using the pcm

# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20210511

import time
from adafruit_servokit import ServoKit
 
# Set channels to the number of servo channels on your kit.
kit = ServoKit(channels=16)


def move_arm(server_number, position, delay=1):
  """this just makes the process for moving the arm easier """
  kit.servo[server_number].angle = position
  
  time.sleep(delay)


# set inital position for arm
move_arm(0,180)
move_arm(1,180)
move_arm(2,180)
move_arm(3,180)


move_arm(0,0)
move_arm(1,0)
move_arm(2,0)
move_arm(3,0)


