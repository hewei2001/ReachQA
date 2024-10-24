import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Manually created power generation data (in TWh) for each renewable energy source
solar = np.array([22, 30, 45, 60, 80, 110, 140, 180, 230, 290, 370])
wind = np.array([120, 135, 150, 170, 200, 235, 275, 320, 370, 430, 500])
hydropower = np.array([350, 355, 360, 365, 370, 375, 380, 385, 390, 395, 400])
geothermal = np.array([10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
biomass = np.array([40, 42, 44, 46, 50, 55, 60, 65, 70, 75, 80])

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(14, 9))

ax.stackplot(
    years,
    solar,
    wind,
    hydropower,
    geothermal,
    biomass,
    labels=['Solar', 'Wind', 'Hydropower', 'Geothermal', 'Biomass'],
    colors=['#ffcc00', '#66ccff', '#99cc99', '#ff6666', '#9966cc'],
    alpha=0.8
)

# Titles and labels
ax.set_title("Decade of Green Energy:\nGrowth of Renewable Power Generation (2010-2020)",
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Power Generation (TWh)", fontsize=14)

# Adjust grid and layout
ax.grid(True, linestyle='--', alpha=0.5)

# Legend outside the plot area to avoid overlapping
ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Adjust x-axis labels to prevent overlap
plt.xticks(years, rotation=45, fontsize=10)
plt.yticks(fontsize=10)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()