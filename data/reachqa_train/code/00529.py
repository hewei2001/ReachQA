import matplotlib.pyplot as plt
import numpy as np

# Data for the horizontal bar chart
countries = ['Brewlandia', 'Arabicano', 'Cappuccinia', 'Espressovia', 'Mocharia', 'Lattelina']
coffee_consumption = [450, 320, 210, 570, 300, 380]
brewing_methods = ['French Press', 'Drip', 'Pour-over', 'Espresso', 'Moka Pot', 'Cold Brew']

# Generate colors for each country from a colormap
colors = plt.cm.viridis(np.linspace(0, 1, len(countries)))

# Create the horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(countries, coffee_consumption, color=colors, height=0.7)

# Annotate bars with the preferred brewing method
for bar, method in zip(bars, brewing_methods):
    ax.text(bar.get_width() + 10, bar.get_y() + bar.get_height() / 2,
            f'{method}', ha='left', va='center', fontsize=9, fontweight='bold')

# Annotate bars with the coffee consumption values
for bar in bars:
    ax.text(bar.get_width() - 30, bar.get_y() + bar.get_height() / 2,
            f'{bar.get_width()}', ha='center', va='center', color='white', fontsize=9)

# Add title and labels
ax.set_title("Coffee Consumption Across Cafferia:\nA Yearly Snapshot", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Cups of Coffee Consumed (Thousands)", fontsize=12)
ax.set_ylabel("Country", fontsize=12)

# Customize grid and background
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_facecolor('#f9f9f9')

# Customize tick parameters
ax.tick_params(axis='y', which='major', labelsize=11)
ax.tick_params(axis='x', which='major', labelsize=10)

# Set x-axis limits for a snug fit
ax.set_xlim(0, max(coffee_consumption) + 100)

# Display the plot
plt.tight_layout()
plt.show()