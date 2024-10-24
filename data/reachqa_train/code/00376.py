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

# Colors for each energy type
colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF6347']

# Plotting configuration
fig, ax = plt.subplots(figsize=(10, 7))
bar_width = 0.6
cumulative_data = np.zeros(len(countries))

# Plot each renewable energy source
for idx, (source, contributions) in enumerate(renewable_data.items()):
    ax.barh(countries, contributions, left=cumulative_data, color=colors[idx], label=source, height=bar_width)
    cumulative_data += np.array(contributions)

# Annotate each bar with the data value
for i, country in enumerate(countries):
    for j, source in enumerate(renewable_data.keys()):
        contribution = renewable_data[source][i]
        ax.text(contribution/2 + sum(list(renewable_data[source][:j])), i, f'{contribution}%', 
                va='center', ha='center', color='white', fontsize=9)

# Additional plot details
ax.set_xlabel('Percentage Contribution (%)', fontsize=12)
ax.set_title('Projected Contribution of Renewable Energy Sources\n to Europe\'s 2030 Energy Grid', fontsize=14, fontweight='bold', pad=15)
ax.invert_yaxis()  # Highest contributor at the top
ax.set_xlim(0, 100)  # Assuming the total is 100%
ax.legend(title='Energy Sources', loc='lower right', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.6, axis='x')

# Enhance visibility of labels and adjust layout
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
plt.tight_layout()

# Display the plot
plt.show()