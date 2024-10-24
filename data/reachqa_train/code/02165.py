import matplotlib.pyplot as plt
import numpy as np

# Years of interest
years = np.arange(2020, 2031)

# Number of space tourists each year (in thousands)
space_tourists = np.array([0.5, 1.2, 2.5, 5.0, 8.5, 12.0, 15.0, 18.5, 22.0, 28.5, 35.0])

# Revenue from space tourism (in millions)
# Assume a $1M revenue per tourist with some growth and variability
revenue_per_tourist = 1.0  # in million dollars
space_revenue = space_tourists * revenue_per_tourist * (1.0 + np.array([0.1, 0.15, 0.2, 0.18, 0.25, 0.22, 0.3, 0.28, 0.35, 0.33, 0.4]))

# Significant milestones in space tourism
milestones = {
    2021: "1K Tourists Achieved",
    2023: "Launch of Space Hotel I",
    2026: "Commercial Flights Double",
    2029: "30K Tourists Milestone"
}

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 9))

# Plotting the number of space tourists (line plot)
ax1.plot(years, space_tourists, marker='o', linestyle='-', color='#FF5733', linewidth=2, label='Space Tourists')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Number of Space Tourists (in thousands)", fontsize=12, color='#FF5733')
ax1.tick_params(axis='y', labelcolor='#FF5733')

# Adding a bar chart for revenue data on a secondary y-axis
ax2 = ax1.twinx()
ax2.bar(years, space_revenue, color='lightblue', alpha=0.6, label='Revenue ($M)', width=0.5)
ax2.set_ylabel("Revenue (in millions)", fontsize=12, color='lightblue')
ax2.tick_params(axis='y', labelcolor='lightblue')

# Annotate significant milestones
for year, label in milestones.items():
    ax1.annotate(label,
                 (year, space_tourists[years == year]),
                 textcoords="offset points",
                 xytext=(0, 15),
                 ha='center',
                 fontsize=9,
                 arrowprops=dict(arrowstyle='->', color='gray'))

# Title with multi-line
plt.title("The Evolution of Space Tourism Visits\nand Generated Revenue from 2020 to 2030", fontsize=16, fontweight='bold', pad=20)

# Customizing the grid, legends, and vertical lines for milestones
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

for year in milestones.keys():
    ax1.axvline(year, color='blue', linestyle='--', linewidth=1)

# Ensuring clarity in ticks
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 40, 5))
ax2.set_yticks(np.arange(0, max(space_revenue) + 5, 5))

# Automatic layout adjustment
fig.tight_layout()

# Display the chart
plt.show()