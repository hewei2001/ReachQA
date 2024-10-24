import matplotlib.pyplot as plt
import numpy as np

# Define decades
decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])

# Artificial data for gas composition in percentage
hydrogen = np.array([80, 78, 75, 72, 70, 68, 65])   # Decreasing trend
helium = np.array([18, 19, 20, 22, 24, 25, 27])      # Increasing trend
other_gases = np.array([2, 3, 5, 6, 6, 7, 8])        # Slight increase

# Stacked data for plotting
data = np.vstack([hydrogen, helium, other_gases])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(decades, data, labels=['Hydrogen', 'Helium', 'Other Gases'], colors=['#a6cee3', '#1f78b4', '#b2df8a'])

# Title and labels
ax.set_title('Galactic Observation Program:\nInterstellar Gas Composition Over Time', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Percentage Composition', fontsize=12)

# Legend and grid
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
ax.grid(True, linestyle='--', alpha=0.7)

# Background color
ax.set_facecolor('#f0f0f0')

# Configure x-ticks to avoid overlap
ax.set_xticks(decades)
ax.set_xticklabels([str(year) for year in decades], rotation=45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()