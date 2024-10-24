import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2023
years = np.arange(2010, 2024)

# Synthetic data for snack consumption popularity (1-100 scale)
chips = [70, 68, 65, 62, 59, 56, 54, 52, 50, 48, 45, 42, 40, 38]
nuts = [30, 32, 34, 36, 39, 42, 45, 48, 52, 57, 62, 68, 74, 80]
fruit_snacks = [15, 18, 22, 26, 30, 36, 42, 50, 58, 66, 75, 85, 92, 100]

# Total snack consumption for different demographics in 2023
total_consumption = {
    'Chips': 38,
    'Nuts': 80,
    'Fruit Snacks': 100
}

# Creating the figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# First subplot: Line Chart
ax1.plot(years, chips, marker='o', linestyle='-', color='orange', label='Chips', linewidth=2)
ax1.plot(years, nuts, marker='o', linestyle='-', color='green', label='Nuts', linewidth=2)
ax1.plot(years, fruit_snacks, marker='o', linestyle='-', color='red', label='Fruit Snacks', linewidth=2)

ax1.set_title("Trends in Snack Consumption in Urban Areas\n2010-2023", fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Popularity Score (1-100)', fontsize=12)
ax1.legend(loc='upper left')
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.annotate('Peak Chips Popularity', xy=(2010, 70), xytext=(2012, 75),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='orange')
ax1.annotate('Nut Consumption Surges', xy=(2023, 80), xytext=(2021, 85),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='green')
ax1.annotate('Fruit Snacks Take Off!', xy=(2023, 100), xytext=(2021, 90),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='red')
ax1.set_xticks(years)

# Second subplot: Bar Chart for 2023 consumption
ax2.bar(total_consumption.keys(), total_consumption.values(), color=['orange', 'green', 'red'])
ax2.set_title("Snack Consumption in 2023", fontsize=16, fontweight='bold')
ax2.set_xlabel('Snack Type', fontsize=12)
ax2.set_ylabel('Total Consumption (Score)', fontsize=12)
ax2.set_ylim(0, 120)

# Adding percentage labels on the bars
for i, value in enumerate(total_consumption.values()):
    ax2.text(i, value + 2, f"{value}", ha='center', fontsize=10, color='black')

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()