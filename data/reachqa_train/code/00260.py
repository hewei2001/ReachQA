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

# Repeat the first angle to close the radar chart loop
angles += angles[:1]

# Set up radar chart framework
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each household's data on the radar chart
for household, values in household_data.items():
    values += values[:1]  # Repeat the first value to close the loop
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=household)
    ax.fill(angles, values, alpha=0.25)

# Customize the chart's appearance
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='grey', size=8)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=10, color='teal')

# Title and legend
plt.title('Eco-Friendly Living Habits\nComparison of Four Households', size=16, weight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Automatically adjust layout to fit and show the plot
plt.tight_layout()
plt.show()