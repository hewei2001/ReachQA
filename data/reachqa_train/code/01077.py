import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Define decades
decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])

# Artificial data for gas composition in percentage
hydrogen = np.array([80, 78, 75, 72, 70, 68, 65])   # Decreasing trend
helium = np.array([18, 19, 20, 22, 24, 25, 27])     # Increasing trend
other_gases = np.array([2, 3, 5, 6, 6, 7, 8])       # Slight increase

# Stacked data for plotting
data = np.vstack([hydrogen, helium, other_gases])

# Create figure and axes
fig, ax = plt.subplots(figsize=(14, 8))

# Use a seaborn color palette for better aesthetics
colors = sns.color_palette('pastel', n_colors=3)

# Plotting the stacked area chart with transparency
ax.stackplot(decades, data, labels=['Hydrogen', 'Helium', 'Other Gases'], colors=colors, alpha=0.8)

# Title and labels
ax.set_title('Galactic Observation Program:\nInterstellar Gas Composition Over Time', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Percentage Composition (%)', fontsize=12)

# Annotations for maximum and minimum values
ax.annotate('Min Hydrogen', xy=(2020, 65), xytext=(2000, 70), 
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax.annotate('Max Helium', xy=(2020, 27), xytext=(2000, 30), 
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Legend customization
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, frameon=False)

# Grid lines
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7, which='both')

# Axes background color with a slight gradient effect
ax.set_facecolor('#e8f4f8')

# Configure x-ticks
ax.set_xticks(decades)
ax.set_xticklabels([str(year) for year in decades], rotation=45)

# Ensure no overlap using tight layout
plt.tight_layout()

# Display the plot
plt.show()