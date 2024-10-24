import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Define cities and their corresponding attendance numbers
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'San Francisco']
attendance = np.array([150000, 120000, 110000, 90000, 85000])

# Construct related data for the line plot - Attendance growth rates over the years
years = np.array([2020, 2021, 2022, 2023])
growth_rates = {
    'New York': [0.05, 0.08, 0.06, 0.10],
    'Los Angeles': [0.04, 0.06, 0.05, 0.09],
    'Chicago': [0.03, 0.07, 0.06, 0.08],
    'Houston': [0.02, 0.05, 0.04, 0.07],
    'San Francisco': [0.01, 0.04, 0.03, 0.06]
}

# Create a figure with subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [2, 3]})

# Plot the bar chart
bar_positions = np.arange(len(cities))
bars = axs[0].bar(bar_positions, attendance, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], width=0.6)

for bar, city in zip(bars, cities):
    height = bar.get_height()
    axs[0].annotate(f'{height:,}', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, color='black')
    
axs[0].set_title('2023 Arts Festival Attendance\nAcross Major Cities', fontsize=14, fontweight='bold')
axs[0].set_xlabel('City', fontsize=11)
axs[0].set_ylabel('Number of Attendees', fontsize=11)
axs[0].set_xticks(bar_positions)
axs[0].set_xticklabels(cities, rotation=45, ha='right', fontsize=9)
axs[0].yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{int(x):,}"))
axs[0].yaxis.grid(True, linestyle='--', alpha=0.6)

# Plot the line chart for growth rates
for city, rates in growth_rates.items():
    axs[1].plot(years, rates, marker='o', label=city)

axs[1].set_title('Annual Attendance Growth Rates\n(2020-2023)', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=11)
axs[1].set_ylabel('Growth Rate', fontsize=11)
axs[1].set_xticks(years)
axs[1].yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:.0%}"))
axs[1].legend(title="Cities", loc='upper left', fontsize=9)
axs[1].grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()