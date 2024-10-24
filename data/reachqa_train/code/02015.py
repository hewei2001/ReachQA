import matplotlib.pyplot as plt
import numpy as np

# Expanded data for household energy consumption in kWh per month
np.random.seed(0)  # Ensure reproducibility

# Data generated with different means and variances for complexity
data = {
    'Urban Apartments': np.random.normal(320, 30, 100),
    'Rural Single-Family Homes': np.random.normal(620, 50, 100),
    'Urban Single-Family Homes': np.random.normal(500, 40, 100),
    'Rural Apartments': np.random.normal(390, 35, 100),
    'Eco-Friendly Homes': np.random.normal(200, 20, 100),
    'Suburban Homes': np.random.normal(550, 45, 100),
    'Smart Homes': np.random.normal(300, 25, 100)
}

labels = list(data.keys())
consumption_data = list(data.values())

# Create a horizontal box plot
fig, ax = plt.subplots(figsize=(12, 8))
box = ax.boxplot(consumption_data, patch_artist=True, vert=False, notch=True,
                 boxprops=dict(color='darkblue', linewidth=1.5),
                 whiskerprops=dict(color='darkblue', linewidth=1.5),
                 capprops=dict(color='darkblue', linewidth=1.5),
                 medianprops=dict(color='red', linewidth=2))

# Color configuration
colors = ['#b3cde3', '#6497b1', '#005b96', '#03396c', '#011f4b', '#7b68ee', '#4682b4']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add mean markers
means = [np.mean(d) for d in consumption_data]
ax.scatter(means, range(1, len(means) + 1), color='gold', marker='D', label='Mean')

# Add grid and labels
ax.set_title('Complex Energy Consumption Patterns:\nAnalyzing Diverse Household Energy Usage', 
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Energy Consumption (kWh per month)', fontsize=12)
ax.set_ylabel('Household Type', fontsize=12)
ax.set_yticklabels(labels, fontsize=10)
ax.grid(True, linestyle='--', alpha=0.7)

# Add legend
ax.legend(loc='upper right', fontsize=10)

# Dual axis: Simulated energy cost plot
ax2 = ax.twiny()
cost_multiplier = 0.12  # Simulated cost per kWh
energy_cost_data = [d * cost_multiplier for d in consumption_data]
ax2.boxplot(energy_cost_data, patch_artist=False, vert=False, widths=0.5)
ax2.set_xlabel('Energy Cost (USD per month)', fontsize=12)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()