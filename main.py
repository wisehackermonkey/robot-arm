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



def move_arm(servo_number, angle_degrees, delay_seconds=1):
  """this just makes the process for moving the arm easier 
  
  servo_number  = Motor number 0,1,2, or 3
  angle_degrees = 0-180 degrees
  delay_seconds = ex: "4" seconds motors wait for 4 sec before moving to next

  EX: 
  move_arm(0, 180, 60) : Move motor 1 to 180 degrees, then wait 1 minute
  move_arm(3, 45, 1)   : Move motor 3 to 45 degrees, then wait 1 second
  move_arm(2, 0, 5)    : Move motor 2 to 0 degrees, then wait 5 seconds
  """
  kit.servo[servo_number].angle = angle_degrees
  
  time.sleep(delay_seconds)


# set inital position for arm
move_arm(0,180)



#====================================
# Edit code below here!
#====================================


# HERE!
move_arm(0,180,1)
move_arm(1,180,1)
move_arm(2,180,1)
move_arm(3,180,1)

move_arm(0,180,1)
move_arm(1,160,1)
move_arm(2,140,1)
move_arm(3,80,1)
#====================================
# ################################# #
#====================================

# put arm into final position
move_arm(0,180,0)
move_arm(2,180,0)