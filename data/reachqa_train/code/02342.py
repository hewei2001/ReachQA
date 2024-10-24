import numpy as np
import matplotlib.pyplot as plt

# Extend the time span and increase data frequency
years = np.arange(2010, 2031)  # From 2010 to 2030

# Define sectors and introduce new categories
sectors = ['Residential', 'Commercial', 'Industrial', 'Transportation', 'Agriculture', 'Public Services']

# Construct the data for each sector (quarterly average for simplicity)
residential_usage = np.array([10, 15, 23, 31, 40, 52, 66, 82, 100, 120, 145, 170, 190, 215, 240, 265, 290, 315, 340, 365, 390])
commercial_usage = np.array([8, 12, 18, 25, 34, 45, 59, 75, 95, 117, 142, 162, 185, 207, 230, 252, 275, 298, 320, 342, 365])
industrial_usage = np.array([20, 25, 33, 43, 56, 72, 91, 113, 138, 166, 198, 225, 255, 280, 305, 330, 355, 380, 405, 430, 455])
transportation_usage = np.array([5, 9, 15, 22, 32, 45, 60, 78, 99, 123, 150, 172, 195, 220, 245, 270, 295, 320, 345, 370, 395])
agriculture_usage = np.array([4, 6, 10, 15, 22, 30, 40, 52, 67, 85, 105, 125, 145, 165, 185, 205, 225, 245, 265, 285, 305])
public_services_usage = np.array([3, 5, 8, 12, 17, 23, 30, 40, 53, 69, 87, 110, 135, 160, 185, 210, 235, 260, 285, 310, 335])

# Set up the plot with subplots for main plot and cumulative growth
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

# Create the stacked area plot
ax1.stackplot(years, residential_usage, commercial_usage, industrial_usage, transportation_usage,
              agriculture_usage, public_services_usage,
              labels=sectors,
              colors=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF66B3', '#CC99FF'], alpha=0.85)

# Customize the main plot
ax1.set_title("Greenovia's Renewable Energy Expansion:\nAn In-depth Analysis of Multi-Sector Adoption (2010-2030)",
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12, labelpad=10)
ax1.set_ylabel("Renewable Energy Usage (GWh)", fontsize=12, labelpad=10)
ax1.legend(loc='upper left', fontsize=10, title="Sectors", title_fontsize='12')
ax1.annotate('Residential Surge', xy=(2020, 1450), xytext=(2018, 1550),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='center')
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_xticks(years[::2])
ax1.set_xticklabels(years[::2], rotation=45)

# Add subplot for cumulative growth
total_usage = (residential_usage + commercial_usage + industrial_usage + transportation_usage +
               agriculture_usage + public_services_usage)
cumulative_growth = np.cumsum(total_usage - total_usage[0])

ax2.plot(years, cumulative_growth, color='tab:blue', linewidth=2.5, linestyle='-')
ax2.set_title("Cumulative Growth of Renewable Energy Usage", fontsize=14, pad=10)
ax2.set_xlabel("Year", fontsize=12, labelpad=10)
ax2.set_ylabel("Cumulative Growth (GWh)", fontsize=12, labelpad=10)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.set_xticks(years[::2])
ax2.set_xticklabels(years[::2], rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()