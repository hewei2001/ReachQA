import matplotlib.pyplot as plt
import numpy as np

# Years and average internet speeds in Mbps
years = np.array([2005, 2008, 2010, 2012, 2015, 2018, 2020])
internet_speeds = [0.2, 1.4, 5, 10, 45, 100, 150]

# Number of mobile internet users (in billions) for secondary y-axis
internet_users = [0.5, 1.0, 1.4, 2.1, 3.0, 4.1, 5.0]

# Milestones with annotations for specific years
milestones = {
    2005: 'Edge Technology',
    2008: 'Intro 3G',
    2012: '4G Adoption',
    2020: '5G Launch'
}

# Plot initialization
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plotting internet speeds
color = 'mediumblue'
ax1.plot(years, internet_speeds, marker='o', linestyle='-', linewidth=2, color=color, label='Avg Internet Speed (Mbps)')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Internet Speed (Mbps)', color=color, fontsize=12)
ax1.tick_params(axis='y', labelcolor=color)

# Shaded regions to highlight eras
ax1.axvspan(2005, 2007, color='lightgray', alpha=0.2, label='Pre-3G Era')
ax1.axvspan(2008, 2011, color='lightblue', alpha=0.2, label='3G Era')
ax1.axvspan(2012, 2019, color='lightgreen', alpha=0.2, label='4G Era')
ax1.axvspan(2020, 2020, color='lightcoral', alpha=0.2, label='5G Era')

# Annotate milestones
for year, label in milestones.items():
    ax1.annotate(label, xy=(year, internet_speeds[years.tolist().index(year)]),
                 xytext=(-50, 20), textcoords='offset points',
                 arrowprops=dict(arrowstyle='->', color='gray'),
                 fontsize=10, color='darkred', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

# Secondary y-axis for number of users
ax2 = ax1.twinx()
color = 'darkgreen'
ax2.plot(years, internet_users, marker='x', linestyle='--', linewidth=2, color=color, label='Internet Users (Billion)')
ax2.set_ylabel('Internet Users (Billion)', color=color, fontsize=12)
ax2.tick_params(axis='y', labelcolor=color)

# Title
ax1.set_title('Evolution of Mobile Internet Speeds and Users (2005-2020)\nHighlighting Technology Milestones', fontsize=16, fontweight='bold', pad=15)

# Grid and limits
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.set_xlim(2005, 2021)
ax1.set_xticks(years)
ax1.set_ylim(0, 160)
ax2.set_ylim(0, 6)

# Legend
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.85))

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()