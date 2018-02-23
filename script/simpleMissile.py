# coding: utf-8
# Python 3.5.2

import matplotlib.pyplot as plt
import math

missile_x = 0.0
missile_y = 0.0
missile_v = 100.0
missile_mass = 10.0
missile_theta = 0.0
missile_inertia = 45

g = 9.81

limit_upper = 100

for num in range(limit_upper):
   missile_x = missile_x + missile_v * math.sin(math.radians(missile_theta))
   missile_y = missile_y + missile_v * math.cos(math.radians(missile_theta))
   missile_theta = missile_theta + missile_inertia * g * math.cos(math.radians(missile_theta))
   plt.plot(missile_x, missile_y, color="k", marker="o")
   print(" x :", missile_x, " y :", missile_y, "th : ", missile_theta)
   if num == limit_upper:
      break
plt.show()
print("terminated.")
