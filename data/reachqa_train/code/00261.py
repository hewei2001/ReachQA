import matplotlib.pyplot as plt
import numpy as np

# Define categories and household data
categories = ['Energy\nConsumption', 'Waste\nReduction', 'Water\nUsage', 'Transport\nHabits', 'Green\nPurchases']
household_data = {
    'Household A': [7, 9, 8, 6, 7],
    'Household B': [8, 6, 7, 9, 8],
    'Household C': [6, 7, 9, 8, 6],
    'Household D': [5, 8, 6, 7, 9],
}

# Number of variables
num_vars = len(categories)

# Compute angle for each category
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # To complete the loop

# Set up radar chart framework
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Compute the average performance and variability
average_data = np.mean([list(household_data.values())[i] for i in range(len(household_data))], axis=0).tolist()
average_data += average_data[:1]
variability = np.std([list(household_data.values())[i] for i in range(len(household_data))], axis=0).tolist()
variability += variability[:1]

# Plot each household's data with filled areas
for household, values in household_data.items():
    values += values[:1]
    ax.plot(angles, values, linewidth=1.5, linestyle='-', label=household)
    ax.fill(angles, values, alpha=0.15)

# Overlay average line with error bars
ax.plot(angles, average_data, linewidth=2, linestyle='--', color='red', label='Average')
ax.errorbar(angles, average_data, yerr=variability, fmt='o', color='red', capsize=5)

# Customize the chart's appearance
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='grey', size=8)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=10, color='teal')

# Title and legend
plt.title('Eco-Friendly Living Habits\nComparison of Four Households and Overall Average', size=16, weight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Automatically adjust layout to fit and show the plot
plt.tight_layout()
plt.show()