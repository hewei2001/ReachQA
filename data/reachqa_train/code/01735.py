import matplotlib.pyplot as plt
import numpy as np

# Define decades
decades = np.array([1990, 2000, 2010, 2020])

# Artificial data for renewable energy contribution in percentage
solar = np.array([0.5, 1.5, 5, 10])     # Steady increase as technology improves
wind = np.array([1, 2.5, 7, 15])        # Significant growth due to tech advancements
hydro = np.array([6, 8, 9, 10])         # Stable with slight increase over time
bioenergy = np.array([2, 3, 4, 5])      # Gradual increase with improved technology

# Stacked data for plotting
data = np.vstack([solar, wind, hydro, bioenergy])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(decades, data, labels=['Solar', 'Wind', 'Hydro', 'Bioenergy'],
             colors=['#FFD700', '#1E90FF', '#32CD32', '#8B4513'], alpha=0.8)

# Title and labels
ax.set_title('Global Shift Towards Renewable Energy:\nContributions to Energy Mix (1990-2020)', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Percentage of Global Energy Mix', fontsize=12)

# Adding grid lines for clarity
ax.grid(True, linestyle='--', alpha=0.7)

# Background color
ax.set_facecolor('#f0f8ff')

# Configure x-ticks to avoid overlap
ax.set_xticks(decades)
ax.set_xticklabels([str(year) for year in decades], rotation=45)

# Enhance readability by setting y-ticks with more steps
ax.set_yticks(np.arange(0, 31, 5))

# Adding annotations for key trends
for i, year in enumerate(decades):
    ax.text(year, np.sum(data[:, i]) + 1, f"{int(np.sum(data[:, i]))}%",
            fontsize=10, ha='center', va='bottom', fontweight='bold')

# Adjust layout to prevent overlap
plt.tight_layout()

# Legend configuration
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Display the plot
plt.show()