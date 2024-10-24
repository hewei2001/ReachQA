import matplotlib.pyplot as plt
import numpy as np

# Define space agencies and their fictional exoplanet discovery counts
agencies = ['NASA', 'ESA', 'CNSA', 'ISRO', 'Roscosmos']
discovery_counts = np.array([320, 245, 198, 152, 180])

# Define colors for the bars for visual distinction
bar_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create positions for the bars on the x-axis
positions = np.arange(len(agencies))

# Cumulative discovery data (fictional) over the years
cumulative_discoveries = np.array([1000, 850, 700, 500, 600])
line_color = '#17becf'
line_marker = 'o'

# Create the figure and a set of subplots
fig, ax1 = plt.subplots(figsize=(12, 8))

# Create the bar chart
bars = ax1.bar(positions, discovery_counts, color=bar_colors, width=0.6, label='Annual Discoveries')

# Set x-ticks and labels
ax1.set_xticks(positions)
ax1.set_xticklabels(agencies, fontsize=12)

# Set the y-axis label for the bar chart
ax1.set_ylabel('Annual Discoveries', fontsize=14)
ax1.set_ylim(0, max(discovery_counts) + 50)

# Add y-axis grid lines for improved readability
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Create a second y-axis for the line plot
ax2 = ax1.twinx()

# Create the line plot
line = ax2.plot(positions, cumulative_discoveries, color=line_color, marker=line_marker, linestyle='-', linewidth=2, label='Cumulative Discoveries')

# Set the y-axis label for the line plot
ax2.set_ylabel('Cumulative Discoveries', fontsize=14, color=line_color)
ax2.tick_params(axis='y', labelcolor=line_color)
ax2.set_ylim(0, max(cumulative_discoveries) + 200)

# Annotate each bar with its value
for bar, count in zip(bars, discovery_counts):
    height = bar.get_height()
    ax1.annotate(f'{count}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5),  # Offset to display above the bar
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=10, color='black')

# Annotate the line plot
for i, cumulative in enumerate(cumulative_discoveries):
    ax2.annotate(f'{cumulative}', 
                 xy=(positions[i], cumulative), 
                 xytext=(5, 5), 
                 textcoords="offset points", 
                 ha='center', 
                 fontsize=10, color=line_color)

# Set the chart title
ax1.set_title('Exoplanet Discoveries by Major Space Agencies (2013-2023)\nAnnual vs Cumulative Insights', 
              fontsize=16, fontweight='bold', pad=20)

# Add a legend
bars_legend = ax1.legend(loc='upper left', frameon=False)
lines_legend = ax2.legend(loc='upper right', frameon=False)
fig.add_artist(bars_legend)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()