import matplotlib.pyplot as plt
import numpy as np

# Cities and energy sources
cities = ['New York', 'Tokyo', 'Berlin', 'Sydney', 'Cape Town']
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Biomass']

# Data: percentage adoption of each energy source by city
adoption_data = [
    [30, 10, 15, 5],   # New York
    [20, 25, 10, 5],   # Tokyo
    [15, 40, 20, 10],  # Berlin
    [25, 15, 30, 10],  # Sydney
    [35, 5, 10, 20]    # Cape Town
]

# Colors for each energy source
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Define positions for each group of bars
bar_width = 0.15
index = np.arange(len(cities))

# Plot each energy source
for i, (energy_source, color) in enumerate(zip(energy_sources, colors)):
    bars = ax.bar(index + i * bar_width, [data[i] for data in adoption_data],
                  bar_width, label=energy_source, color=color)

    # Add text labels above bars
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}%',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # Offset text above the bar
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold')

# Add labels and title
ax.set_xlabel('Cities', fontsize=12)
ax.set_ylabel('Adoption Percentage (%)', fontsize=12)
ax.set_title('The Dawn of Eco-Urbanism:\nRenewable Energy Adoption in Metropolitan Areas', fontsize=14, fontweight='bold', pad=15)

# Set x-ticks and labels
ax.set_xticks(index + 1.5 * bar_width)
ax.set_xticklabels(cities, fontsize=11)
ax.set_ylim(0, 50)

# Add grid lines to y-axis
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Add a legend
ax.legend(title='Energy Sources', fontsize=10, title_fontsize='12', loc='upper right')

# Automatically adjust layout for better fit
plt.tight_layout()

# Show plot
plt.show()