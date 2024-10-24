import matplotlib.pyplot as plt
import numpy as np

# Define decades and contributions
decades = np.arange(1960, 2030, 10)

# Contribution by each field over the decades
computing = [10, 20, 40, 60, 80, 90, 100]  # Steep growth in recent years
biotechnology = [5, 10, 25, 35, 55, 75, 85]  # Rapid rise in the 2000s
renewable_energy = [3, 5, 15, 30, 50, 70, 80]  # Consistent growth, peaks in recent times
space_exploration = [8, 15, 25, 20, 30, 35, 45]  # Early growth with resurgence in recent decades

# Stack data for plotting
data = np.vstack([computing, biotechnology, renewable_energy, space_exploration])

# Define distinct colors for each field
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(decades, data, labels=['Computing', 'Biotechnology', 'Renewable Energy', 'Space Exploration'], colors=colors, alpha=0.8)

# Add titles and labels
ax.set_title('Evolution of Technological Influence\nby Sector (1960-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Contribution to Technological Advancements', fontsize=12)

# Add grid and legend
ax.grid(linestyle='--', alpha=0.5)
ax.legend(loc='upper left', title='Technology Sectors', fontsize=10)

# Annotations for significant points or changes
ax.annotate('Rapid Computing Growth', xy=(2000, 160), xytext=(1975, 180),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, bbox=dict(facecolor='white', edgecolor='white', boxstyle='round,pad=0.5'))

ax.annotate('Rise of Biotechnology', xy=(2010, 230), xytext=(1990, 250),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, bbox=dict(facecolor='white', edgecolor='white', boxstyle='round,pad=0.5'))

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()