import matplotlib.pyplot as plt
import numpy as np

# Original pie chart data
energy_sources = ['Solar Panels', 'Wind Turbines', 'Hydroelectric Dams', 
                  'Biomass Generators', 'Geothermal Plants']
contributions_2050 = [40, 25, 15, 10, 10]  # Contribution percentages for 2050

# New subplot data: Projected output (in GWh) over the years
years = np.arange(2020, 2051, 5)
output_projections = {
    'Solar Panels': np.array([100, 120, 150, 200, 250, 320, 400]),
    'Wind Turbines': np.array([80, 100, 120, 150, 180, 210, 250]),
    'Hydroelectric Dams': np.array([60, 65, 70, 75, 80, 85, 90]),
    'Biomass Generators': np.array([40, 45, 50, 55, 60, 65, 70]),
    'Geothermal Plants': np.array([30, 35, 40, 45, 50, 55, 60])
}

# Color scheme
colors = ['#FFDD44', '#44BBA4', '#5F4BB6', '#FF6F61', '#6CBB3C']

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 9))

# Donut pie chart (original)
wedges, texts, autotexts = axes[0].pie(contributions_2050, labels=energy_sources,
                                       colors=colors, autopct='%1.1f%%',
                                       startangle=90, pctdistance=0.85,
                                       wedgeprops=dict(width=0.3), shadow=True)
plt.setp(autotexts, size=10, weight="bold", color='darkblue')
plt.setp(texts, size=10, weight="bold")
axes[0].set_title('Ecoopolis Energy Source Distribution\nin 2050', 
                  fontsize=16, weight='bold', pad=30)
axes[0].axis('equal')

# Line chart for projected outputs over time
for source, output in output_projections.items():
    axes[1].plot(years, output, label=source, linewidth=2.5)

# Customize line chart
axes[1].set_title('Projected Energy Output\n2020-2050', fontsize=16, weight='bold', pad=20)
axes[1].set_xlabel('Year', fontsize=12, weight='bold')
axes[1].set_ylabel('Output (GWh)', fontsize=12, weight='bold')
axes[1].legend(title="Energy Sources", fontsize='medium', loc='upper left')
axes[1].grid(True)

# Layout and display
plt.tight_layout()
plt.show()