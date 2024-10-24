import matplotlib.pyplot as plt
import numpy as np

# Define months for the chart
months = ["January", "February", "March", "April", "May", "June"]

# Define production data (in liters)
craft_beer_production = [120, 135, 150, 160, 180, 190]
herbal_tea_production = [110, 130, 125, 140, 145, 155]
organic_coffee_production = [140, 150, 160, 155, 170, 175]

# Define consumption data (in liters)
craft_beer_consumption = [100, 120, 130, 140, 160, 170]
herbal_tea_consumption = [90, 110, 115, 120, 130, 145]
organic_coffee_consumption = [130, 145, 150, 140, 160, 165]

# Compute leftover (production - consumption)
craft_beer_leftover = np.array(craft_beer_production) - np.array(craft_beer_consumption)
herbal_tea_leftover = np.array(herbal_tea_production) - np.array(herbal_tea_consumption)
organic_coffee_leftover = np.array(organic_coffee_production) - np.array(organic_coffee_consumption)

# Compute efficiency (consumption / production)
craft_beer_efficiency = np.array(craft_beer_consumption) / np.array(craft_beer_production)
herbal_tea_efficiency = np.array(herbal_tea_consumption) / np.array(herbal_tea_production)
organic_coffee_efficiency = np.array(organic_coffee_consumption) / np.array(organic_coffee_production)

# Initialize plot with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Subplot 1: Stacked bar chart of production vs. consumption
bar_width = 0.6

p1 = ax1.bar(months, craft_beer_consumption, bar_width, label='Craft Beer Consumed', color='dodgerblue', alpha=0.85)
p2 = ax1.bar(months, herbal_tea_consumption, bar_width, bottom=craft_beer_consumption, label='Herbal Tea Consumed', color='mediumseagreen', alpha=0.85)
p3 = ax1.bar(months, organic_coffee_consumption, bar_width, bottom=np.array(craft_beer_consumption) + np.array(herbal_tea_consumption), label='Organic Coffee Consumed', color='goldenrod', alpha=0.85)

p4 = ax1.bar(months, craft_beer_leftover, bar_width, bottom=craft_beer_consumption, label='Craft Beer Leftover', color='lightblue', alpha=0.6, hatch='//')
p5 = ax1.bar(months, herbal_tea_leftover, bar_width, bottom=np.array(craft_beer_consumption) + np.array(herbal_tea_consumption), label='Herbal Tea Leftover', color='lightgreen', alpha=0.6, hatch='//')
p6 = ax1.bar(months, organic_coffee_leftover, bar_width, bottom=np.array(craft_beer_consumption) + np.array(herbal_tea_consumption) + np.array(organic_coffee_consumption), label='Organic Coffee Leftover', color='khaki', alpha=0.6, hatch='//')

# Titles and labels for subplot 1
ax1.set_title("Artisan Beverage Trends:\nProduction vs. Consumption", fontsize=14, fontweight='bold')
ax1.set_xlabel("Months", fontsize=12)
ax1.set_ylabel("Volume (Liters)", fontsize=12)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.legend(loc='upper left', fontsize=10, title='Beverage Status')
ax1.tick_params(axis='x', rotation=45)

# Subplot 2: Line plot for efficiency
ax2.plot(months, craft_beer_efficiency, marker='o', label='Craft Beer Efficiency', color='dodgerblue')
ax2.plot(months, herbal_tea_efficiency, marker='s', label='Herbal Tea Efficiency', color='mediumseagreen')
ax2.plot(months, organic_coffee_efficiency, marker='^', label='Organic Coffee Efficiency', color='goldenrod')

# Titles and labels for subplot 2
ax2.set_title("Efficiency Trends:\nConsumption/Production Ratio", fontsize=14, fontweight='bold')
ax2.set_xlabel("Months", fontsize=12)
ax2.set_ylabel("Efficiency Ratio", fontsize=12)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.legend(loc='best', fontsize=10)
ax2.tick_params(axis='x', rotation=45)

# Adjust layout for better visualization
plt.tight_layout()

# Display the plots
plt.show()