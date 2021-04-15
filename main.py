# # this is the code that moves the robotic arm using the pcm
#%%
import time
from adafruit_servokit import ServoKit
 
# Set channels to the number of servo channels on your kit.
kit = ServoKit(channels=16)


# if __name__ == __main__:
kit.servo[0].angle = 180
time.sleep(1)


kit.servo[2].angle = 180 -40
time.sleep(1)

kit.servo[2].angle = 180
kit.servo[0].angle = 0