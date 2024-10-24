import matplotlib.pyplot as plt
import numpy as np

# Country names
countries = ['United States', 'China', 'Russia', 'India', 'EU']

# Investment data in billions of USD for each target
moon_investment = np.array([45, 30, 20, 15, 25])
mars_investment = np.array([50, 35, 25, 20, 30])
asteroid_investment = np.array([20, 15, 10, 8, 12])

# Stack the data for the chart
investment_data = np.vstack([moon_investment, mars_investment, asteroid_investment])

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(14, 9))

# Plot the bars with gradient-style coloring using hatching
bar_width = 0.6
ax.bar(countries, moon_investment, label='Moon', color='silver', edgecolor='grey', width=bar_width, hatch='//')
ax.bar(countries, mars_investment, bottom=moon_investment, label='Mars', color='darkorange', edgecolor='grey', width=bar_width, hatch='..')
ax.bar(countries, asteroid_investment, bottom=moon_investment+mars_investment, label='Asteroids', color='darkred', edgecolor='grey', width=bar_width, hatch='xx')

# Title and labels
ax.set_title('2030 Space Exploration Investment by Country\nAllocated to Moon, Mars, and Asteroid Exploration', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Investment (Billion USD)', fontsize=14)
ax.set_xlabel('Countries', fontsize=14)

# Add a secondary y-axis to show the percentage of total investment
total_investment = np.sum(investment_data)
ax2 = ax.twinx()
ax2.set_ylim(0, 130)
ax2.set_yticks(np.arange(0, 131, 10))
ax2.set_yticklabels([f'{int(y/total_investment*100)}%' for y in np.arange(0, 131, 10)])
ax2.set_ylabel('Percentage of Total Global Investment', fontsize=14, rotation=270, labelpad=15)

# Adding a legend
ax.legend(title='Exploration Targets', fontsize=12, loc='upper left', bbox_to_anchor=(1, 1), frameon=False)

# Add gridlines
ax.yaxis.grid(True, linestyle='--', alpha=0.5)

# Annotate total investments above bars with percentages
for idx, total in enumerate(np.sum(investment_data, axis=0)):
    ax.text(idx, total + 2, f'{total}B\n({int(total/total_investment*100)}%)', ha='center', va='bottom', fontsize=11, fontweight='bold', color='black')

# Rotate x-axis labels
ax.set_xticklabels(countries, rotation=45, ha='right')

# Ensure layout is tight
plt.tight_layout()

# Show the plot
plt.show()