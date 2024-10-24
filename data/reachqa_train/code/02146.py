import numpy as np
import matplotlib.pyplot as plt

# Define celestial influence attributes
attributes = [
    'Diplomacy',
    'Military Strategy',
    'Economic Development',
    'Tech Advancements',
    'Cultural Richness',
    'Environmental Policies'
]

num_vars = len(attributes)

# Galactic regions with their attribute values influenced by celestial bodies
alpha_quadrant = [6, 7, 8, 5, 9, 6]
beta_sector = [7, 6, 5, 8, 7, 8]
gamma_galaxy = [8, 5, 7, 9, 6, 7]
delta_zone = [5, 8, 6, 7, 8, 5]
epsilon_sphere = [7, 7, 8, 6, 5, 9]

# Organize data into an array for easy plotting
data = np.array([alpha_quadrant, beta_sector, gamma_galaxy, delta_zone, epsilon_sphere], dtype=float)

# Normalize data to [0, 1] range for radar chart
data /= 10.0

# Calculate angles for radar chart (one per attribute)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Repeat the first angle to close the radar chart
data = np.concatenate((data, data[:, [0]]), axis=1)
angles += angles[:1]

# Create the radar chart with area fill
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

# Define colors for each region
colors = ['#FF5733', '#33FF57', '#3357FF', '#F0FF33', '#33FFF0']
regions = ['Alpha Quadrant', 'Beta Sector', 'Gamma Galaxy', 'Delta Zone', 'Epsilon Sphere']

# Plot data with filled areas
for i, color in enumerate(colors):
    ax.fill(angles, data[i], color=color, alpha=0.25, label=regions[i])
    ax.plot(angles, data[i], color=color, linewidth=2)

# Setup radar chart properties
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=10)
ax.set_title("Astral Influences on Galactic Politics\nin Stellaris Nova", size=14, pad=20, fontweight='bold')
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.7)
ax.xaxis.grid(True, linestyle='--', color='grey', alpha=0.7)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=9, title="Galactic Regions")

# Adjust layout for readability
plt.tight_layout()

# Display the plot
plt.show()