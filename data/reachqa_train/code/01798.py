import matplotlib.pyplot as plt
import numpy as np

# Original data for years 2010 to 2020
years = np.arange(2010, 2021)
coal = np.array([350, 340, 330, 310, 290, 270, 250, 230, 200, 180, 150])
natural_gas = np.array([200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300])
nuclear = np.array([100, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145])
renewables = np.array([50, 60, 75, 90, 105, 120, 140, 160, 180, 210, 250])
oil = np.array([150, 145, 140, 135, 130, 125, 120, 115, 110, 105, 100])

# Data construction for new plot - forecast for 2021 to 2025
forecast_years = np.arange(2021, 2026)
coal_forecast = np.array([140, 130, 120, 110, 100])
natural_gas_forecast = np.array([310, 320, 330, 340, 350])
nuclear_forecast = np.array([150, 155, 160, 165, 170])
renewables_forecast = np.array([270, 290, 310, 330, 350])
oil_forecast = np.array([95, 90, 85, 80, 75])

# Start plotting
fig, ax = plt.subplots(1, 2, figsize=(18, 8))

# Plot 1: Stacked area chart for 2010-2020
ax[0].stackplot(years, coal, natural_gas, nuclear, renewables, oil,
                labels=['Coal', 'Natural Gas', 'Nuclear', 'Renewables', 'Oil'],
                colors=['#d62728', '#1f77b4', '#9467bd', '#2ca02c', '#ff7f0e'], alpha=0.85)

ax[0].set_title('Energy Consumption by Source\n2010-2020', fontsize=14, fontweight='bold')
ax[0].set_xlabel('Year', fontsize=12)
ax[0].set_ylabel('Energy Consumption (TWh)', fontsize=12)
ax[0].set_xlim(years[0], years[-1])
ax[0].set_ylim(0, np.max([coal + natural_gas + nuclear + renewables + oil]) + 50)
ax[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax[0].legend(loc='upper left', fontsize=10, title="Energy Sources", bbox_to_anchor=(1.05, 1))
ax[0].tick_params(axis='x', rotation=45)
ax[0].annotate('Rise of Renewables', xy=(2019, 1100), xytext=(2016, 1400),
               arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, fontweight='bold')
ax[0].annotate('Decline in Coal Usage', xy=(2011, 600), xytext=(2012, 1000),
               arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, fontweight='bold')

# Plot 2: Bar chart for forecasted data 2021-2025
ax[1].bar(forecast_years - 0.2, coal_forecast, width=0.2, label='Coal', color='#d62728', alpha=0.85)
ax[1].bar(forecast_years, natural_gas_forecast, width=0.2, label='Natural Gas', color='#1f77b4', alpha=0.85)
ax[1].bar(forecast_years + 0.2, nuclear_forecast, width=0.2, label='Nuclear', color='#9467bd', alpha=0.85)
ax[1].bar(forecast_years + 0.4, renewables_forecast, width=0.2, label='Renewables', color='#2ca02c', alpha=0.85)
ax[1].bar(forecast_years + 0.6, oil_forecast, width=0.2, label='Oil', color='#ff7f0e', alpha=0.85)

ax[1].set_title('Forecasted Energy Consumption\n2021-2025', fontsize=14, fontweight='bold')
ax[1].set_xlabel('Year', fontsize=12)
ax[1].set_ylabel('Energy Consumption (TWh)', fontsize=12)
ax[1].set_xlim(forecast_years[0] - 1, forecast_years[-1] + 1)
ax[1].set_ylim(0, np.max([coal_forecast + natural_gas_forecast + nuclear_forecast + renewables_forecast + oil_forecast]) + 50)
ax[1].legend(loc='upper left', fontsize=10, title="Energy Sources", bbox_to_anchor=(1.05, 1))
ax[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax[1].tick_params(axis='x', rotation=45)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()