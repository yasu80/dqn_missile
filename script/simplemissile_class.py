# coding: utf-8
# Python 3.5.2

import matplotlib.pyplot as plt
import math

class Missile:
   def __init__(self,mass,inertia,g):
      self._mass = mass
      self._inertia = inertia
      self._g = g
   def update_x(self,_x, _v,_theta):
      return _x + _v * math.sin(math.radians(_theta))
   def update_y(self,_y, _v,_theta):
      return _y + _v * math.cos(math.radians(_theta))
   def update_theta(self,_theta):
      return _theta + self._inertia *self._g * math.cos(math.radians(_theta))
   

x = 0.0
y = 10.0
v = 100.0
theta = 30.0
limit_upper = 100

resolution = 0.1

m = Missile(1,1,0)
for num in range(limit_upper):
   x = m.update_x(x, v, theta) * resolution
   y = m.update_y(y, v, theta) * resolution
   theta = m.update_theta(theta) * resolution
   plt.plot(x, y, color="k", marker="o")
   print(" x :", x)
   print(" y :", y ,"\n")

   if num == limit_upper:
      break
plt.show()
print("terminated.")

