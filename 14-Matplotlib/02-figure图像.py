import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-1, 1, 50)
y1 = 2*x + 1
y2 = x**2 + 1

plt.figure()
plt.plot(x, y1)

plt.figure(figsize=(8, 5))  # 长8 宽5
plt.plot(x, y2)
plt.plot(x, y1, color="red", linewidth=1.0, linestyle="--")

plt.show()
