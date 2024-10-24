import matplotlib.pyplot as plt
import numpy as np

# Expanded data setup
countries = ['Germany', 'China', 'USA', 'Brazil', 'India', 'Japan', 'Canada', 'France', 'Australia', 'South Africa']
renewable_sources = ['Wind', 'Solar', 'Hydro', 'Geothermal', 'Biomass']
percentages = {
    'Wind': [30, 15, 20, 35, 10, 25, 45, 33, 15, 10],
    'Solar': [15, 10, 15, 25, 15, 20, 30, 22, 18, 5],
    'Hydro': [11, 13, 10, 17, 5, 13, 25, 20, 10, 8],
    'Geothermal': [2, 3, 1, 0, 7, 6, 4, 5, 2, 1],
    'Biomass': [4, 2, 5, 5, 3, 4, 6, 7, 5, 6],
}

# Calculate remaining energy that exceeds 100%
remaining = [max(0, 110 - sum(x)) for x in zip(*percentages.values())]
percentages['Other'] = remaining

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Positions for each country
bar_positions = np.arange(len(countries))

# Initialize bottom for stacking bars
cumulative_bottom = np.zeros(len(countries))

# Colors for the segments
colors = ['#4CAF50', '#FFD700', '#FF5722', '#9C27B0', '#3F51B5', '#00BCD4']

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
        if val > 2:  # Annotate only meaningful values to avoid clutter
            ax.text(cumulative_value + val/2, i, f'{val}%', ha='center', va='center', color='white', weight='bold')
        cumulative_value += val

# Labels and title
ax.set_yticks(bar_positions)
ax.set_yticklabels(countries)
ax.set_xlabel("Percentage of Total Renewable Energy", fontsize=12)
ax.set_title("Complex Distribution of Renewable Energy Sources by Country\n(2023 - Incorporating Overlapping Contributions)", fontsize=14, weight='bold')

# Set x-axis range to accommodate the potential overflow beyond 100%
ax.set_xlim(0, 120)

# Legend
ax.legend(title="Renewable Energy Source", bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout for better readability
plt.tight_layout()

# Show plot
plt.show()