import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2021)

# Define energy consumption data (in terawatt-hours, TWh) for each source
solar = np.array([20, 25, 30, 38, 50, 65, 80, 100, 125, 150, 180])
wind = np.array([10, 20, 35, 50, 70, 90, 110, 130, 155, 170, 200])
hydroelectric = np.array([40, 45, 48, 50, 52, 54, 55, 57, 60, 62, 65])
geothermal = np.array([5, 8, 10, 13, 15, 18, 20, 23, 25, 27, 30])

# Calculate the percentage change year-over-year
def percentage_change(data):
    return np.array([(data[i] - data[i - 1]) / data[i - 1] * 100 if i != 0 else 0 for i in range(len(data))])

solar_pct_change = percentage_change(solar)
wind_pct_change = percentage_change(wind)
hydroelectric_pct_change = percentage_change(hydroelectric)
geothermal_pct_change = percentage_change(geothermal)

# Create the subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Subplot 1: Stacked Area Chart
ax1.stackplot(years, solar, wind, hydroelectric, geothermal, labels=['Solar', 'Wind', 'Hydroelectric', 'Geothermal'],
              colors=['#FFD700', '#1E90FF', '#32CD32', '#8B4513'], alpha=0.8)
ax1.set_title('Decadal Trends in Renewable Energy Usage\nin EcoLand (2010-2020)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Energy Consumption (TWh)', fontsize=12)
ax1.legend(loc='upper left', fontsize=10, title='Energy Source')
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.annotate('Significant solar growth', xy=(2015, 90), xytext=(2016, 200),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=9)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.set_yticks(np.arange(0, 451, 50))

# Subplot 2: Line Chart for Percentage Change
ax2.plot(years, solar_pct_change, label='Solar', color='#FFD700', marker='o')
ax2.plot(years, wind_pct_change, label='Wind', color='#1E90FF', marker='o')
ax2.plot(years, hydroelectric_pct_change, label='Hydroelectric', color='#32CD32', marker='o')
ax2.plot(years, geothermal_pct_change, label='Geothermal', color='#8B4513', marker='o')
ax2.set_title('Yearly Percentage Change in Renewable Energy\nConsumption (2010-2020)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Percentage Change (%)', fontsize=12)
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)
ax2.axhline(0, color='black', linewidth=0.8, linestyle='--')

# Adjust layout
plt.tight_layout()

# Show the charts
plt.show()