import matplotlib.pyplot as plt
import numpy as np

# Define an extended range of years for data collection
years = np.arange(2010, 2023)

# Synthetic sales growth data for additional regions (in percentage)
sales_growth = {
    'North America': np.array([8, 9, 10, 11, 12, 10, 12, 14, 13, 16, 14, 17, 19]),
    'Europe': np.array([7, 8, 9, 10, 11, 9, 11, 15, 14, 17, 15, 16, 18]),
    'Asia-Pacific': np.array([12, 13, 15, 16, 18, 15, 18, 22, 20, 25, 23, 27, 30]),
    'Latin America': np.array([5, 6, 8, 9, 10, 8, 10, 13, 12, 14, 13, 15, 16]),
    'Africa': np.array([3, 4, 5, 6, 7, 6, 8, 10, 9, 11, 10, 12, 14])
}

# Error margins for uncertainty (in percentage)
error_margins = {
    'North America': np.array([1, 1.2, 1.5, 1.6, 1.7, 1.5, 1.7, 2, 1.8, 2.2, 2, 2.3, 2.5]),
    'Europe': np.array([1, 1.1, 1.3, 1.4, 1.5, 1.3, 1.5, 2, 1.9, 2.3, 2.1, 2.2, 2.4]),
    'Asia-Pacific': np.array([1.5, 1.6, 1.8, 2, 2.2, 1.8, 2, 2.5, 2.3, 2.7, 2.5, 2.8, 3]),
    'Latin America': np.array([0.8, 1, 1.2, 1.4, 1.5, 1.2, 1.4, 1.8, 1.7, 2, 1.9, 2.1, 2.3]),
    'Africa': np.array([0.5, 0.7, 0.9, 1.1, 1.2, 1.1, 1.3, 1.6, 1.5, 1.8, 1.7, 2, 2.2])
}

# Create the figure and axes for plotting
fig, ax = plt.subplots(2, 1, figsize=(14, 12))

# Define line styles and colors
line_styles = ['-', '--', '-.', ':', '-']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot the line chart with error bars
for (region, growth), color, style in zip(sales_growth.items(), colors, line_styles):
    ax[0].errorbar(years, growth, yerr=error_margins[region], label=region,
                   capsize=3, marker='o', linestyle=style, color=color, alpha=0.8)

# Customizing aesthetics for the first plot
ax[0].set_title("Annual Growth & Uncertainty in E-commerce Sales\nAcross Different Regions (2010-2022)", fontsize=14, fontweight='bold')
ax[0].set_xlabel("Year", fontsize=12)
ax[0].set_ylabel("Growth in Sales (%)", fontsize=12)
ax[0].legend(title="Region", loc='upper left')
ax[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add a subplot for cumulative sales growth
for region, growth in sales_growth.items():
    ax[1].plot(years, np.cumsum(growth), label=region, linestyle='-', marker='x', alpha=0.7)

# Customize the aesthetics for the second plot
ax[1].set_title("Cumulative Sales Growth (2010-2022)", fontsize=14, fontweight='bold')
ax[1].set_xlabel("Year", fontsize=12)
ax[1].set_ylabel("Cumulative Growth (%)", fontsize=12)
ax[1].legend(title="Region", loc='upper left')
ax[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Ensure layout is tight and no elements overlap
plt.tight_layout()

# Display the completed plots
plt.show()