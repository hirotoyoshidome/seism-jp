import numpy as np
from scipy import integrate


dt = 0.01
y = lambda x: np.sin(x) ** 2

integ = integrate.quad(y, 0, np.pi)

print(integ)
