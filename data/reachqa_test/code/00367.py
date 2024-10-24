import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Age groups
age_groups = ['18-24', '25-34', '35-44', '45-54', '55+', '65+']

# Music genres
genres = ['Rock', 'Pop', 'Hip-Hop', 'Electronic', 'Jazz', 'Classical']

# Average attendance data
attendance = np.array([
    [1200, 800, 600, 400, 200, 100],  # 18-24
    [1500, 1000, 800, 600, 400, 200],  # 25-34
    [1000, 800, 600, 400, 200, 150],  # 35-44
    [800, 600, 400, 200, 150, 100],  # 45-54
    [400, 200, 100, 50, 20, 10],  # 55+
    [200, 100, 50, 20, 10, 5]  # 65+
])

fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(genres)):
    ax.bar3d(np.arange(len(age_groups)), [i]*len(age_groups), np.zeros(len(age_groups)), 
             1, 1, attendance[:, i], color=plt.cm.tab20(i/len(genres)), alpha=0.7)

ax.set_xlabel('Age Groups')
ax.set_ylabel('Music Genres')
ax.set_zlabel('Average Attendance')

ax.set_xticks(np.arange(len(age_groups)))
ax.set_xticklabels(age_groups, rotation=45, ha='right', fontsize=8)

ax.set_yticks(np.arange(len(genres)))
ax.set_yticklabels(genres, fontsize=8)

ax.view_init(30, 60)

plt.title("Average Music Festival Attendance by Age Group and Genre\n"
          "(Color corresponds to Music Genre)\n"
          "Note: The attendance is highest for Rock and Pop music")

plt.tight_layout()
plt.show()