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

# Plotting the stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot caffeine consumption for Development department
ax.bar(years - 0.3, coffee_consumption[0], width=0.3, label='Coffee (Development)', color='#FF6F61')
ax.bar(years - 0.3, energy_drink_consumption[0], width=0.3, bottom=coffee_consumption[0], color='#6B5B95')
ax.bar(years - 0.3, tea_consumption[0], width=0.3, bottom=coffee_consumption[0] + energy_drink_consumption[0], color='#88B04B')

# Plot caffeine consumption for Marketing department
ax.bar(years, coffee_consumption[1], width=0.3, label='Coffee (Marketing)', color='#F7CAC9')
ax.bar(years, energy_drink_consumption[1], width=0.3, bottom=coffee_consumption[1], color='#92A8D1')
ax.bar(years, tea_consumption[1], width=0.3, bottom=coffee_consumption[1] + energy_drink_consumption[1], color='#955251')

# Plot caffeine consumption for Operations department
ax.bar(years + 0.3, coffee_consumption[2], width=0.3, label='Coffee (Operations)', color='#B565A7')
ax.bar(years + 0.3, energy_drink_consumption[2], width=0.3, bottom=coffee_consumption[2], color='#009B77')
ax.bar(years + 0.3, tea_consumption[2], width=0.3, bottom=coffee_consumption[2] + energy_drink_consumption[2], color='#DD4124')

# Set chart title and labels
ax.set_title("Caffeine Consumption Trends in Tech Startups (2015-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Caffeine Units Consumed", fontsize=12)

# Set x-ticks and labels
ax.set_xticks(years)
ax.set_xticklabels(years)

# Add legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title='Caffeine Source (Department)')

# Add gridlines for easier reading
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()