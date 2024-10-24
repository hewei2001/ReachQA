import matplotlib.pyplot as plt
import numpy as np

# Data Construction
years = np.array([2017, 2018, 2019, 2020, 2021])
almond_milk = np.array([200, 220, 250, 290, 350])  # Millions of Liters
soy_milk = np.array([180, 190, 210, 240, 270])     # Millions of Liters
oat_milk = np.array([50, 70, 100, 150, 200])       # Millions of Liters
coconut_milk = np.array([30, 40, 60, 80, 110])     # Millions of Liters

# Calculate total consumption and percentage growth
total_consumption = almond_milk + soy_milk + oat_milk + coconut_milk
growth_rate = np.append([0], np.diff(total_consumption) / total_consumption[:-1] * 100)  # % growth, first year set to 0%

# Stacked Bar Chart Plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Stack the bars
ax1.bar(years, almond_milk, label='Almond Milk', color='#A3E4D7', edgecolor='white')
ax1.bar(years, soy_milk, bottom=almond_milk, label='Soy Milk', color='#F7DC6F', edgecolor='white')
ax1.bar(years, oat_milk, bottom=almond_milk + soy_milk, label='Oat Milk', color='#F5B7B1', edgecolor='white')
ax1.bar(years, coconut_milk, bottom=almond_milk + soy_milk + oat_milk, label='Coconut Milk', color='#D2B4DE', edgecolor='white')

# Labels and title
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Consumption (Millions of Liters)', fontsize=12)
ax1.set_title('The Rise in Plant-Based Beverage Consumption\nand Growth Rate (2017-2021)', 
              fontsize=16, fontweight='bold', color='navy')
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 901, 100))

# Add secondary y-axis for growth rate
ax2 = ax1.twinx()
ax2.plot(years, growth_rate, color='darkred', marker='o', linestyle='-', linewidth=2, markersize=8, label='Growth Rate')
ax2.set_ylabel('Growth Rate (%)', fontsize=12, color='darkred')
ax2.tick_params(axis='y', labelcolor='darkred')
ax2.set_ylim(-5, 35)

# Display the legends
ax1.legend(loc='upper left', title='Beverage Type', fontsize=10)
ax2.legend(loc='upper right', title='Growth Rate', fontsize=10)

# Grid settings for better readability
ax1.yaxis.grid(True, linestyle='--', which='both', color='grey', alpha=0.5)

# Rotate x-ticks labels for better readability
plt.xticks(rotation=45)

# Annotate percentage growth points
for i, growth in enumerate(growth_rate):
    ax2.annotate(f'{growth:.1f}%', (years[i], growth_rate[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='darkred')

# Automatically adjust layout to fit elements
plt.tight_layout()

# Show plot
plt.show()