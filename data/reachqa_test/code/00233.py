import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2000, 2021)

# Energy contributions in TWh for each renewable source
solar = np.array([10, 12, 15, 20, 30, 50, 80, 120, 160, 210, 300, 420, 550, 700, 900, 1150, 1500, 1850, 2250, 2700, 3200])
wind = np.array([20, 25, 40, 60, 90, 130, 180, 250, 330, 430, 550, 680, 830, 1000, 1200, 1450, 1750, 2100, 2500, 2950, 3400])
hydro = np.array([1000, 1005, 1010, 1015, 1020, 1025, 1030, 1035, 1040, 1045, 1050, 1055, 1060, 1065, 1070, 1075, 1080, 1085, 1090, 1095, 1100])
biomass = np.array([150, 160, 175, 190, 210, 230, 255, 280, 310, 340, 370, 410, 450, 500, 560, 620, 690, 760, 850, 950, 1050])

# Calculate total renewable energy for an additional plot
total_renewable = solar + wind + hydro + biomass

# Colors for each energy source
colors = ['#ffcc00', '#4682b4', '#32cd32', '#8b4513']

# Create the stacked area plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Stacked area plot
ax1.stackplot(years, solar, wind, hydro, biomass, labels=['Solar', 'Wind', 'Hydro', 'Biomass'], colors=colors)
ax1.set_title("Contribution of Renewable Energy Sources\n to Global Energy Production (2000-2020)", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12, fontweight='bold')
ax1.set_ylabel("Energy Production (TWh)", fontsize=12, fontweight='bold')

# Add grid lines
ax1.grid(visible=True, which='both', color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Highlight specific years
highlight_years = [2010, 2015]
for year in highlight_years:
    ax1.axvline(x=year, color='grey', linestyle=':', linewidth=1)

# Add annotations
ax1.annotate('Rapid solar growth', xy=(2015, solar[15]), xytext=(2008, 1000),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Secondary plot for total renewable energy
ax2 = ax1.twinx()
ax2.plot(years, total_renewable, color='black', linestyle='-', marker='o', label='Total Renewable')
ax2.set_ylabel("Total Renewable Energy (TWh)", fontsize=12, fontweight='bold', color='black')

# Customize ticks
ax1.tick_params(axis='x', rotation=45)
ax1.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

# Add a legend with a custom location to avoid occlusion of data
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Automatically adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()