import matplotlib.pyplot as plt
import numpy as np

# Define marine mammals and dietary components
marine_mammals = ['Dolphins', 'Seals', 'Whales']
diet_components = ['Fish', 'Squid', 'Crustaceans', 'Others']

# Dietary composition data
diet_data = np.array([
    [60, 25, 10, 5],  # Dolphins
    [50, 20, 20, 10], # Seals
    [30, 40, 20, 10], # Whales
])

# Create a color palette for different components
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Create a horizontal percentage bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bottom = np.zeros(len(marine_mammals))

# Plot each component of the diet
for i, (component, color) in enumerate(zip(diet_components, colors)):
    ax.barh(marine_mammals, diet_data[:, i], left=bottom, label=component, color=color, alpha=0.8)
    bottom += diet_data[:, i]

# Add a title and labels
ax.set_title('Dietary Composition of Marine Mammals\nPercentage Breakdown by Food Type', fontsize=14, weight='bold', pad=15)
ax.set_xlabel('Percentage of Total Diet (%)', fontsize=12)
ax.set_xlim(0, 100)

# Adding a legend to identify dietary components
ax.legend(title='Dietary Components', loc='lower right', fontsize=10)

# Add data labels
for i, (diet) in enumerate(diet_data):
    cum_sum = 0
    for j, value in enumerate(diet):
        ax.text(cum_sum + value / 2, i, f'{value}%', ha='center', va='center', fontsize=9, color='white')
        cum_sum += value

# Customize grid and layout
ax.xaxis.grid(True, linestyle='--', alpha=0.5)
ax.set_axisbelow(True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()