import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2010, 2020)
north_america = np.array([450, 470, 495, 520, 550, 580, 615, 645, 680, 715])
europe = np.array([430, 455, 480, 505, 535, 570, 600, 640, 675, 710])
asia = np.array([300, 340, 380, 420, 470, 520, 580, 650, 720, 800])
africa = np.array([150, 160, 180, 205, 230, 260, 300, 360, 400, 450])
south_america = np.array([280, 290, 310, 340, 370, 410, 460, 510, 570, 620])

# Cumulative sum for each region
north_america_cum = np.cumsum(north_america)
europe_cum = np.cumsum(europe)
asia_cum = np.cumsum(asia)
africa_cum = np.cumsum(africa)
south_america_cum = np.cumsum(south_america)

# Plotting
fig, ax = plt.subplots(2, 1, figsize=(12, 10))

# Main plot with cumulative data
ax[0].plot(years, north_america_cum, label='North America', marker='o', linestyle='-', color='b', linewidth=2)
ax[0].plot(years, europe_cum, label='Europe', marker='s', linestyle='--', color='g', linewidth=2)
ax[0].plot(years, asia_cum, label='Asia', marker='^', linestyle='-.', color='r', linewidth=2)
ax[0].plot(years, africa_cum, label='Africa', marker='d', linestyle=':', color='m', linewidth=2)
ax[0].plot(years, south_america_cum, label='South America', marker='x', linestyle='-', color='y', linewidth=2)

ax[0].set_title("Cumulative Growth in Renewable Energy Usage\nAcross Regions (2010-2019)", fontsize=14, weight='bold')
ax[0].set_xlabel("Year", fontsize=12)
ax[0].set_ylabel("Cumulative Energy Consumption (in Terawatt-hours)", fontsize=12)
ax[0].set_xticks(years)
ax[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax[0].legend(loc='upper left', fontsize=10)

# Subplot with relative growth rate
growth_rate_na = np.gradient(north_america)
growth_rate_eu = np.gradient(europe)
growth_rate_asia = np.gradient(asia)
growth_rate_africa = np.gradient(africa)
growth_rate_sa = np.gradient(south_america)

ax[1].plot(years, growth_rate_na, label='North America', marker='o', linestyle='-', color='b', linewidth=2)
ax[1].plot(years, growth_rate_eu, label='Europe', marker='s', linestyle='--', color='g', linewidth=2)
ax[1].plot(years, growth_rate_asia, label='Asia', marker='^', linestyle='-.', color='r', linewidth=2)
ax[1].plot(years, growth_rate_africa, label='Africa', marker='d', linestyle=':', color='m', linewidth=2)
ax[1].plot(years, growth_rate_sa, label='South America', marker='x', linestyle='-', color='y', linewidth=2)

ax[1].set_title("Year-on-Year Growth Rate of Renewable Energy Usage", fontsize=12, weight='bold')
ax[1].set_xlabel("Year", fontsize=12)
ax[1].set_ylabel("Growth Rate (TWh/year)", fontsize=12)
ax[1].set_xticks(years)
ax[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax[1].legend(loc='upper left', fontsize=10)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()