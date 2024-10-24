import matplotlib.pyplot as plt
import numpy as np

# Define the mode of transport and their hypothetical usage percentages
modes_of_transport = [
    'Autonomous Electric Cars',
    'High-Speed Trains',
    'Aerial Drones',
    'Hyperloop Systems',
    'Traditional Public Transit',
    'Biking and Walking'
]

usage_percentages = np.array([35, 25, 15, 10, 10, 5])
growth_rates = np.array([5, 10, 20, 25, 5, 8])  # Hypothetical growth rates for the next decade

# Colors for each mode
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Emphasize 'Autonomous Electric Cars' by exploding it slightly
explode = (0.1, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax1 = plt.subplots(figsize=(14, 8))  # Increase figure size for better spacing

wedges, texts, autotexts = ax1.pie(
    usage_percentages,
    labels=modes_of_transport,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    explode=explode
)

# Draw center circle for a donut style
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax1.add_artist(centre_circle)

# Equal aspect ratio ensures that pie chart is drawn as a circle
ax1.axis('equal')

# Customize text on pie chart for readability
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Create a bar chart overlay
ax2 = ax1.twinx()  # Create a secondary y-axis on the same x-axis
bar_width = 0.1
bar_positions = np.arange(len(modes_of_transport))

# Adjust bar positions to avoid overlap
bar_positions = bar_positions + 0.15

ax2.bar(
    bar_positions,
    growth_rates,
    color=colors,
    width=bar_width,
    alpha=0.6,
    label='Projected Growth Rates (%)'
)

ax2.set_ylim(0, max(growth_rates) + 5)
ax2.set_ylabel('Growth Rate (%)', fontsize=10)
ax2.set_xticks(bar_positions - 0.15)  # Adjust ticks back to original positions
ax2.set_xticklabels(modes_of_transport, rotation=45, ha='right', fontsize=10)  # Adjust fontsize
ax2.legend(loc='upper right')

# Title and layout adjustments
plt.title("Global Modes of Transport in 2030:\nA Vision of the Future with Growth Projections", fontsize=14, fontweight='bold', pad=20)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()