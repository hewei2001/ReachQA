import matplotlib.pyplot as plt
import numpy as np

# Data: Number of employees and their coffee preferences at InnovateTech
coffee_types = ['Espresso', 'Americano', 'Cappuccino', 'Latte', 'Macchiato', 'Mocha']
preferences = [50, 30, 40, 60, 25, 45]

# Additional Data: Average daily coffee consumption per type
average_daily_consumption = [3.5, 2.7, 3.0, 4.1, 2.3, 3.2]

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Histogram for coffee preferences
bin_edges = np.arange(len(coffee_types) + 1) - 0.5
ax1.hist(range(len(coffee_types)), bins=bin_edges, weights=preferences,
         color='#6f4e37',  # Use a single color for all bars
         edgecolor='black', alpha=0.8)
ax1.set_title("Coffee Consumption Preferences\nat InnovateTech", fontsize=14, fontweight='bold')
ax1.set_xlabel("Type of Coffee", fontsize=12)
ax1.set_ylabel("Number of Employees", fontsize=12)
ax1.set_xticks(range(len(coffee_types)))
ax1.set_xticklabels(coffee_types, rotation=45, ha='right')
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
for i, v in enumerate(preferences):
    ax1.text(i, v + 1, str(v), ha='center', va='bottom', fontweight='bold', fontsize=10)

# Plot 2: Pie chart for average daily coffee consumption
ax2.pie(average_daily_consumption, labels=coffee_types, autopct='%1.1f%%', startangle=140, 
        colors=['#6f4e37', '#d2691e', '#8b4513', '#deb887', '#cd853f', '#a0522d'],
        wedgeprops={'edgecolor': 'black'})
ax2.set_title("Average Daily Coffee Consumption\nPer Type", fontsize=14, fontweight='bold')

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()