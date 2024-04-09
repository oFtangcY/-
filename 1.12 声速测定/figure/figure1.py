import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import make_interp_spline

x_h = np.array([8.328, 13.232, 18.200, 22.901, 27.312, 31.793, 36.140])
U_pp_h = np.array([3.54, 3.10, 2.86, 2.50, 2.30, 1.98, 1.82])

x_h = np.array(x_h).astype(int)
for a,b in zip(x_h, U_pp_h):
    plt.text(a,b,b, ha='center', va='bottom')
plt.scatter(x_h, U_pp_h, marker='o', s = 30,c ='r')

poly = np.polyfit(x_h, U_pp_h, deg=2)
y_value = np.polyval(poly, x_h)
line1, = plt.plot(x_h, y_value, ':r', label = 'High crest')

x_l = np.array([10.692, 15.087, 19.792, 24.472, 29.109, 33.569, 33.729, 33.889])
U_pp_l = np.array([2.46, 2.16, 1.88, 1.64, 1.46, 1.26, 1.26, 1.26])

x_l = np.array(x_l).astype(int)
for a,b in zip(x_l, U_pp_l):
    plt.text(a,b,b, ha='center', va='bottom')
plt.scatter(x_l, U_pp_l, marker='s', s = 30,c ='b')

poly = np.polyfit(x_l, U_pp_l, deg=2)
y_value = np.polyval(poly, x_l)
line2, = plt.plot(x_l, y_value, ':b', label ='Low crest')

plt.title(r'Figure 1  Amplitude Decay Curve: $U_{pp}-x$', size = 20)
plt.xlabel('x/mm')
plt.ylabel(r"$U_{pp}/V$")


ax = plt.subplot()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position(('data',0))

plt.xlim(1, 40)
plt.ylim(-2, 6)

plt.legend(handles=[line1, line2], labels=['High crest','Low crest'], loc='best')

plt.show()