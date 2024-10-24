import matplotlib.pyplot as plt
import numpy as np

# Data for the eco-friendly beverage production
beverages = ['Organic Tea', 'Herbal Infusion', 'Kombucha', 'Coconut Water', 'Aloe Vera Juice']
production_volumes = [55, 42, 63, 80, 37]  # Production volumes in millions of liters
colors = ['#8FD14F', '#FFD700', '#FF69B4', '#40E0D0', '#BA55D3']

# Plotting the bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(beverages, production_volumes, color=colors, alpha=0.85, edgecolor='black')

# Adding data annotations on each bar
for bar, volume in zip(bars, production_volumes):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 1, f'{volume}M', ha='center', va='bottom', fontsize=11, fontweight='bold')

# Title and labels
ax.set_title("Eco-Friendly Beverage Production\nA Year in Review", fontsize=16, fontweight='bold')
ax.set_xlabel("Beverage Type", fontsize=14)
ax.set_ylabel("Production Volume (Million Liters)", fontsize=14)

# Adding a legend to highlight the most produced beverage
most_produced_index = np.argmax(production_volumes)
ax.legend([bars[most_produced_index]], [beverages[most_produced_index]], title="Top Producer", loc='upper left', fontsize=10, frameon=False)

# Grid lines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()