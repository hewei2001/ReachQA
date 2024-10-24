import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import ConnectionPatch

# Data for the pie chart
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass', 'Ocean']
percentages = [35, 25, 20, 10, 5, 5]

# Extended data for comparison
years = ['2020', '2030', '2040', '2050']
solar_trend = [15, 20, 30, 35]  # Fictional growth over time
wind_trend = [20, 22, 24, 25]
hydro_trend = [25, 23, 22, 20]
geothermal_trend = [5, 7, 9, 10]
biomass_trend = [10, 8, 6, 5]
ocean_trend = [2, 3, 4, 5]

# Colors for each segment
colors = ['gold', 'skyblue', 'lightgreen', 'salmon', 'purple', 'teal']

# Explode parameter to highlight specific slices
explode = (0.1, 0.1, 0, 0, 0, 0)

# Create a doughnut chart
plt.figure(figsize=(14, 7))

# First subplot - Doughnut Chart
ax1 = plt.subplot(121)
wedges, texts, autotexts = ax1.pie(
    percentages,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    shadow=True,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1.5},
    pctdistance=0.85
)
plt.setp(autotexts, size=10, weight="bold", color="white")
# Draw center circle for doughnut style
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax1.set_title('Global Renewable Energy Sources\nDistribution in 2050', fontsize=14, fontweight='bold', pad=20)

# Second subplot - Bar Chart for Trends
ax2 = plt.subplot(122)
# Bar positions
ind = np.arange(len(years))
bar_width = 0.15

# Plotting trends
ax2.bar(ind, solar_trend, width=bar_width, label='Solar', color='gold')
ax2.bar(ind + bar_width, wind_trend, width=bar_width, label='Wind', color='skyblue')
ax2.bar(ind + 2*bar_width, hydro_trend, width=bar_width, label='Hydroelectric', color='lightgreen')
ax2.bar(ind + 3*bar_width, geothermal_trend, width=bar_width, label='Geothermal', color='salmon')
ax2.bar(ind + 4*bar_width, biomass_trend, width=bar_width, label='Biomass', color='purple')
ax2.bar(ind + 5*bar_width, ocean_trend, width=bar_width, label='Ocean', color='teal')

ax2.set_xticks(ind + 2.5 * bar_width)
ax2.set_xticklabels(years)
ax2.set_ylabel('Percentage')
ax2.set_title('Renewable Energy Source Trends\n(2020-2050)', fontsize=12, fontweight='bold')
ax2.legend(title='Energy Sources', bbox_to_anchor=(1.05, 1), loc='upper left')

# Connection lines for doughnut and bar chart
for i, wedge in enumerate(wedges):
    connection = ConnectionPatch(xyA=(1.15, wedge.theta1), xyB=(0, 0),
                                 coordsA='axes fraction', coordsB='data',
                                 axesA=ax1, axesB=ax2, color=colors[i])
    ax1.add_artist(connection)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the plots
plt.show()