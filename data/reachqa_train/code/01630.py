import matplotlib.pyplot as plt
import numpy as np

# Data for pie chart: Market share of renewable energy types
labels_pie = ['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal']
sizes_pie = [35, 25, 20, 15, 5]
colors_pie = ['#ffcc00', '#66b3ff', '#99ff99', '#ff9999', '#c2c2f0']
explode_pie = (0.1, 0, 0, 0, 0)  # "Explode" the Solar slice

# Data for bar chart: Estimated growth over years for renewable energies
years = [2021, 2022, 2023, 2024]
growth_data = {
    'Solar': [30, 35, 40, 45],
    'Wind': [20, 25, 28, 30],
    'Hydroelectric': [18, 20, 22, 24],
    'Biomass': [10, 12, 14, 16],
    'Geothermal': [4, 5, 5.5, 6]
}
colors_bar = ['#ffcc00', '#66b3ff', '#99ff99', '#ff9999', '#c2c2f0']

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Plotting the pie chart
ax1.pie(sizes_pie, explode=explode_pie, labels=labels_pie, colors=colors_pie, autopct='%1.1f%%', shadow=True, startangle=140)
ax1.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
ax1.set_title("Global Market Share of\nRenewable Energy Sources (2023)", fontsize=12, fontweight='bold')

# Plotting the bar chart
x = np.arange(len(years))  # label locations
bar_width = 0.15

for i, (energy_type, growth) in enumerate(growth_data.items()):
    ax2.bar(x + i * bar_width, growth, bar_width, label=energy_type, color=colors_bar[i])

ax2.set_xlabel('Year', fontsize=10)
ax2.set_ylabel('Growth Percentage', fontsize=10)
ax2.set_title("Projected Growth of Renewable\nEnergy Types (2021-2024)", fontsize=12, fontweight='bold')
ax2.set_xticks(x + bar_width * 2)
ax2.set_xticklabels(years)
ax2.legend(title="Energy Types", loc='upper left', bbox_to_anchor=(1, 1))

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()