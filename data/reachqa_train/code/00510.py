import numpy as np
import matplotlib.pyplot as plt

# Define labels for each coffee attribute
labels = np.array(['Aroma', 'Flavor', 'Acidity', 'Body', 'Aftertaste'])

# Number of variables we're plotting
num_vars = len(labels)

# Define the attributes for each coffee type
espresso = [85, 90, 70, 95, 80]
latte = [75, 85, 60, 80, 70]
cappuccino = [80, 88, 65, 85, 75]
americano = [78, 80, 68, 75, 72]
cold_brew = [70, 78, 80, 70, 85]

# Combine the data for all coffee types
data = np.array([espresso, latte, cappuccino, americano, cold_brew])

# Repeat the first data point to close the radar chart
data = np.concatenate((data, data[:, [0]]), axis=1)

# Calculate angles for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Create radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Colors for each coffee type
colors = ['brown', 'tan', 'sienna', 'gray', 'darkcyan']

# Plot each coffee type with specific colors and transparency
coffee_types = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Cold Brew']
for idx, coffee in enumerate(coffee_types):
    ax.fill(angles, data[idx], color=colors[idx], alpha=0.25, label=coffee)
    ax.plot(angles, data[idx], color=colors[idx], linewidth=2)

# Customization of the chart
ax.set_yticklabels([])  # Remove radial labels for a cleaner look
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=12)

# Title and legend
ax.set_title('Coffee Lover\'s Radar:\nExploring Coffee Characteristics', 
             size=15, color='chocolate', pad=20, weight='bold')
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10)

# Improve layout
plt.tight_layout()

# Show the radar chart
plt.show()