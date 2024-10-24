import matplotlib.pyplot as plt
import numpy as np

# Data for the original bar chart
industries = ['Manufacturing', 'Healthcare', 'Agriculture', 'Logistics', 'Retail']
robotics_utilization = [75, 50, 30, 60, 40]  # Utilization percentage

# Data for the secondary plot - growth rates over a span of years
years = np.arange(2015, 2021)
growth_rates = {
    'Manufacturing': [10, 12, 15, 18, 20, 25],
    'Healthcare': [5, 8, 10, 15, 20, 25],
    'Agriculture': [2, 3, 4, 5, 6, 7],
    'Logistics': [6, 8, 10, 12, 15, 18],
    'Retail': [3, 5, 7, 8, 10, 12]
}

# Create a figure with 1x2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [1, 1.2]})

# First plot: Bar chart
positions = np.arange(len(industries))
bars = ax1.bar(positions, robotics_utilization, color=['steelblue', 'lightcoral', 'forestgreen', 'gold', 'mediumorchid'], width=0.6)

# Annotate bars
for bar in bars:
    yval = bar.get_height()
    ax1.text(
        bar.get_x() + bar.get_width() / 2, yval + 2,
        f'{yval}%', ha='center', va='bottom', fontsize=10, fontweight='bold'
    )

# Title and axis labels for bar chart
ax1.set_title('Robotics Utilization Across Industries', fontsize=14, fontweight='bold')
ax1.set_xlabel('Industry', fontsize=12)
ax1.set_ylabel('Utilization (%)', fontsize=12)

# Customize x-ticks for bar chart
ax1.set_xticks(positions)
ax1.set_xticklabels(industries, rotation=45, ha='right')

# Add grid lines for the bar chart
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.set_axisbelow(True)

# Second plot: Line chart showing growth rates
for industry, rates in growth_rates.items():
    ax2.plot(years, rates, marker='o', label=industry)

# Title and axis labels for line chart
ax2.set_title('Growth Rate of Robotics Utilization\n(2015-2020)', fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)

# Customize legend and grid for line chart
ax2.legend(title='Industry', fontsize=9)
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)
ax2.set_axisbelow(True)

# Enhance layout
plt.tight_layout()
plt.show()