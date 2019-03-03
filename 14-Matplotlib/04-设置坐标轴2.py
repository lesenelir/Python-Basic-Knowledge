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

plt.xlim(-1, 2)  # 取值范围
plt.ylim(-2, 3)

new_ticks = np.linspace(-1, 2, 5)
# print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1, 0, 1, 3],
           ["really bad", "bad", "normal", "good", "really good"])

# gca = "get current axis"
ax = plt.gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))

plt.show()
