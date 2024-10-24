import matplotlib.pyplot as plt

# New, more detailed data for the donut pie chart
energy_sources = [
    'Solar Photovoltaic', 'Solar Thermal', 'Onshore Wind', 'Offshore Wind',
    'Large-scale Hydroelectric', 'Small-scale Hydroelectric', 
    'Biomass (Wood)', 'Biomass (Biofuels)', 'Geothermal', 'Tidal'
]

# Updated proportions reflecting more detailed data points
proportions_2023 = [15, 8, 12, 8, 10, 10, 5, 10, 12, 10]
proportions_2030 = [20, 10, 15, 10, 8, 9, 3, 7, 10, 8]  # projected for comparison

# Define distinct colors for each energy source
colors = [
    '#FFD700', '#FFA500', '#00BFFF', '#1E90FF',
    '#32CD32', '#9ACD32', '#8B4513', '#D2691E', 
    '#FF4500', '#8A2BE2'
]

# Create a figure with multiple subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# First subplot for 2023 data
wedges_2023, texts_2023, autotexts_2023 = axs[0].pie(
    proportions_2023, labels=energy_sources, autopct='%1.1f%%', startangle=90,
    colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.3), shadow=True
)
axs[0].set_title('2023 Renewable Energy Composition', fontsize=12, weight='bold')
axs[0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.setp(autotexts_2023, size=9, weight='bold', color='white')

# Second subplot for 2030 projected data
wedges_2030, texts_2030, autotexts_2030 = axs[1].pie(
    proportions_2030, labels=energy_sources, autopct='%1.1f%%', startangle=90,
    colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.3), shadow=True
)
axs[1].set_title('2030 Projected Renewable Energy Composition', fontsize=12, weight='bold')
axs[1].axis('equal')
plt.setp(autotexts_2030, size=9, weight='bold', color='white')

# Add a centralized title for the entire figure
fig.suptitle('Renewable Energy Consumption in Greenlandia', fontsize=16, weight='bold', y=1.05)

# Add a legend, ensuring it doesn't overlap with the chart
fig.legend(wedges_2023, energy_sources, title="Energy Sources", loc="center right", bbox_to_anchor=(1.2, 0.5))

# Automatically adjust layout for better presentation
plt.tight_layout()

# Display the chart
plt.show()