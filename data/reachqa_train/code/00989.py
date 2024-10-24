import matplotlib.pyplot as plt
import numpy as np

# Define regions and renewable energy sources
regions = ['Sun Valley', 'Wind Ridge', 'Riverland', 'Geotherma']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal']

# Data: energy production in Gigawatt hours (GWh)
production_data = np.array([
    [300, 100, 50, 20],   # Sun Valley
    [50, 320, 30, 10],    # Wind Ridge
    [40, 60, 380, 10],    # Riverland
    [30, 70, 20, 290]     # Geotherma
])

# Calculate totals for annotations
total_production = production_data.sum(axis=1)

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))

# Colors for the energy sources
colors = ['#f1c40f', '#3498db', '#2ecc71', '#e67e22']

# Stacked bar chart
bottoms = np.zeros(len(regions))
for i in range(len(energy_sources)):
    ax.bar(
        regions,
        production_data[:, i],
        bottom=bottoms,
        label=energy_sources[i],
        color=colors[i],
        edgecolor='white'
    )
    bottoms += production_data[:, i]

# Title and labels
ax.set_title('Green Energy Insights: 2023\nRenewable Energy Production by Region', fontsize=16, pad=20)
ax.set_ylabel('Energy Production (GWh)', fontsize=12)

# Legend outside plot
ax.legend(title='Energy Source', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Add total production labels on top of each stack
for i, total in enumerate(total_production):
    ax.text(i, total + 10, f'{total} GWh', ha='center', fontsize=11, color='black')

# Avoid overlap by adjusting layout
plt.tight_layout()

# Display the plot
plt.show()