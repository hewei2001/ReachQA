import matplotlib.pyplot as plt
import numpy as np

# Define the years and sales data
years = np.arange(2010, 2021)
sales = np.array([50, 70, 100, 160, 250, 400, 650, 1000, 1500, 2300, 3500])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the sales data as a line chart
ax.plot(years, sales, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6, label='EV Sales')

# Add title and labels
ax.set_title('The Rise of Electric Vehicles:\nA Decade of Growth in Global Sales', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Sales (in thousands)', fontsize=14)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Highlight key milestones in the growth of EVs
ax.annotate('Significant Growth Begins', xy=(2013, 160), xytext=(2011, 800),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=12, color='darkred', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightgrey', alpha=0.8))
ax.annotate('Exponential Increase', xy=(2018, 1500), xytext=(2016, 3000),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=12, color='darkgreen', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightgrey', alpha=0.8))

# Set axis limits
ax.set_xlim(2010, 2020)
ax.set_ylim(0, 4000)

# Add a legend to the plot
ax.legend(loc='upper left', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()