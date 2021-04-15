# robot-arm
----
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<!-- <img src="assets/NNNNNNNNNNNNN" width="400"> -->
<h2 align="center">This project is to create code that moves my robotic arm, ideally using ROS (robotic operating system)</h2>

<!-- <h4 align="center">________________________</h4> -->


# Quick start
### __________________
<!-- 
##### __________________________
```bash
``` 
-->

# Summary
<!-- ### -  *[Quick start](#Quick-start)*
### -  *[Installation](#Installation)*
### -  *[For developers](#For-developers)* -->
### -  *[Contributors](#Contributors)*
### -  *[Todo](#TODO)*
### -  *[License](#License)*




# Installation
```bash
```

<!-- ----------------- -->
<!-- # Screenshots -->
<!-- - <img src="assets/_____________" width="400">  -->
<!-- -  -->



<!-- SETUP -->
-----------------
# For developers
### Install circuit python on raspberry pi 4
### [Installing CircuitPython Libraries on Raspberry Pi | CircuitPython on Linux and Raspberry Pi | Adafruit Learning System](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)
```bash
git clone https://github.com/wisehackermonkey/robot-arm.git
cd ~/robot-arm
sudo pip3 install --upgrade adafruit-python-shell

# wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo apt-get install -y i2c-tools
pip3 install --upgrade RPi.GPIO
pip3 install --upgrade adafruit-blinka

ls /dev/i2c* /dev/spi*
/dev/i2c-1 /dev/spidev0.0 /dev/spidev0.1

```
### NOTE i had an issue with dietpi spi not working solution is here
#### [raspbian - Unable to activate SPI module on Raspberry Pi Zero W running on DietPi - Raspberry Pi Stack Exchange](https://raspberrypi.stackexchange.com/questions/70768/unable-to-activate-spi-module-on-raspberry-pi-zero-w-running-on-dietpi) 

### install this library 
#### [adafruit/Adafruit_CircuitPython_PCA9685: Adafruit CircuitPython driver for PCA9685 16-channel, 12-bit PWM LED & servo driver chip.](https://github.com/adafruit/Adafruit_CircuitPython_PCA9685)

```bash
pip3 install adafruit-circuitpython-pca9685
pip3 install adafruit-circuitpython-servokit
```
### issue
```bash
    raise ValueError("No I2C device at address: 0x%x" % self.device_address)
ValueError: No I2C device at address: 0x40
```
### solution
```
sudo i2cdetect -y 1

root@dietpi4:~/github/robot-arm# sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --                         
```
#### WEIRD!
##### issue was the pins werint connected! ha. wow. 
##### [Adafruit customer service forums • View topic - VEML6075 "No I2C device at address: 10" [SOLVED}](https://forums.adafruit.com/viewtopic.php?t=147027)
```bash

     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: 40 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: 70 -- -- -- -- -- -- --                    
```

-----------------
# conversion to ros node
### how i found the correct message format
### NOPE: [common_msgs - ROS Wiki](http://wiki.ros.org/common_msgs)
### YEP: [std_msgs - ROS Wiki](http://wiki.ros.org/std_msgs)

#### final datatype i went with 
#### [std_msgs/Int16MultiArray Documentation](http://docs.ros.org/en/api/std_msgs/html/msg/Int16MultiArray.html)
```
# Please look at the MultiArrayLayout message definition for
# documentation on all multiarrays.

MultiArrayLayout  layout        # specification of data layout
int16[]           data          # array of data
```
### key info is `int16[]`

