from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import random


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Data

# X is TC#


def give_x_values(i):
    set_x = []
    for j in range(0, 100):
        set_x.append(i)
    return set_x


X1 = np.array(give_x_values(1))
X2 = np.array(give_x_values(2))
X3 = np.array(give_x_values(3))

# Y is Time
Y = range(0, 100)


# Z is Temp
def rand_temp_set():
    set_z = []
    for j in range(0, 100):
        k = j + random.randint(-10, 10)
        set_z.append(k)
    return set_z


Z1 = np.array(rand_temp_set())
Z2 = np.array(rand_temp_set())
Z3 = np.array(rand_temp_set())

# Plot a basic wireframe.
ax.plot_wireframe(X1, Y, Z1, rstride=10, cstride=10)
ax.plot_wireframe(X2, Y, Z2, rstride=10, cstride=10)
ax.plot_wireframe(X3, Y, Z3, rstride=10, cstride=10)

# Modify axis labels
ax.set_xlabel('TC#')
ax.set_ylabel('Time')
ax.set_zlabel('Temp')
ax.set_xticks([1, 2, 3])



plt.show()
