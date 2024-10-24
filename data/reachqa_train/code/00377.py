import matplotlib.pyplot as plt
import numpy as np

# List of countries
countries = ['Germany', 'France', 'Italy', 'Spain', 'Netherlands']

# Renewable energy contributions (in percentages) for each country
renewable_data = {
    'Solar': [35, 20, 40, 25, 30],
    'Wind': [30, 25, 20, 35, 40],
    'Hydroelectric': [20, 35, 15, 25, 15],
    'Biomass': [15, 20, 25, 15, 15]
}

# Growth projection (in percentages) for renewable energy sources by 2030
growth_projection = {
    'Solar': 40,
    'Wind': 35,
    'Hydroelectric': 15,
    'Biomass': 10
}

# Colors for each energy type
colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF6347']

# Setup figure with 2 subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 7))
fig.suptitle('Europe\'s Renewable Energy Landscape', fontsize=16, fontweight='bold', y=1.02)

# Plot 1: Horizontal Stacked Bar Chart
ax1 = axes[0]
bar_width = 0.6
cumulative_data = np.zeros(len(countries))

for idx, (source, contributions) in enumerate(renewable_data.items()):
    ax1.barh(countries, contributions, left=cumulative_data, color=colors[idx], label=source, height=bar_width)
    cumulative_data += np.array(contributions)

# Annotate bars
for i, country in enumerate(countries):
    cum_sum = 0
    for idx, source in enumerate(renewable_data.keys()):
        contribution = renewable_data[source][i]
        ax1.text(cum_sum + contribution / 2, i, f'{contribution}%', va='center', ha='center',
                 color='white', fontsize=9)
        cum_sum += contribution

ax1.set_xlabel('Percentage Contribution (%)', fontsize=12)
ax1.set_title('Projected Renewable Energy Contributions by Country', fontsize=12, pad=10)
ax1.invert_yaxis()
ax1.set_xlim(0, 100)
ax1.legend(title='Energy Sources', loc='lower right', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.6, axis='x')

# Plot 2: Pie Chart for Growth Projections
ax2 = axes[1]
ax2.pie(growth_projection.values(), labels=growth_projection.keys(), autopct='%1.1f%%', startangle=90, colors=colors)
ax2.set_title('2030 Growth Projections by Energy Source', fontsize=12, pad=10)

# Adjust layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()