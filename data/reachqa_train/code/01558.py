import matplotlib.pyplot as plt
import numpy as np

# Data setup
countries = ['Germany', 'China', 'USA', 'Brazil', 'India']
renewable_sources = ['Wind', 'Solar', 'Hydro']
percentages = {
    'Wind': [30, 15, 20, 35, 10],
    'Solar': [15, 10, 15, 25, 15],
    'Hydro': [11, 13, 10, 17, 5]
}
# Calculate remaining for simplicity, assuming percentages should sum up to 56, 38, 45, 77, and 30 respectively
remaining = [56 - sum(x) for x in zip(percentages['Wind'], percentages['Solar'], percentages['Hydro'])]
percentages['Other'] = remaining

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))

# Positions for each country
bar_positions = np.arange(len(countries))

# Initialize bottom for stacking bars
cumulative_bottom = np.zeros(len(countries))

# Colors for the segments
colors = ['#4CAF50', '#FFD700', '#FF5722', '#9C27B0']

# Plot each segment of the bar
for idx, (source, color) in enumerate(zip(percentages, colors)):
    ax.barh(bar_positions, percentages[source], left=cumulative_bottom, color=color, edgecolor='black', label=source)
    # Update cumulative bottom for the next stack
    cumulative_bottom += np.array(percentages[source])

# Annotate each segment with its percentage value
for i, country in enumerate(countries):
    cumulative_value = 0
    for source in renewable_sources + ['Other']:
        val = percentages[source][i]
        if val > 0:  # Only annotate non-zero values
            ax.text(cumulative_value + val/2, i, f'{val}%', ha='center', va='center', color='white', weight='bold')
        cumulative_value += val

# Labels and title
ax.set_yticks(bar_positions)
ax.set_yticklabels(countries)
ax.set_xlabel("Percentage of Total Renewable Energy", fontsize=12)
ax.set_title("Distribution of Renewable Energy Sources by Country (2023)", fontsize=16, weight='bold')

# Set x-axis range to 0-100%
ax.set_xlim(0, 100)

# Legend
ax.legend(title="Renewable Energy Source", bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout for better readability
plt.tight_layout()

# Show plot
plt.show()