# coding: utf-8
# Python 3.5.2

import matplotlib.pyplot as plt
import math

class Missile:
   def __init__(self,mass,inertia,g,impulse):
      self._mass = mass
      self._inertia = inertia
      self._g = g
      self._impulse = impulse
   def update_x(self,_x, _v,_theta):
      return _x + _v * math.sin(math.radians(_theta))
   def update_y(self,_y, _v,_theta):
      return _y + _v * math.cos(math.radians(_theta))
   def update_theta(self,_theta):
      return _theta + self._inertia *self._g * math.cos(math.radians(_theta))
   def update_speed(self,_theta,_v):
      return _v + self._impulse / self._mass - self._g * math.cos(math.radians(_theta))
   

x = 0.0
y = 0.0
v = 100.0
theta = 15.0
limit_upper = 100


m = Missile(1,0.1,9.8,10)
for num in range(limit_upper):
   x = m.update_x(x, v, theta)
   y = m.update_y(y, v, theta)
   v = m.update_speed(theta, v)
   theta = m.update_theta(theta)
   plt.plot(x, y, color="k", marker="o")
   print(" x :", x)
   print(" y :", y ,"\n")
   if num == limit_upper:
      break
plt.show()
print("terminated.")

