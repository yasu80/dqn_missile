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
      # theta must be angle of attack for ground plane; g for earth 
   def update_x(self,_x, _v,_theta):
      return _v * math.cos(_theta)
   def update_y(self,_y, _v,_theta):
      return _v * math.sin(_theta)
   def update_theta(self,_theta):
      # give _theta degree
      if (_theta >= 360):
            _theta = _theta % 360
      elif (_theta <= -360):
            _theta = _theta % 360 * -1
      if _theta >= 270:
            return - self._g * math.cos(_theta) / self._inertia
      elif _theta >= 180:                                                         
            return self._g * math.cos(_theta) / self._inertia
      elif _theta >= 90:                                                          
            return self._g * math.cos(_theta) / self._inertia
      elif _theta >= 0.0:                                                                       
            return - self._g * math.cos(_theta) / self._inertia
      elif _theta >= -90:
            return - self._g * math.cos(_theta) / self._inertia
      elif _theta >= -180:                                                         
            return self._g * math.cos(_theta) / self._inertia
      elif _theta >= -270:                                                         
            return self._g * math.cos(_theta) / self._inertia
      elif _theta >= -360:                                                         
            return - self._g * math.cos(_theta) / self._inertia
      else:
            return - self._g * math.cos(_theta) / self._inertia
      # Add more models
   def update_speed(self,_theta,_v):
      if _theta >= 0.0:
            return self._impulse / self._mass - self._g * math.cos(_theta)
      else: 
            return self._impulse / self._mass + self._g * math.cos(_theta)
   

x = 10.0
y = 10.0
g = 9.8
v = 100.0

#resolution = 0.0001
resolution = 0.001

theta_radian = math.radians(20.0) # input degree
limit_upper = 1000

print("Launcher : pos0(",x , y ,", A.O.A :", math.degrees(theta_radian) ,"deg) first_velo", v ," \n will iterate", limit_upper ,"times...\nHit Some Key plz $")

hoge = input()

plt.axes().set_aspect('equal', 'datalim') # set 1:1 graph ratio

mass = 0.1
inertia = 1
impulse = 1000


m = Missile(mass,inertia, g, impulse)
for num in range (limit_upper):

   v = v + m.update_speed(theta_radian, v) * resolution
   x = x + m.update_x(x, v, theta_radian) * resolution
   y = y + m.update_y(y, v, theta_radian) * resolution

   theta_radian = theta_radian + m.update_theta(theta_radian) * resolution

   plt.plot(x, y, color="k", marker="x")
   print("loop ...",num)
   print("x:",x ,end='')
   print(", y:",y)
   #print("flight path angle degree:",math.degrees(math.atan(math.sqrt(x*x+y*y))))
   #print("flight path angle degree:",math.degrees(theta_radian)
   
   #print(", AOA degree:",math.degrees(theta_radian))
   print(", AOA degree:",math.degrees(theta_radian))
   if num == limit_upper or y < 0:
      break
print("Simulation terminated.")
print("Launcher : pos_term(",x , y ,", A.O.A :", math.degrees(theta_radian) ,"deg) first_velo", v )
plt.show()
