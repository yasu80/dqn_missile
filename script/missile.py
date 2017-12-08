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
      # theta must be attack of angle for ground plane; g for earth 
   def update_x(self,_x, _v,_theta):
      return _x + _v * math.cos(math.radians(_theta))
   def update_y(self,_y, _v,_theta):
      return _y + _v * math.sin(math.radians(_theta))
   def update_theta(self,_theta):
      # give _theta degree
      if (_theta >= 360) or( _theta <= -360):
            _theta = _theta % 360

      if _theta >= 0.0:
            if _theta >= 270:
                  return _theta - self._g * math.cos(math.radians(_theta)) / self._inertia
            elif _theta >= 180:                                                         
                  return _theta + self._g * math.cos(math.radians(_theta)) / self._inertia
            elif _theta >= 90:                                                          
                  return _theta + self._g * math.cos(math.radians(_theta)) / self._inertia
            else:                                                                       
                  return _theta - self._g * math.cos(math.radians(_theta)) / self._inertia
            
      elif _theta >= -90:
            return _theta - self._g * math.cos(math.radians(_theta)) / self._inertia
      if _theta >= -180:                                                         
            return _theta + self._g * math.cos(math.radians(_theta)) / self._inertia
      if _theta >= -270:                                                         
            return _theta + self._g * math.cos(math.radians(_theta)) / self._inertia
      if _theta >= -360:                                                         
            return _theta - self._g * math.cos(math.radians(_theta)) / self._inertia
      else:
            return _theta - self._g * math.cos(math.radians(_theta)) / self._inertia
      # Add more models
   def update_speed(self,_theta,_v):
      if _theta >= 0.0:
            return _v + self._impulse / self._mass - self._g * math.cos(math.radians(_theta))
      else: 
            return _v + self._impulse / self._mass + self._g * math.cos(math.radians(_theta))
   

x = 0.0
y = 1.0
v = 1000.0

theta_radian = math.radians(45.0) # input degree
limit_upper = 100

print("Launcher : pos0(",x , y ,", A.O.A :", math.degrees(theta_radian) ,"deg) first_velo", v ," \n will iterate", limit_upper ,"times...\nHit Some Key plz $")

hoge = input()

plt.axes().set_aspect('equal', 'datalim') # set 1:1 graph ratio
m = Missile(1,10,9.8,1000)
for num in range(limit_upper):

   v = m.update_speed(theta_radian, v)
   x = m.update_x(x, v, theta_radian)
   y = m.update_y(y, v, theta_radian)

   theta_radian = m.update_theta(theta_radian)

   plt.plot(x, y, color="k", marker="x")
   print("loop ...",num)
   print("x:",x ,end='')
   print(", y:",y)
   print("flight path angle degree:",math.degrees(math.atan(math.sqrt(x*x+y*y))))
   print(", AOA degree:",math.degrees(theta_radian))
   if num == limit_upper or y < 0:
      break
print("Simulation terminated.")
print("Launcher : pos_term(",x , y ,", A.O.A :", math.degrees(theta_radian) ,"deg) first_velo", v )
plt.show()

