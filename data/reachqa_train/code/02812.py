import matplotlib.pyplot as plt
import numpy as np

# Define the renewable energy data
energy_types = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass']
current_shares = [22, 24, 35, 9, 10]

# Projected growth percentages over the next decade
projected_growth = [1.5, 2.0, 0.8, 1.1, 0.9]  # Assumed annual growth rates in %

# Project future shares based on simple growth model
future_shares = [current * (1 + growth * 10 / 100) for current, growth in zip(current_shares, projected_growth)]

# Define colors for energy types and bar chart
colors = ['#ffcc00', '#66c2a5', '#8da0cb', '#e78ac3', '#a6d854']
bar_colors = ['#ff8c00', '#5ab4ac', '#3b62f8', '#c51b8a', '#6dac20']

# Create a figure and axis for the pie chart
fig, ax1 = plt.subplots(figsize=(12, 8))
explode = [0, 0, 0.1, 0, 0]

# Plot the pie chart
wedges, texts, autotexts = ax1.pie(
    current_shares,
    labels=energy_types,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    explode=explode,
    shadow=True
)

# Customize label and text appearance
plt.setp(texts, size=10, weight='bold')
plt.setp(autotexts, size=9, weight='bold', color='white')

# Title and legend for the pie chart
plt.title(
    "Current and Projected Future Shares of Renewable Energy Production by Type\n"
    "Moving Towards a Sustainable Energy Future",
    fontsize=14,
    fontweight='bold',
    pad=20
)

ax1.legend(wedges, energy_types, title="Energy Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Ensure pie chart maintains a circular shape
ax1.axis('equal')

# Create a twin axes on the right for the bar chart
ax2 = ax1.twinx()

# Plot the bar chart
x = np.arange(len(energy_types))
ax2.bar(x, future_shares, color=bar_colors, alpha=0.6, width=0.4, label='Projected Future Shares')
ax2.set_ylim(0, max(future_shares) + 10)

# Add labels and customize the secondary axis
ax2.set_ylabel('Projected Share (%)', fontsize=12, weight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(energy_types)
ax2.legend(loc="upper right")

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()