import matplotlib.pyplot as plt
import numpy as np

# Define marine mammals and dietary components
marine_mammals = ['Dolphins', 'Seals', 'Whales']
diet_components = ['Fish', 'Squid', 'Crustaceans', 'Others']

# Dietary composition data (in percentages)
diet_data = np.array([
    [60, 25, 10, 5],  # Dolphins
    [50, 20, 20, 10], # Seals
    [30, 40, 20, 10], # Whales
])

# Hypothetical average nutrient intake data (e.g., in grams per day)
nutrient_data = np.array([
    [80, 70, 90],  # Protein intake for Dolphins, Seals, Whales
    [25, 30, 20],  # Fat intake for Dolphins, Seals, Whales
])

# Create color palettes
diet_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
nutrient_colors = ['#8c564b', '#e377c2']

fig, ax1 = plt.subplots(figsize=(12, 7))
bottom = np.zeros(len(marine_mammals))

# Plot each component of the diet as stacked horizontal bars
for i, (component, color) in enumerate(zip(diet_components, diet_colors)):
    ax1.barh(marine_mammals, diet_data[:, i], left=bottom, label=component, color=color, alpha=0.8)
    bottom += diet_data[:, i]

# Set title and labels for the primary y-axis
ax1.set_title('Dietary Composition and Nutrient Intake of Marine Mammals\nPercentage Breakdown and Average Intake', fontsize=14, weight='bold', pad=20)
ax1.set_xlabel('Percentage of Total Diet (%)', fontsize=12)
ax1.set_xlim(0, 100)

# Adding a legend for diet components
ax1.legend(title='Dietary Components', loc='lower left', fontsize=10)

# Add data labels to the bars
for i, (diet) in enumerate(diet_data):
    cum_sum = 0
    for j, value in enumerate(diet):
        ax1.text(cum_sum + value / 2, i, f'{value}%', ha='center', va='center', fontsize=9, color='white')
        cum_sum += value

# Create secondary y-axis for nutrient intake
ax2 = ax1.twinx()
ax2.set_ylabel('Average Nutrient Intake (grams/day)', fontsize=12, color='dimgray')
ax2.tick_params(axis='y', labelcolor='dimgray')

# Plot nutrient intake data as line plots
nutrient_labels = ['Protein Intake', 'Fat Intake']
for i, (nutrients, color, label) in enumerate(zip(nutrient_data, nutrient_colors, nutrient_labels)):
    ax2.plot(nutrients, marine_mammals, marker='o', color=color, linestyle='-', label=label, linewidth=2, markersize=6)

# Adding a legend for nutrient intake
ax2.legend(title='Nutrient Intake', loc='upper right', fontsize=10)

# Customize grid and layout
ax1.xaxis.grid(True, linestyle='--', alpha=0.5)
ax1.set_axisbelow(True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()