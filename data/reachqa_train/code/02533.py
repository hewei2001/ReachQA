import matplotlib.pyplot as plt
import numpy as np

# Define the years and departments
years = np.arange(2015, 2021)
departments = ['Development', 'Marketing', 'Operations']

# Caffeine consumption data (units)
coffee_consumption = np.array([
    [80, 90, 95, 100, 105, 110],  # Development
    [60, 65, 70, 75, 80, 85],     # Marketing
    [40, 45, 50, 52, 53, 54]      # Operations
])

energy_drink_consumption = np.array([
    [30, 32, 34, 36, 38, 40],     # Development
    [10, 12, 15, 18, 20, 22],     # Marketing
    [5, 6, 8, 9, 10, 11]          # Operations
])

tea_consumption = np.array([
    [20, 22, 25, 28, 30, 32],     # Development
    [25, 27, 29, 32, 35, 37],     # Marketing
    [15, 16, 17, 18, 19, 20]      # Operations
])

# Calculate total consumption for annotations
total_consumption = coffee_consumption + energy_drink_consumption + tea_consumption

# Plotting the stacked bar chart
fig, ax = plt.subplots(figsize=(14, 9))

# Define bar positions
bar_width = 0.25
positions = np.array([-0.3, 0, 0.3])

# Colors
colors = [['#FF6F61', '#6B5B95', '#88B04B'], 
          ['#F7CAC9', '#92A8D1', '#955251'], 
          ['#B565A7', '#009B77', '#DD4124']]

# Plot each department's caffeine consumption
for i, department in enumerate(departments):
    ax.bar(years + positions[i], coffee_consumption[i], width=bar_width, label=f'Coffee ({department})', color=colors[i][0])
    ax.bar(years + positions[i], energy_drink_consumption[i], width=bar_width, bottom=coffee_consumption[i], color=colors[i][1])
    ax.bar(years + positions[i], tea_consumption[i], width=bar_width, bottom=coffee_consumption[i] + energy_drink_consumption[i], color=colors[i][2])
    
    # Annotate each bar with total consumption values
    for year_idx, year in enumerate(years):
        total_value = total_consumption[i, year_idx]
        ax.text(year + positions[i], total_value + 1, str(total_value), ha='center', va='bottom', fontsize=8, fontweight='bold')

# Set chart title and labels
ax.set_title("Caffeine Consumption Trends\nin Tech Startups (2015-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Caffeine Units Consumed", fontsize=12)

# Set x-ticks and labels
ax.set_xticks(years)
ax.set_xticklabels(years)

# Add legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title='Caffeine Source (Department)')

# Add gridlines for easier reading
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Highlight significant changes with arrows
for i, (start, end) in enumerate(zip(total_consumption[:, :-1], total_consumption[:, 1:])):
    for j, (s, e) in enumerate(zip(start, end)):
        if e - s > 15:  # Arbitrarily choosing a threshold for significant change
            ax.annotate('', xy=(years[j+1]+positions[i], e), xytext=(years[j]+positions[i], s),
                        arrowprops=dict(arrowstyle='->', lw=1.5, color=colors[i][0]))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()