import matplotlib.pyplot as plt
import numpy as np

# Define the time range for a century
years = np.arange(1900, 2000)

# Growth data for eco-industries over a century
organic_farming = 5 + np.linspace(1, 10, len(years))
solar_energy = np.array([0 if year < 1950 else (year - 1950)**1.5 for year in years])
wind_power = np.linspace(0, 25, len(years))
recycling = np.array([1 if year < 1960 else (year - 1960)**0.8 for year in years])
electric_vehicles = np.array([0 if year < 1980 else (year - 1980)**1.2 for year in years])

# Create market share data as percentages over time
total_growth = organic_farming + solar_energy + wind_power + recycling + electric_vehicles
market_share = {
    'Organic Farming': organic_farming / total_growth * 100,
    'Solar Energy': solar_energy / total_growth * 100,
    'Wind Power': wind_power / total_growth * 100,
    'Recycling': recycling / total_growth * 100,
    'Electric Vehicles': electric_vehicles / total_growth * 100,
}

# Create the figure and two side-by-side subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# Plot the stacked area chart in the first subplot
axes[0].stackplot(years, organic_farming, solar_energy, wind_power, recycling, electric_vehicles,
                  labels=['Organic Farming', 'Solar Energy', 'Wind Power', 'Recycling', 'Electric Vehicles'],
                  colors=['forestgreen', 'gold', 'skyblue', 'darkorange', 'purple'], alpha=0.8)
axes[0].set_title("The Rise of Eco-Industries: \nA Century of Sustainability and Innovation", fontsize=14, fontweight='bold')
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Contribution to Sustainable Economy (Units)', fontsize=12)
axes[0].set_xticks(np.arange(1900, 2001, 10))
axes[0].legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))
axes[0].grid(True, linestyle='--', alpha=0.5)

# Plot the market share line plot in the second subplot
for industry, share in market_share.items():
    axes[1].plot(years, share, label=industry)

axes[1].set_title("Market Share of Eco-Industries \nAcross the Century", fontsize=14, fontweight='bold')
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Market Share (%)', fontsize=12)
axes[1].set_xticks(np.arange(1900, 2001, 10))
axes[1].legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))
axes[1].grid(True, linestyle='--', alpha=0.5)

# Adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()