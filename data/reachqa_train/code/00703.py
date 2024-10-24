import matplotlib.pyplot as plt
import numpy as np

# Define the years over which data is collected
years = np.array([2018, 2019, 2020, 2021, 2022])

# Synthetic sales growth data for each region (in percentage)
sales_growth = {
    'North America': np.array([10, 12, 14, 13, 16]),
    'Europe': np.array([9, 11, 15, 14, 17]),
    'Asia-Pacific': np.array([15, 18, 22, 20, 25]),
    'Latin America': np.array([8, 10, 13, 12, 14])
}

# Error margins representing uncertainty in each region's growth data (in percentage)
error_margins = {
    'North America': np.array([1.5, 1.7, 2, 1.8, 2.2]),
    'Europe': np.array([1.3, 1.5, 2, 1.9, 2.3]),
    'Asia-Pacific': np.array([1.8, 2, 2.5, 2.3, 2.7]),
    'Latin America': np.array([1.2, 1.4, 1.8, 1.7, 2])
}

# Plotting the line chart with error bars
fig, ax = plt.subplots(figsize=(12, 8))

# Define line styles and colors for diversity and clarity
line_styles = ['-', '--', '-.', ':']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Iterate over the data, plotting each region's growth with error bars
for (region, growth), color, style in zip(sales_growth.items(), colors, line_styles):
    ax.errorbar(years, growth, yerr=error_margins[region], label=region,
                capsize=5, marker='o', linestyle=style, color=color, alpha=0.9)

# Customizing plot aesthetics
ax.set_title("Annual Growth & Uncertainty in E-commerce Sales\nAcross Different Regions", fontsize=14, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Growth in Sales (%)", fontsize=12)
ax.legend(title="Region", loc='upper left')
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Use tight_layout to prevent overlapping elements
plt.tight_layout()

# Display the completed chart
plt.show()