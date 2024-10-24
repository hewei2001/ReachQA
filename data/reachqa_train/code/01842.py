import matplotlib.pyplot as plt
import numpy as np

# Device categories and their energy consumption percentages
device_categories = ['Smart Lighting', 'Smart Thermostats', 'Smart Speakers', 'Smart TVs', 'Smart Appliances']
energy_consumption_percentages = [15, 25, 10, 30, 20]

# Define a color palette for the device categories
cmap = plt.get_cmap('coolwarm')
colors = [cmap(0.2), cmap(0.4), cmap(0.6), cmap(0.8), cmap(1.0)]

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.barh(device_categories, energy_consumption_percentages, color=colors, edgecolor='black', height=0.6)

# Set labels and a descriptive multi-line title
ax.set_xlabel('Energy Consumption (%)', fontsize=12, fontweight='bold')
ax.set_ylabel('Smart Devices', fontsize=12, fontweight='bold')
ax.set_title('Tech Energy Consumption:\nPercentage Contribution of Devices in Smart Homes (2023)', fontsize=16, fontweight='bold', loc='left', pad=20)

# Add data labels to each bar with enhanced styling
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height()/2,
            f'{width}%', va='center', ha='left', fontsize=11, fontweight='bold', color='darkred')

# Set x-axis limits to focus on percentage representation
ax.set_xlim(0, 100)

# Add horizontal grid lines for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7, color='gray')

# Customize y-axis: invert and align ticks with bar centers
ax.invert_yaxis()

# Create annotations for smart device significance
annotations = [
    '💡 Smart Lighting: Enhances ambiance, saves energy',
    '🌡️ Smart Thermostats: Automates climate control, improves efficiency',
    '🔊 Smart Speakers: Provides connectivity, minimal power use',
    '📺 Smart TVs: Entertainment, significant energy draw',
    '🔌 Smart Appliances: Streamline chores, considerable power'
]

# Add a legend explaining device significance with formatted annotations
legend = plt.legend(bars, annotations, title="Device Significance", loc='upper right',
                    bbox_to_anchor=(1.35, 1), fontsize=10, title_fontsize='11', frameon=False)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()