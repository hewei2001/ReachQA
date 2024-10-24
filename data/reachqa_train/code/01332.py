import numpy as np
import matplotlib.pyplot as plt

# Define the years from 2100 to 2140 with increments of 5 years
years = np.array([2100, 2105, 2110, 2115, 2120, 2125, 2130, 2135, 2140])

# Define the hypothetical population data (in thousands)
population = np.array([50, 65, 80, 100, 125, 160, 190, 230, 280])

# Calculate the growth rate as percentage
growth_rate = np.diff(population) / population[:-1] * 100
growth_rate = np.insert(growth_rate, 0, 0)  # Prepend zero for the first year

# Create a color gradient for the population line
colors = plt.cm.viridis(np.linspace(0, 1, len(years)))

# Create the figure and axes with dual y-axes
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

# Plot the population growth with color gradient
for i in range(len(years)-1):
    ax1.plot(years[i:i+2], population[i:i+2], marker='o', color=colors[i], linewidth=3)

# Annotate each point with its population value and change
for i, (year, pop, change) in enumerate(zip(years, population, np.diff(population, prepend=population[0]))):
    offset = 15 if i % 2 == 0 else -25
    ax1.annotate(f'{pop}k\n(+{change}k)', xy=(year, pop), xytext=(0, offset), 
                 textcoords='offset points', fontsize=9, color='darkblue',
                 ha='center', va='bottom' if i % 2 == 0 else 'top',
                 arrowprops=dict(arrowstyle='->', color='gray', lw=0.5, alpha=0.5))

# Plot the growth rate
ax2.plot(years, growth_rate, color='tomato', linewidth=2, linestyle='--', label='Growth Rate (%)')
ax2.scatter(years, growth_rate, color='tomato', s=50)

# Fill between the population line for better visual effect
ax1.fill_between(years, population, color='skyblue', alpha=0.3)

# Add titles and labels
ax1.set_title("Urban Population Growth in Neo-Terra\nfrom 2100 to 2140", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Population (in thousands)", fontsize=12)
ax2.set_ylabel("Growth Rate (%)", fontsize=12)

# Add legends
ax1.legend(['Population Growth'], loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Enable grid for better readability
ax1.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()