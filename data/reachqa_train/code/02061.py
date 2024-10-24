import matplotlib.pyplot as plt

# Data for coffee consumption by type (percentages)
coffee_types = ['Espresso', 'Cappuccino', 'Latte', 'Americano', 'Mocha']
consumption = [25, 15, 30, 10, 20]

# Define colors for each type of coffee
colors = ['#8B4513', '#D2691E', '#F5DEB3', '#C0C0C0', '#8B0000']

# Create the ring chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))

# Plot the data with the ring (donut) effect
wedges, texts, autotexts = ax.pie(
    consumption, labels=coffee_types, colors=colors,
    autopct='%1.1f%%', startangle=140, pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Draw the central label
plt.text(0, 0, 'Global Coffee\nConsumption', horizontalalignment='center', 
         verticalalignment='center', fontsize=14, weight='bold', color='darkblue')

# Formatting for text labels
plt.setp(autotexts, size=10, weight="bold", color="darkblue")
ax.set_title("Global Coffee Consumption by Beverage Type", fontsize=14, weight='bold')

# Customize legend to prevent occlusion
ax.legend(wedges, coffee_types, title="Coffee Types", loc='center left', 
          bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10, title_fontsize='11')

# Adjust layout
plt.tight_layout()

# Display the ring chart
plt.show()