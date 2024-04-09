import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import make_interp_spline

x = np.array([33.105, 37.446, 42.18, 46.585, 51.11, 55.335, 59.998, 64.398, 68.925, 73.602])
y = np.array([15.2, 13.4, 12.6, 11.6, 10.5, 9.6, 8.56, 8.16, 7.36, 6.48])

m = make_interp_spline(x, y)
xs = np.linspace(0, 23, 500)
ys = m(xs)
plt.plot(xs, ys, ':b')

plt.title('Amplitude Decay Curve')
plt.xlabel('x/mm')
plt.ylabel(r"$U_{pp}/V$")

plt.show()