#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import math
import numpy as np

# Create your objects here.
ev3 = EV3Brick()

# Initialize
joint1 = Motor(Port.A)
joint2= Motor(Port.B)
joint3 = Motor(Port.C)

#設好"日"筆畫的座標
x= 1*np.ones(10)
y= np.linspace(1, -20, 10)

#設定參數
l1 = 12
l2 = 14


#開始寫字
#還沒考慮提筆問題
for i in range(0,(len(x)-1)):
    theta = caculate_thera(x[i],y[i])
    joint1.run_target(100,theta[0]*180/math.pi)
    joint2.run_target(100,theta[1]*180/math.pi)

def caculate_theta(x,y):
        temp = (x**2+y**2-12**2-14**2)/(2*12*14)
        theta2 = math.acos(temp)
        alpha = math.atan2(x,y)
        temp2 = (l2*math.sin(theta2))/math.sqrt(x[i]**2+y[i]**2)
        theta = math.asin(temp2)
        theta1 = alpha - theta
    return [theta1,theta2]

## Pen lifting
### Lifting the pen
def lift_wrist():
    joint3.run_angle(10, 45) # lift the pen by 45 degrees, + or - can be later adjusted
    joint3.hold()
    wait(1000)

### Dorpping down the pen
def drop_wrist():
    joint3.run_angle(10, -45) # drop down the pen by 45 degrees back, + or - can be later adjusted
    joint3.hold()
    wait(1000)