-----------------
# TODO
- [x] setup on raspberry pi
- [ ] add controll software similar to this [meisben/easyEEZYbotARM: A python and arduino control library for the EEZYbotARM 3d printed robot arm (Includes 3-D kinematics for Mk1 and Mk2)](https://github.com/meisben/easyEEZYbotARM) 
- [ ] ros node 
- [ ] ___________ 
- [ ] ___________ 
- [ ] ___________ 

-----------------
# Contributors

[![](https://contrib.rocks/image?repo=wisehackermonkey/robot-arm)](https://github.com/wisehackermonkey/robot-arm/graphs/contributors)

##### Made with [contributors-img](https://contrib.rocks).

-----------------
# License
#### MIT © wisehackermonkey
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
```bash
by oran collins
github.com/wisehackermonkey
oranbusiness@gmail.com
______________________
```

















<!-- ---------------------------------- -->
<!-- FULL -->
<!-- ---------------------------------- -->

<!-- # robot-arm -->
<!-- ---- -->
<!-- 
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<img src="assets/NNNNNNNNNNNNN" width="400">
<h2 align="center">____________________</h2>
<h4 align="center">________________________</h4>
 -->

<!-- 

# Quick start
### __________________
##### __________________________
```bash
```

 -->


<!-- 

# Summary
### -  *[Quick start](#Quick-start)*
### -  *[Live Demo](#Live-demo)*
### -  *[Installation](#Installation)*
### -  *[Screenshots](#Screenshots)*
### -  *[License](#License)*
### -  *[Features](#Features)*
### -  *[For developers](#For-developers)*
### -  *[Todo](#TODO)*
### -  *[Related](#Related)*
### -  *[Contributors](#Contributors)*
 -->



<!-- ----------------- -->
<!-- <img src="assets/KKKKKKKKKKK" width="400"> -->
<!-- # [Live Demo](https://www._____________.com) -->





<!-- 
# Installation
### 
```bash
``` 
-->




<!-- 

-----------------
# Screenshots
- <img src="assets/_____________" width="400"> 
- 
-->



<!-- 

# Features
- [x] ______
- [ ] ______

-->


<!-- 
-----------------
# For developers
### 
```bash
```
 -->





<!-- -----------------
# TODO
- [x] ___________
- [ ] ___________ 
-->

<!-- 
-----------------
# Built with
- #### ________________
-->





<!-- -----------------
# Related 
### [_________](https://www.____________.com)
 -->





<!-- 
-----------------
# Contributors

[![](https://contrib.rocks/image?repo=wisehackermonkey/robot-arm)](https://github.com/wisehackermonkey/robot-arm/graphs/contributors)

##### Made with [contributors-img](https://contrib.rocks).

-----------------
# License
#### MIT © wisehackermonkey
[![MIT](https://img.shields.io/github/license/wisehackermonkey/robot-arm.svg)](https://github.com/wisehackermonkey/robot-arm/blob/master/LICENSE)
-->

<!-- 
```bash
by oran collins
github.com/wisehackermonkey
oranbusiness@gmail.com
______________________
``` 
-->

<!-- ---------------------------------- -->
<!-- EXTRAS -->
<!-- ----------------------------------- -->
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<!-- 
[![Javascript](https://img.shields.io/badge/Javascript-Enabled-lightgreen.svg)](https://shields.io/) 
[![forthebadge made-with-python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![Python](https://img.shields.io/badge/Python-Enabled-<COLOR>.svg)
![P5.js](https://img.shields.io/badge/P5.js-Enabled-pink.svg)
[![Generic badge](https://img.shields.io/badge/<SUBJECT>-<STATUS>-<COLOR>.svg)](https://shields.io/)
[![GitHub release](https://img.shields.io/github/release/wisehackermonkey/robot-arm.svg)](https://GitHub.com/wisehackermonkey/robot-arm/releases/)
[![GitHub tag](https://img.shields.io/github/tag/wisehackermonkey/robot-arm.svg)](https://GitHub.com/wisehackermonkey/robot-arm/tags/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/wisehackermonkey/robot-arm.svg)](https://GitHub.com/wisehackermonkey/robot-arm/pull/)
[![Website perso.crans.org](https://img.shields.io/website-up-down-green-red/http/www.orancollins.com.svg)](http://www.orancollins.com/) 
    -->

<!-- 
# https://yuml.me/diagram/plain/activity/draw
### (start)->[AAAAAAAA]<aaaaa->(BBBBBB)->(end) 

# Diagram
## 
```bash
```
 -->

<!-- 

# List
- 
- 
- 

# Table
| XXX | YYYY |
|----- |-----|
| ___s | ____| 

| XXX  | YYYY |
|:-----|:-----:|
| ___s | ____| 


# Toggle List (NO FORMATTING)
<details><summary>AAAAAAAA</summary>
<details><summary>Hidden A</summary>
</details>
</details>

<details><summary>BBBBBBBBB</summary>
<details><summary>Hidden B</summary>
</details>
</details>

<details><summary>CCCCCCCCC</summary>
</details>



# Toggle list with formatting
<details><summary>Level 1</summary></details>

<details><summary>&emsp;BBBBBBBBB</summary></details>
<details><summary>&emsp;&emsp;CCCCCCCCC</summary></details>
<details><summary>&emsp;&emsp;&emsp;DDDDDDDDD</summary></details>


# Toggle list Nested
<details><summary>Level 1</summary>

<details><summary>&emsp;BBBBBBBBB</summary>
<details><summary>&emsp;&emsp;CCCCCCCCC</summary>
<details><summary>&emsp;&emsp;&emsp;DDDDDDDDD</summary>

</details></details></details></details></details></details></details></details></details></details></details></details></details></details></details></details></details></details>

# Keyboard Commnand
### <kbd>Command/ctrl + R</kbd> 

# Installation
### 
```bash
cd ~
git clone https://github.com/wisehackermonkey/robot-arm.git
cd robot-arm
pip install -r requirements.txt
npm install
```

# Docker
### Build
```bash
cd ~
git clone https://github.com/wisehackermonkey/robot-arm.git
cd robot-arm
docker build -t wisehackermonkey/robot-arm:latest .  
```
### Run
```bash
docker run -it --rm --name wisehackermonkey/robot-arm:latest  
```
### Docker-compose
```bash
docker-compose build
docker-compose up 
```



# Publish Docker Image
```bash
docker build -t wisehackermonkey/robot-arm:latest .
docker login
docker push wisehackermonkey/robot-arm:latest
```

 -->