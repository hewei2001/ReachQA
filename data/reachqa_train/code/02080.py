import matplotlib.pyplot as plt
import numpy as np

# Define continents and decades
continents = ['Asia', 'Europe', 'North America', 'South America', 'Africa']
decades = ['2000s', '2010s', '2020s']

# Renewable energy adoption data in gigawatts for each continent over the decades
# Format: [[solar, wind, hydro], ...] for each continent
asia = [[30, 20, 50], [150, 100, 70], [300, 250, 120]]
europe = [[40, 60, 30], [200, 300, 50], [350, 500, 80]]
north_america = [[20, 40, 60], [180, 150, 100], [300, 320, 130]]
south_america = [[10, 10, 80], [50, 70, 90], [100, 150, 140]]
africa = [[5, 5, 20], [25, 30, 40], [80, 110, 60]]

# Compile the data into a list
data = [asia, europe, north_america, south_america, africa]

# Define colors for each energy type
colors = ['#ffdd57', '#76c7c0', '#68a7ad']
sources = ['Solar', 'Wind', 'Hydroelectric']

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Calculate x positions for each continent's bars
bar_width = 0.15
x_positions = np.arange(len(decades))

# Plot each continent's data as stacked bars
for i, continent_data in enumerate(data):
    solar, wind, hydro = np.array(continent_data).T
    
    # Adjust bar positions by offsetting using the bar_width
    x_offset = i * bar_width
    ax.bar(x_positions + x_offset, solar, color=colors[0], label=sources[0] if i == 0 else "", width=bar_width)
    ax.bar(x_positions + x_offset, wind, color=colors[1], label=sources[1] if i == 0 else "", bottom=solar, width=bar_width)
    ax.bar(x_positions + x_offset, hydro, color=colors[2], label=sources[2] if i == 0 else "", bottom=solar + wind, width=bar_width)

    # Adding continent labels on top of the bars
    for j in range(len(decades)):
        ax.text(x_positions[j] + x_offset, np.sum(continent_data[j]), continents[i], ha='center', va='bottom', 
                fontsize=8, weight='bold', rotation=90, color='black', alpha=0.7)

# Configure the plot
ax.set_title('Renewable Energy Adoption Across Continents:\nA Decadal Analysis (2000-2020)', 
             fontsize=16, fontweight='bold')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Adoption (Gigawatts)', fontsize=12)
ax.set_ylim(0, 1000)  # Set y-axis limit for better visibility of stacked bars
ax.set_xticks(x_positions + bar_width * (len(continents) - 1) / 2)
ax.set_xticklabels(decades)

# Add grid for easier comparison
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add legend
ax.legend(loc='upper left', fontsize=10, frameon=False, title='Energy Source', title_fontsize='13')

# Ensure the layout is tight and prevents overlap
plt.tight_layout()

# Show the plot
plt.show()