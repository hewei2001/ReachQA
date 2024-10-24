import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
countries = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E']
tea_consumption = [2.5, 4.2, 1.8, 3.6, 2.9]

# Data for the line chart (hypothetical historical growth for Country A)
years = np.array([2018, 2019, 2020, 2021, 2022])
consumption_growth = np.array([1.8, 2.0, 2.3, 2.5, 2.8])

# Create figure and subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))

# Bar chart
x_pos = np.arange(len(countries))
colors = ['#B5651D', '#8B4513', '#A0522D', '#CD853F', '#D2691E']
bars = ax1.bar(x_pos, tea_consumption, color=colors, alpha=0.8, width=0.5)

for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2.0, height + 0.1,
             f'{height:.1f}', ha='center', va='bottom', fontsize=10)

ax1.set_title('Average Annual Tea Consumption\nPer Person by Country', fontsize=14, fontweight='bold')
ax1.set_xlabel('Country', fontsize=12)
ax1.set_ylabel('Tea Consumption (kg/person/year)', fontsize=12)
ax1.set_xticks(x_pos)
ax1.set_xticklabels(countries, rotation=30, ha='right', fontsize=10)
ax1.yaxis.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)

# Line chart
ax2.plot(years, consumption_growth, marker='o', linestyle='-', color='#6495ED', linewidth=2)
ax2.set_title('Historical Tea Consumption\nGrowth for Country A', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Tea Consumption (kg/person/year)', fontsize=12)
ax2.set_xticks(years)
ax2.yaxis.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)

# Annotations for the line chart
for year, consumption in zip(years, consumption_growth):
    ax2.text(year, consumption + 0.05, f'{consumption:.1f}', ha='center', va='bottom', fontsize=10)

# Adjust layout
plt.tight_layout()

# Show the chart
plt.show()