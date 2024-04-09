import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import make_interp_spline

x_a = np.array([33.105, 37.446, 42.180, 46.585, 51.110, 55.335, 59.998, 64.398, 68.925, 73.602])
U_pp_a = np.array([15.2, 13.4, 12.6, 11.2, 10.4, 9.2, 8.6, 7.6, 7.0, 6.4])

x_a = np.array(x_a).astype(int)
for a,b in zip(x_a, U_pp_a):
    plt.text(a,b,b, ha='center', va='bottom')
plt.scatter(x_a, U_pp_a, marker='^', s = 30,c ='y')

poly = np.polyfit(x_a, U_pp_a, deg=2)
y_value = np.polyval(poly, x_a)
plt.plot(x_a, y_value, ':y')

plt.title(r"Figure 2  Amplitude Decay Curve: $U'_{pp}-x'$", size = 20)
plt.xlabel(r"$x'/mm$")
plt.ylabel(r"$U'_{pp}/V$")

ax = plt.subplot()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position(('data',0))

plt.xlim(1, 80)
plt.ylim(-10, 20)

plt.show()