import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2010, 2021)
solar_growth = np.array([30, 40, 60, 80, 100, 130, 160, 200, 250, 310, 380])  # in TWh
wind_growth = np.array([80, 95, 115, 145, 180, 220, 265, 315, 370, 430, 500])  # in TWh
total_renewable = np.array([200, 230, 270, 320, 380, 450, 530, 620, 720, 840, 980])  # in TWh

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# First subplot: Line plot for solar and wind growth
ax1.plot(years, solar_growth, marker='o', linestyle='-', color='gold', linewidth=2, markersize=8, label='Solar Energy Growth')
ax1.plot(years, wind_growth, marker='s', linestyle='-', color='skyblue', linewidth=2, markersize=8, label='Wind Energy Growth')
ax1.annotate('Significant Solar Surge', xy=(2015, 130), xytext=(2013, 230),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=9, fontweight='bold')
ax1.annotate('Wind Takes the Lead', xy=(2018, 315), xytext=(2016, 410),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=9, fontweight='bold')
ax1.set_title('Rising Tides of Green Energy:\nTracking Solar and Wind Growth from 2010 to 2020', fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12, labelpad=10)
ax1.set_ylabel('Energy Production Growth (TWh)', fontsize=12, labelpad=10)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, ha='right', fontsize=11)
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax1.legend(loc='upper left', fontsize=11, frameon=False)
for x, y in zip(years, solar_growth):
    ax1.text(x, y + 10, f'{y}', ha='center', va='bottom', fontsize=9, color='darkgoldenrod')
for x, y in zip(years, wind_growth):
    ax1.text(x, y + 10, f'{y}', ha='center', va='bottom', fontsize=9, color='dodgerblue')

# Second subplot: Bar chart for total renewable energy
width = 0.35
ax2.bar(years - width/2, solar_growth + wind_growth, width, label='Combined Solar & Wind', color='lightseagreen')
ax2.bar(years + width/2, total_renewable, width, label='Total Renewable', color='coral')
ax2.set_title('Combined vs Total Renewable Energy Production', fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel('Year', fontsize=12, labelpad=10)
ax2.set_ylabel('Energy Production (TWh)', fontsize=12, labelpad=10)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45, ha='right', fontsize=11)
ax2.legend(loc='upper left', fontsize=11, frameon=False)
ax2.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the charts
plt.show()