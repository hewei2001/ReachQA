import matplotlib.pyplot as plt
import numpy as np

# Define regions
regions = ['North America', 'Europe', 'Asia', 'Africa', 'South America']

# Define dietary preference data (% of population)
vegetarian = np.array([15, 20, 10, 5, 12])
vegan = np.array([5, 10, 5, 2, 4])
pescatarian = np.array([10, 15, 10, 3, 8])
flexitarian = np.array([20, 25, 15, 10, 18])
omnivorous = np.array([50, 30, 60, 80, 58])

# Stack data for plotting
diet_data = np.vstack([vegetarian, vegan, pescatarian, flexitarian, omnivorous])

# Define colors for each dietary type
colors = ['#FFB6C1', '#7FFFD4', '#6495ED', '#FFD700', '#FF6347']

# Plotting setup
fig, ax = plt.subplots(figsize=(12, 8))

# Create a stacked bar chart
width = 0.6
for i in range(len(diet_data)):
    ax.barh(regions, diet_data[i], width, left=np.sum(diet_data[:i], axis=0), color=colors[i])

# Add labels, title and customize ticks
ax.set_title('Global Dietary Preference Adoption Rates\nA Decade of Change', fontsize=16, fontweight='bold')
ax.set_xlabel('Percentage of Population (%)', fontsize=12)
ax.set_xlim(0, 100)
ax.set_xticks(np.arange(0, 101, 10))

# Add a legend
ax.legend(['Vegetarian', 'Vegan', 'Pescatarian', 'Flexitarian', 'Omnivorous'], loc='lower left', bbox_to_anchor=(1, 0.5))

# Directly label each segment with its percentage value
for i, region_data in enumerate(diet_data.T):
    left = 0
    for j, value in enumerate(region_data):
        if value > 0:
            ax.text(left + value / 2, i, f'{value}%', va='center', ha='center', color='black', fontsize=10)
        left += value

# Ensure layout is tight
plt.tight_layout()

# Show the plot
plt.show()