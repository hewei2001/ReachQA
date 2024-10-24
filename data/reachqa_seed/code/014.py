import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import Normalize
from matplotlib.markers import MarkerStyle
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D

SUCCESS_SYMBOLS = [
    TextPath((0, 0), "☹"),
    TextPath((0, 0), "😒"),
    TextPath((0, 0), "☺"),
]

N = 15

skills = np.array([8.3, 12.6, 11.0, 10.0, 6.7, 6.7, 5.9, 12.0, 10.0, 10.8, 5.7, 12.8, 11.7, 7.1, 6.9])
takeoff_angles = np.array([-51.4, -83.2, -235.1, 85.5, 73.5, -137.1, -38.5, -66.8, -63.3, -192.6, -56.7, 53.8, 230.4, 35.5, 11.0])
thrusts = np.array([0.2, 0.1, 0.9, 1.0, 0.8, 0.3, 0.1, 0.7, 0.4, 0.1, 0.5, 0.0, 0.9, 0.3, 0.7])
successful = np.array([1, 1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1, 1, 2])
positions = np.array([[-2.6, -5.0], [-7.9, 3.9], [-2.7, -6.7], [-4.4, -5.7], [0.7, 2.9], [4.4, 4.5], [3.8, -1.0], [-3.1, -7.5], [5.5, -0.9], [-2.1, 5.9], [-4.5, 4.2], [1.5, -5.2], [-0.4, 4.9], [4.0, 7.5], [1.7, 6.9]])

data = zip(skills, takeoff_angles, thrusts, successful, positions)

cmap = plt.get_cmap("plasma")
fig, ax = plt.subplots()
fig.suptitle("Throwing success", size=14)
for skill, takeoff, thrust, mood, pos in data:
    t = Affine2D().scale(skill).rotate_deg(takeoff)
    m = MarkerStyle(SUCCESS_SYMBOLS[mood], transform=t)
    ax.plot(pos[0], pos[1], marker=m, color=cmap(thrust))
fig.colorbar(plt.cm.ScalarMappable(norm=Normalize(0, 1), cmap=cmap),
             ax=ax, label="Normalized Thrust [a.u.]")

ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])

ax.set_xlabel("X position [m]")
ax.set_ylabel("Y position [m]")

plt.show()
