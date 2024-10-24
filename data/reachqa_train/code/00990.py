import matplotlib.pyplot as plt
import numpy as np

# Define extended regions and renewable energy sources
regions = ['Sun Valley', 'Wind Ridge', 'Riverland', 'Geotherma', 'Solar Coast', 'Windy Plains']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']

# Data: energy production in Gigawatt hours (GWh) over two years (2022 & 2023)
production_data_2022 = np.array([
    [300, 120, 50, 30, 10],   # Sun Valley
    [60, 300, 40, 20, 15],    # Wind Ridge
    [50, 80, 360, 15, 20],    # Riverland
    [40, 60, 30, 280, 20],    # Geotherma
    [320, 80, 60, 40, 30],    # Solar Coast
    [70, 310, 50, 10, 40]     # Windy Plains
])

production_data_2023 = np.array([
    [330, 130, 60, 35, 20],   # Sun Valley
    [70, 320, 50, 25, 25],    # Wind Ridge
    [60, 90, 380, 20, 30],    # Riverland
    [50, 70, 40, 300, 25],    # Geotherma
    [350, 100, 70, 45, 40],   # Solar Coast
    [80, 330, 60, 15, 50]     # Windy Plains
])

# Calculate totals for annotations
total_production_2022 = production_data_2022.sum(axis=1)
total_production_2023 = production_data_2023.sum(axis=1)

# Plot setup
fig, ax = plt.subplots(figsize=(14, 10))

# Colors for the energy sources
colors = ['#f1c40f', '#3498db', '#2ecc71', '#e67e22', '#9b59b6']

# Plot data for 2022
x_2022 = np.arange(len(regions)) - 0.2
bottoms_2022 = np.zeros(len(regions))
for i in range(len(energy_sources)):
    ax.bar(
        x_2022,
        production_data_2022[:, i],
        width=0.4,
        bottom=bottoms_2022,
        label=f'{energy_sources[i]} 2022',
        color=colors[i],
        alpha=0.7,
        edgecolor='white'
    )
    bottoms_2022 += production_data_2022[:, i]

# Plot data for 2023
x_2023 = np.arange(len(regions)) + 0.2
bottoms_2023 = np.zeros(len(regions))
for i in range(len(energy_sources)):
    ax.bar(
        x_2023,
        production_data_2023[:, i],
        width=0.4,
        bottom=bottoms_2023,
        label=f'{energy_sources[i]} 2023',
        color=colors[i],
        edgecolor='white'
    )
    bottoms_2023 += production_data_2023[:, i]

# Title and labels
ax.set_title('Green Energy Insights: 2022 vs 2023\nRenewable Energy Production by Region', fontsize=16, pad=20)
ax.set_ylabel('Energy Production (GWh)', fontsize=12)
ax.set_xticks(np.arange(len(regions)))
ax.set_xticklabels(regions, rotation=45, ha='right')

# Legend
ax.legend(title='Energy Source & Year', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Add total production labels on top of each stack
for i, total in enumerate(total_production_2022):
    ax.text(i - 0.2, total + 20, f'{total} GWh', ha='center', fontsize=10, color='black', rotation=90)
for i, total in enumerate(total_production_2023):
    ax.text(i + 0.2, total + 20, f'{total} GWh', ha='center', fontsize=10, color='black', rotation=90)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()