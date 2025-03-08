from utils import solve_system, get_system_matrix_from_csv
import  matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

system_matrix = get_system_matrix_from_csv('input.csv')
# x,y are values
# if i have the list of coeficients i could perform... element wise mul, then sum :D

labels = []
def plane(x, y, eqNo):
    a, b, c, d = system_matrix[eqNo, :]
    labels.append(f"Plane {eqNo}: {a}x + {b}y + {c}z = {d}")
    return (d - a * x - b * y) / c

dim = 100
zAxLim = int(dim / 2)
xyAxLim = 10

x = np.linspace(-xyAxLim, xyAxLim, dim)
y = np.linspace(-xyAxLim, xyAxLim, dim)
x, y = np.meshgrid(x, y)

z1 = plane(x, y, 0)
z2 = plane(x, y, 1)
z3 = plane(x, y, 2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z1, alpha=0.5, rstride=100, cstride=100, color='red', label=labels[0])
ax.plot_surface(x, y, z2, alpha=0.5, rstride=100, cstride=100, color='blue', label=labels[1])
ax.plot_surface(x, y, z3, alpha=0.5, rstride=100, cstride=100, color='green', label=labels[2])

x0, y0, z0 = solve_system(system_matrix, True)
ax.scatter(x0, y0, z0, label=f"Intersection Point ({x0:.2f}, {y0:.2f}, {z0:.2f})")
ax.text(x0, y0, z0, f"({x0:.2f}, {y0:.2f}, {z0:.2f})", color='black', fontsize=12)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.legend(loc='upper left', bbox_to_anchor=(1, 1), frameon=False)
plt.show()

#  homework: can i highlight where two planes meet? a line along them :D