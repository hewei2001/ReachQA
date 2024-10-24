import matplotlib.pyplot as plt
import numpy as np

# Cities and transportation modes
cities = ['EcoCity', 'GreenTown', 'CycleVille', 'SustainableCity', 'CleanAirDistrict']
transport_modes = ['Bicycles', 'Electric Scooters', 'Walking', 'Public Transport', 'Cars']

# Construct the data for each city
transport_data = np.array([
    [25, 15, 20, 30, 10],  # EcoCity
    [20, 20, 30, 20, 10],  # GreenTown
    [30, 25, 15, 20, 10],  # CycleVille
    [15, 10, 25, 40, 10],  # SustainableCity
    [20, 10, 20, 30, 20],  # CleanAirDistrict
])

# Plotting the data
fig, ax = plt.subplots(figsize=(12, 8))

# Define colors for the transport modes
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Set bar positions and width
x = np.arange(len(cities))
bar_width = 0.15

# Plot each city's data as a grouped bar
for i, (mode, color) in enumerate(zip(transport_modes, colors)):
    bars = ax.bar(x + i * bar_width, transport_data[:, i], width=bar_width, label=mode, color=color, edgecolor='grey', alpha=0.8)

    # Add data labels
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}%',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # Offset label position
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

# Title and axis labels
ax.set_title('The Rise of Eco-Friendly Transportation\nin Urban Areas', fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Cities', fontsize=12)
ax.set_ylabel('Percentage (%)', fontsize=12)
ax.set_xticks(x + bar_width * 2)
ax.set_xticklabels(cities, rotation=20, ha='right')

# Add legend
ax.legend(title='Transport Modes', title_fontsize='13', loc='upper right')

# Add gridlines
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()