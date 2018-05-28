import math
import sys

t1 = 10
v1 = 15
t2 = 0
v2 = 25
t3 = -10
v3 = 35

t4 = input("Please enter air temperature: ")
if t4.isdigit() is False:
      print("Please enter only float type of input")
      sys.exit()

v4 =input("Please enter wind speed: ")
if v4.isdigit() is False:
      print("Please enter only float type of input")
      sys.exit()

t4 = float(t4)
v4 = float(v4)


print("For {} temperature and {} velocity of wind WTC index: {}".format(t1, v1, 35.74+0.6215*t1-35.75*v1**0.16+0.4275*t1*v1**0.16))

print("For {} temperature and {} velocity of wind WTC index: {}".format(t2, v2, 35.74+0.6215*t2-35.75*v2**0.16+0.4275*t2*v2**0.16))

print("For {} temperature and {} velocity of wind WTC index: {}".format(t3, v3, 35.74+0.6215*t3-35.75*v3**0.16+0.4275*t3*v3**0.16))

print("For {} temperature and {} velocity of wind WTC index: {}".format(t4, v4, 35.74+0.6215*t4-35.75*v4**0.16+0.4275*t4*v4**0.16))
