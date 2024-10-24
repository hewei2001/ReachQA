import matplotlib.pyplot as plt
import numpy as np

# Years and average internet speeds in Mbps
years = np.array([2005, 2008, 2010, 2012, 2015, 2018, 2020])
internet_speeds = [0.2, 1.4, 5, 10, 45, 100, 150]

# Milestones with annotations for specific years
milestones = {
    2005: 'Edge Technology',
    2008: 'Intro 3G',
    2012: '4G Adoption',
    2020: '5G Launch'
}

# Plot initialization
fig, ax = plt.subplots(figsize=(12, 6))

# Line plot with markers
ax.plot(years, internet_speeds, marker='o', color='mediumblue', linestyle='-', linewidth=2, label='Avg Internet Speed')

# Annotate milestones with arrows and text
for year, label in milestones.items():
    ax.annotate(label, xy=(year, internet_speeds[years.tolist().index(year)]),
                xytext=(-40, 15), textcoords='offset points',
                arrowprops=dict(arrowstyle='->', color='gray'),
                fontsize=10, color='darkred')

# Title and labels
ax.set_title('Evolution of Mobile Internet Speeds\n(2005-2020)', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Internet Speed (Mbps)', fontsize=12)

# Adding grid for better readability
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Set limits and ticks
ax.set_xlim(2005, 2021)
ax.set_xticks(years)
ax.set_ylim(0, 160)

# Legend placement
ax.legend(loc='upper left')

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()