import matplotlib.pyplot as plt
import numpy as np

# Define the time periods
eras = ['Ancient Era\n(5000 BC)', 'Medieval Era\n(1000 AD)', 'Industrial Revolution\n(1800)', 'Modern Era\n(2020)']

# Approximate dietary composition percentages for each era
proteins = [10, 15, 20, 25]
carbohydrates = [50, 40, 35, 30]
fats = [15, 20, 25, 30]
vegetables = [25, 25, 20, 15]

# Stack the data
data = np.array([proteins, carbohydrates, fats, vegetables])

# Convert eras to a numerical range for plotting
x = np.arange(len(eras))

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the stacked area chart
ax.stackplot(x, data, labels=['Proteins', 'Carbohydrates', 'Fats', 'Vegetables'],
             colors=['#d62728', '#ff7f0e', '#2ca02c', '#1f77b4'], alpha=0.8)

# Customize the plot
ax.set_title('The Evolution of Culinary Cultures\nThrough the Ages', fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Time Period', fontsize=12)
ax.set_ylabel('Dietary Composition (%)', fontsize=12)
ax.set_xlim(0, len(eras) - 1)
ax.set_ylim(0, 100)
ax.set_xticks(x)
ax.set_xticklabels(eras, rotation=30, ha='right', fontsize=10)

# Add grid and legend
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title="Food Components")

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()