import numpy as np
import matplotlib.pyplot as plt

# Define the years from 2100 to 2140 with increments of 5 years
years = np.array([2100, 2105, 2110, 2115, 2120, 2125, 2130, 2135, 2140])

# Define the hypothetical population data (in thousands)
population = np.array([50, 65, 80, 100, 125, 160, 190, 230, 280])

# Calculate the change in population for annotation purposes
population_change = np.diff(population, prepend=population[0])

# Create the figure and plot
plt.figure(figsize=(12, 8))
plt.plot(years, population, marker='o', color='royalblue', linewidth=2, markersize=8, linestyle='-', label='Population Growth')

# Annotate each point with its population value and change
for i, (year, pop, change) in enumerate(zip(years, population, population_change)):
    # Choose position offset based on index to avoid overlapping
    xytext_offset = (0, 10 if i % 2 == 0 else -15)
    plt.annotate(f'{pop}k\n(+{change}k)', xy=(year, pop), xytext=xytext_offset,
                 textcoords='offset points', fontsize=9, color='darkblue',
                 ha='center', va='bottom' if i % 2 == 0 else 'top',
                 arrowprops=dict(arrowstyle='->', color='gray', lw=0.5, alpha=0.5))

# Add title, labels, and legend
plt.title("Urban Population Growth in Neo-Terra\nfrom 2100 to 2140", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Population (in thousands)", fontsize=12)
plt.legend(loc='upper left', fontsize=10)

# Enable grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()