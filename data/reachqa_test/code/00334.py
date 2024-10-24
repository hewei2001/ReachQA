import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Hypothetical data for the percentage of urban areas adopting renewable energy solutions
renewable_adoption = np.array([15, 18, 22, 30, 40, 48, 55, 62, 70, 80, 90])

# Hypothetical data for renewable infrastructure investment (in billions)
infrastructure_investment = np.array([5, 6, 7, 10, 13, 16, 20, 24, 29, 35, 42])

# Annotations for key events impacting adoption
annotations = {
    2013: 'Urban Policy\nChange',
    2016: 'Tech Breakthrough',
    2019: 'Global Summit\nAgreement'
}

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(14, 7))

# Primary line chart for renewable adoption
ax1.plot(years, renewable_adoption, marker='o', color='seagreen', linestyle='-', linewidth=2.5, markersize=8, label='Renewable Adoption (%)')

# Secondary y-axis for infrastructure investment
ax2 = ax1.twinx()
ax2.plot(years, infrastructure_investment, color='mediumblue', linestyle='--', linewidth=2, marker='s', markersize=6, label='Infrastructure Investment (Billion $)', alpha=0.7)

# Enhancements for annotations
for year, text in annotations.items():
    ax1.annotate(
        text,
        (year, renewable_adoption[year - 2010]),
        xytext=(-30, 20),
        textcoords='offset points',
        bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='whitesmoke', alpha=0.8),
        arrowprops=dict(arrowstyle='->', color='gray'),
        ha='center', fontsize=10, color='darkgreen'
    )

# Titles and labels
ax1.set_title(
    "Growth of Renewable Energy Adoption\nin Global Urban Areas with Investment (2010-2020)",
    fontsize=16, fontweight='bold', pad=20
)
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Adoption (%)", fontsize=14, color='seagreen')
ax2.set_ylabel("Investment (Billion $)", fontsize=14, color='mediumblue')

# Format y-axis to include percentage sign
ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{int(y)}%'))

# Customize the grid
ax1.grid(True, linestyle='--', alpha=0.7)

# Ensure all years are marked on the x-axis
ax1.set_xticks(years)

# Label each data point with its value
for x, y in zip(years, renewable_adoption):
    ax1.text(x, y + 2, f'{y}%', ha='center', va='bottom', fontsize=10, color='seagreen')

# Legend for both lines
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=12)

# Add a subtle background gradient
ax1.set_facecolor('#f7f7f9')
ax2.set_facecolor('#f7f7f9')

# Add trend line for renewable adoption
z = np.polyfit(years, renewable_adoption, 2)
p = np.poly1d(z)
ax1.plot(years, p(years), color='limegreen', linestyle=':', linewidth=1.5, label='Trend Line')

# Adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()