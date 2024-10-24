import matplotlib.pyplot as plt
import numpy as np

# Define the years and sales data
years = np.arange(2010, 2021)
sales = np.array([50, 70, 100, 160, 250, 400, 650, 1000, 1500, 2300, 3500])

# Create related data for overlay: EV market share percentages
market_share = np.array([0.5, 0.7, 0.9, 1.5, 2.1, 2.8, 3.5, 4.7, 6.3, 8.0, 10.0])

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot the sales data as a line chart
line1, = ax1.plot(years, sales, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6, label='EV Sales')

# Add title and labels for the first y-axis
ax1.set_title('The Rise of Electric Vehicles:\nA Decade of Growth and Market Penetration', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Sales (in thousands)', fontsize=14, color='blue')

# Add grid for better readability
ax1.grid(True, linestyle='--', alpha=0.6)

# Highlight key milestones in the growth of EVs
ax1.annotate('Significant Growth Begins', xy=(2013, 160), xytext=(2011, 800),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=12, color='darkred', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightgrey', alpha=0.8))
ax1.annotate('Exponential Increase', xy=(2018, 1500), xytext=(2016, 3000),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=12, color='darkgreen', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightgrey', alpha=0.8))

# Create a secondary y-axis to overlay the market share data as a bar chart
ax2 = ax1.twinx()
bars = ax2.bar(years, market_share, color='orange', alpha=0.5, label='EV Market Share (%)')

# Add labels for the second y-axis
ax2.set_ylabel('Market Share (%)', fontsize=14, color='orange')

# Set axis limits
ax1.set_xlim(2010, 2020)
ax1.set_ylim(0, 4000)
ax2.set_ylim(0, 12)

# Combine legends from both plots
lines = [line1, bars]
ax1.legend(lines, [line.get_label() for line in lines], loc='upper left', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()