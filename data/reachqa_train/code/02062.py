import matplotlib.pyplot as plt
import numpy as np

# Expanded data set for coffee consumption by type (percentages)
coffee_types = [
    'Espresso', 'Cappuccino', 'Latte', 'Americano', 'Mocha', 
    'Flat White', 'Macchiato', 'Ristretto', 'Affogato', 'Irish Coffee'
]
consumption = [12, 15, 20, 10, 18, 8, 5, 4, 3, 5]
caffeine_content = [212, 150, 75, 95, 150, 105, 115, 120, 180, 100]  # in mg

# Define colors for each type of coffee
colors = ['#8B4513', '#D2691E', '#F5DEB3', '#C0C0C0', '#8B0000', 
          '#CD853F', '#8B0000', '#A0522D', '#8B4513', '#A52A2A']

# Create the ring chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(aspect="equal"))

# Plot the data with the ring (donut) effect
wedges, texts, autotexts = ax.pie(
    consumption, labels=coffee_types, colors=colors,
    autopct=lambda pct: f'{pct:.1f}%\n({int(pct/100*sum(consumption))}%)',
    startangle=140, pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Annotate caffeine content
for i, txt in enumerate(autotexts):
    txt.set_text(txt.get_text() + f"\n{caffeine_content[i]}mg")
    txt.set_color('darkblue')
    txt.set_fontsize(9)

# Draw the central label
plt.text(0, 0, 'Global Coffee\nConsumption\n(Caffeine Content)', 
         horizontalalignment='center', verticalalignment='center', 
         fontsize=14, weight='bold', color='darkblue')

# Formatting and title adjustments
ax.set_title("Global Coffee Consumption by Beverage Type\nand Caffeine Content",
             fontsize=14, weight='bold', va='top', pad=20)

# Customize legend to prevent occlusion
ax.legend(wedges, coffee_types, title="Coffee Types", loc='center left', 
          bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10, title_fontsize='11')

# Draw lines indicating caffeine content range
theta = np.linspace(0, 2 * np.pi, 100)
r1 = [0.5 * c/250 for c in caffeine_content]
r2 = [0.55 * c/250 for c in caffeine_content]
ax.plot(np.sin(theta), np.cos(theta), lw=2, linestyle='--', color='gray', alpha=0.7)

# Adjust layout for clarity
plt.tight_layout()

# Display the ring chart
plt.show()