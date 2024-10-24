import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2021)

# Define energy consumption data (in terawatt-hours, TWh) for each source
solar = [20, 25, 30, 38, 50, 65, 80, 100, 125, 150, 180]
wind = [10, 20, 35, 50, 70, 90, 110, 130, 155, 170, 200]
hydroelectric = [40, 45, 48, 50, 52, 54, 55, 57, 60, 62, 65]
geothermal = [5, 8, 10, 13, 15, 18, 20, 23, 25, 27, 30]

# Stack the data
data = np.vstack([solar, wind, hydroelectric, geothermal])

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(years, data, labels=['Solar', 'Wind', 'Hydroelectric', 'Geothermal'], colors=['#FFD700', '#1E90FF', '#32CD32', '#8B4513'], alpha=0.8)

# Add chart details
ax.set_title('Decadal Trends in Renewable Energy Usage\nin EcoLand (2010-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Consumption (TWh)', fontsize=12)
ax.legend(loc='upper left', fontsize=10, title='Energy Source')
ax.grid(True, linestyle='--', alpha=0.6)

# Highlighting notable events
ax.annotate('Significant solar growth', xy=(2015, 90), xytext=(2016, 200),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=9)

# Adjust the x-axis labels to prevent overlap
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 451, 50))

# Automatically adjust layout to prevent overlapping of elements
plt.tight_layout()

# Show the chart
plt.show()