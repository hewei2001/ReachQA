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

# Initialize plot
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.6

# Stacking bars for consumption and leftovers
p1 = ax.bar(months, craft_beer_consumption, bar_width, label='Craft Beer Consumed', color='dodgerblue', alpha=0.85)
p2 = ax.bar(months, herbal_tea_consumption, bar_width, bottom=craft_beer_consumption, label='Herbal Tea Consumed', color='mediumseagreen', alpha=0.85)
p3 = ax.bar(months, organic_coffee_consumption, bar_width, bottom=np.array(craft_beer_consumption) + np.array(herbal_tea_consumption), label='Organic Coffee Consumed', color='goldenrod', alpha=0.85)

p4 = ax.bar(months, craft_beer_leftover, bar_width, bottom=craft_beer_consumption, label='Craft Beer Leftover', color='lightblue', alpha=0.6, hatch='//')
p5 = ax.bar(months, herbal_tea_leftover, bar_width, bottom=np.array(craft_beer_consumption) + np.array(herbal_tea_consumption), label='Herbal Tea Leftover', color='lightgreen', alpha=0.6, hatch='//')
p6 = ax.bar(months, organic_coffee_leftover, bar_width, bottom=np.array(craft_beer_consumption) + np.array(herbal_tea_consumption) + np.array(organic_coffee_consumption), label='Organic Coffee Leftover', color='khaki', alpha=0.6, hatch='//')

# Titles and labels
ax.set_title("Artisan Beverage Trends: Production vs. Consumption", fontsize=16, fontweight='bold')
ax.set_xlabel("Months", fontsize=12)
ax.set_ylabel("Volume (Liters)", fontsize=12)

# Grid for readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Legend
ax.legend(loc='upper left', fontsize=10, title='Beverage Status')

# Rotate x-ticks for better visibility
plt.xticks(rotation=45)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()