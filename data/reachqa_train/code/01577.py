import matplotlib.pyplot as plt
import numpy as np

# Data Setup
years = np.arange(2013, 2024)
ev_count = [500, 800, 1200, 1800, 2500, 3500, 5000, 7500, 11000, 16000, 23000]

# Calculate year-over-year growth rate in percentage
growth_rate = [0] + [((ev_count[i] - ev_count[i-1]) / ev_count[i-1]) * 100 for i in range(1, len(ev_count))]

# Significant events to annotate
events = {
    2015: "First Govt\nIncentives",
    2018: "Battery\nTech Breakthrough",
    2021: "EV Mandate\nPolicy"
}

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the line chart for EV count
color = 'teal'
ax1.plot(years, ev_count, marker='o', color=color, linestyle='-', linewidth=2, markersize=8, label='EV Count')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Electric Vehicles', fontsize=12, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Annotate significant events
for year, event in events.items():
    ax1.annotate(event,
                 xy=(year, ev_count[year-2013]),
                 xytext=(year, ev_count[year-2013] + 2500),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=10, color='darkred', ha='center')

# Add text annotations for each data point
for i, count in enumerate(ev_count):
    ax1.text(years[i], count + 500, f'{count:,}', fontsize=9, ha='center', color='navy')

# Create secondary y-axis for growth rate
ax2 = ax1.twinx()
color = 'orange'
ax2.bar(years, growth_rate, color=color, alpha=0.6, width=0.5, label='Growth Rate (%)')
ax2.set_ylabel('Year-over-Year Growth Rate (%)', fontsize=12, color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Add title and subtitle
plt.title("The Rise of Electric Vehicle Adoption in Electrica\nA Decade of Growth (2013-2023)", 
          fontsize=16, fontweight='bold')

# Legends
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), bbox_transform=ax1.transAxes)

# Grid and layout adjustment
ax1.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Show plot
plt.show()