import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Energy consumption data for each source (in terawatt-hours)
coal = np.array([350, 340, 330, 310, 290, 270, 250, 230, 200, 180, 150])
natural_gas = np.array([200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300])
nuclear = np.array([100, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145])
renewables = np.array([50, 60, 75, 90, 105, 120, 140, 160, 180, 210, 250])
oil = np.array([150, 145, 140, 135, 130, 125, 120, 115, 110, 105, 100])

# Stack the data
data = np.array([coal, natural_gas, nuclear, renewables, oil])

# Plotting the stacked area chart
plt.figure(figsize=(14, 8))
plt.stackplot(years, data, labels=['Coal', 'Natural Gas', 'Nuclear', 'Renewables', 'Oil'],
              colors=['#d62728', '#1f77b4', '#9467bd', '#2ca02c', '#ff7f0e'], alpha=0.85)

# Titles and labels
plt.title('Evolution of Energy Consumption by Source\n2010 to 2020', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Consumption (TWh)', fontsize=12)
plt.xlim(years[0], years[-1])
plt.ylim(0, np.max(data.sum(axis=0)) + 50)

# Add grid for clarity
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add legend
plt.legend(loc='upper left', fontsize=10, title="Energy Sources", bbox_to_anchor=(1.05, 1))

# Rotating x-axis labels for better readability
plt.xticks(years, rotation=45)

# Adding annotations to highlight key trends
plt.annotate('Rise of Renewables', xy=(2019, 1100), xytext=(2016, 1400),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, fontweight='bold')
plt.annotate('Decline in Coal Usage', xy=(2011, 600), xytext=(2012, 1000),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, fontweight='bold')

# Adjust layout for better visibility
plt.tight_layout()

# Show the plot
plt.show()