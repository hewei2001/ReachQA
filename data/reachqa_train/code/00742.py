import matplotlib.pyplot as plt
import numpy as np

# Galaxies
galaxies = ['Milky Way', 'Andromeda', 'Triangulum', 'Messier 81', 'NGC 300']

# Semesters
semesters = np.array(['Sem 1', 'Sem 2', 'Sem 3', 'Sem 4'])

# Resource utilization data for each galaxy over the semesters
energy_crystals = np.array([
    [120, 150, 160, 140],
    [110, 130, 150, 145],
    [90, 100, 110, 120],
    [85, 95, 105, 115],
    [130, 160, 170, 160]
])

quantum_circuits = np.array([
    [90, 80, 85, 70],
    [100, 90, 95, 80],
    [110, 100, 95, 105],
    [95, 85, 80, 75],
    [120, 110, 115, 105]
])

neutronium_alloys = np.array([
    [100, 110, 120, 130],
    [80, 90, 100, 110],
    [85, 95, 100, 90],
    [90, 85, 95, 105],
    [95, 105, 115, 125]
])

# Bar width
width = 0.5
colors = ['#4CAF50', '#2196F3', '#FFC107']  # Colors for each resource

# 3D Bar Plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot each resource as a stack for each galaxy
for g_index, galaxy in enumerate(galaxies):
    xpos = np.arange(len(semesters))
    ypos = np.full(len(semesters), g_index)
    zpos = np.zeros(len(semesters))

    # Stack resources for each galaxy
    ax.bar3d(xpos, ypos, zpos, width, width, energy_crystals[g_index], color=colors[0], alpha=0.8, label='Energy Crystals' if g_index == 0 else "")
    ax.bar3d(xpos, ypos, energy_crystals[g_index], width, width, quantum_circuits[g_index], color=colors[1], alpha=0.8, label='Quantum Circuits' if g_index == 0 else "")
    ax.bar3d(xpos, ypos, energy_crystals[g_index] + quantum_circuits[g_index], width, width, neutronium_alloys[g_index], color=colors[2], alpha=0.8, label='Neutronium Alloys' if g_index == 0 else "")

# Labeling
ax.set_xlabel('Semesters', labelpad=15)
ax.set_ylabel('Galaxies', labelpad=15)
ax.set_zlabel('Resources Used (Units)', labelpad=15)
ax.set_title('Galactic Resource Utilization\nby Starfleet Academies Across the Universe', pad=20)

# Ticks and labels
ax.set_xticks(np.arange(len(semesters)))
ax.set_xticklabels(semesters, rotation=30, ha='right')
ax.set_yticks(np.arange(len(galaxies)))
ax.set_yticklabels(galaxies)
ax.set_zlim(0, 500)

# Viewing angle for clarity
ax.view_init(elev=25, azim=35)

# Add legend
ax.legend(loc='upper left', bbox_to_anchor=(0.75, 1), title='Resources')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()