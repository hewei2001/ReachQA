import numpy as np
import matplotlib.pyplot as plt

# Define attributes for the radar chart
attributes = ['Fuel Efficiency', 'Cargo Capacity', 'Shield Strength', 'Speed', 'Durability']

# Data for each spacecraft
voyager_x = [8, 7, 6, 9, 8]
galaxy_explorer = [6, 8, 7, 8, 7]
stellar_pioneer = [9, 6, 8, 7, 9]
cosmos_crusader = [7, 9, 9, 6, 8]

# Organize data
data = np.array([voyager_x, galaxy_explorer, stellar_pioneer, cosmos_crusader])

# Number of variables
num_vars = len(attributes)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Complete the loop for plotting
data = np.concatenate((data, data[:, [0]]), axis=1)
angles += angles[:1]

# Set up the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Color palette for each spacecraft
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Plot each spacecraft
for i, spacecraft_data in enumerate(data):
    ax.fill(angles, spacecraft_data, color=colors[i], alpha=0.25)
    ax.plot(angles, spacecraft_data, label=f'{["Voyager X", "Galaxy Explorer", "Stellar Pioneer", "Cosmos Crusader"][i]}', color=colors[i], linewidth=2)

# Add attribute labels
plt.xticks(angles[:-1], attributes, color='grey', size=10)

# Add y-labels
ax.set_rlabel_position(30)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
plt.ylim(0, 10)

# Title with multiple lines for better visibility
plt.title("Interstellar Voyage Preparation Analysis:\nSpacecraft Attributes Evaluation", size=16, weight='bold', position=(0.5, 1.1), ha='center')

# Add a legend
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()