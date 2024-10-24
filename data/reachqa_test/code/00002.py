import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
years = ['2019', '2020', '2021', '2022', '2023']
adoption_rates = {
    'Electric Scooters': [15, 25, 40, 50, 60],
    'Autonomous Cars': [5, 10, 20, 35, 50],
    'Hyperloop Travel': [0, 5, 10, 20, 30],
    'Flying Taxis': [0, 0, 5, 10, 20]
}

# Constructing related data for the overlay line plot
# Here, we consider the average adoption rate across all technologies
average_adoption_rate = [np.mean([adoption_rates[tech][i] for tech in adoption_rates]) for i in range(len(years))]

# Colors for the bars
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8']
x = np.arange(len(years))
width = 0.2  # Width of the bars

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 8))

# Create bars for each technology
for i, (technology, rates) in enumerate(adoption_rates.items()):
    ax1.bar(x + i * width, rates, width, label=technology, color=colors[i])

# Annotate each bar with the data value
for i, (technology, rates) in enumerate(adoption_rates.items()):
    for j, rate in enumerate(rates):
        ax1.text(x[j] + i * width, rate + 1, f'{rate}%', ha='center', va='bottom', fontsize=8, color='black')

# Line plot overlay for average adoption rates
ax2 = ax1.twinx()
ax2.plot(x + width * 1.5, average_adoption_rate, marker='o', linestyle='-', color='black', label='Average Adoption Rate')
ax2.set_ylabel('Average Adoption Rate (%)', fontsize=12, color='black')

# Annotate the line plot with data values
for j, rate in enumerate(average_adoption_rate):
    ax2.text(x[j] + width * 1.5, rate + 1, f'{rate:.1f}%', ha='center', va='bottom', fontsize=8, color='black')

# Setting title and labels
ax1.set_title('Adoption Rates of Future Transport Technologies\nin Futureville (2019-2023)', fontsize=14)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Adoption Rate (%)', fontsize=12)
ax1.set_xticks(x + width * 1.5)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left', fontsize=10)

# Customize the grid and style
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
ax1.set_axisbelow(True)

# Ensure both legends do not overlap
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2)

# Adjust layout to fit all elements
plt.tight_layout()

# Display the chart
plt.show()