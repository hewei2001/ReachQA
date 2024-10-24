import matplotlib.pyplot as plt
import numpy as np

# Extended range from 1990 to 2025
years = np.arange(1990, 2026, 1)

# Hypothetical monthly data from 1990 to 2025
months_per_year = 12
total_months = len(years) * months_per_year
month_years = np.linspace(1990, 2025.99, total_months)

# Hypothetical emissions data
co2_emissions = 30 + 0.2 * (month_years - 1990) + 2 * np.sin(month_years * np.pi / 6)  # Adding seasonal variation
ch4_emissions = 4 + 0.05 * (month_years - 1990) - 0.01 * (month_years - 2005)**2 + 0.5 * np.sin(month_years * np.pi / 6)
n2o_emissions = 3 + 0.03 * (month_years - 1990) - 0.005 * (month_years - 2010)**2

# New gas emissions data
hfc_emissions = 1 + 0.08 * (month_years - 2000) + 0.2 * np.cos(month_years * np.pi / 6)
gdp_growth = 2 + 0.02 * (month_years - 1990) + 0.5 * np.sin(month_years * np.pi / 6)  # GDP in trillion USD

# Moving averages for smoothing the data
def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size) / window_size, mode='valid')

window_size = 12  # One year for smoothing
co2_avg = moving_average(co2_emissions, window_size)
ch4_avg = moving_average(ch4_emissions, window_size)
n2o_avg = moving_average(n2o_emissions, window_size)
hfc_avg = moving_average(hfc_emissions, window_size)

# Create the plot
plt.figure(figsize=(14, 10))
plt.plot(month_years[window_size - 1:], co2_avg, label='CO2 Emissions (Moving Avg)', color='red', linewidth=2)
plt.plot(month_years[window_size - 1:], ch4_avg, label='CH4 Emissions (Moving Avg)', color='green', linestyle='--', linewidth=2)
plt.plot(month_years[window_size - 1:], n2o_avg, label='N2O Emissions (Moving Avg)', color='blue', linestyle='-.', linewidth=2)
plt.plot(month_years[window_size - 1:], hfc_avg, label='HFC Emissions (Moving Avg)', color='purple', linestyle=':', linewidth=2)
plt.plot(month_years, gdp_growth, label='Global GDP Growth', color='orange', linestyle='-', linewidth=1.5, alpha=0.6)

# Labels and title
plt.title('Global Greenhouse Gas Emissions and GDP Growth\n(1990-2025)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Value (Million Metric Tons / Trillion USD)', fontsize=12)

# Axis ticks
plt.xticks(np.arange(1990, 2026, 5), rotation=45)
plt.yticks(np.arange(0, 45, 5))

# Annotations
plt.annotate('CO2 Peak', xy=(2010, max(co2_avg)), xytext=(2005, 42), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
plt.annotate('GDP Growth Trends', xy=(2000, gdp_growth[120]), xytext=(1995, 38), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Legend
plt.legend(title='Data Type', title_fontsize='13', fontsize=11, loc='upper left')

# Grid and layout
plt.grid(visible=True, which='major', linestyle='--', linewidth=0.5)
plt.tight_layout()

# Show the plot
plt.show()