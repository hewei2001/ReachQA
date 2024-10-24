import matplotlib.pyplot as plt
import numpy as np

# Define renewable energy types and their corresponding investment amounts in billion USD
energy_types = ['Solar', 'Wind', 'Hydropower', 'Biomass', 'Geothermal']
investment_amounts = [120, 95, 70, 45, 20]  # Hypothetical values for 2023

# Colors for the bars
colors = ['#f9a825', '#29b6f6', '#66bb6a', '#8d6e63', '#ff7043']

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the investment bars
bars = ax.barh(energy_types, investment_amounts, color=colors, edgecolor='black')

# Add investment amount labels on the bars
for bar in bars:
    width = bar.get_width()
    label_x_pos = width - 5 if width > 10 else width + 5
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'${width}B', ha='center', va='center', fontsize=12, color='black' if width > 10 else 'white', fontweight='bold')

# Set the title and labels
ax.set_title("Global Renewable Energy Investment\nDistribution in 2023", fontsize=18, fontweight='bold', pad=15)
ax.set_xlabel("Investment Amount (Billion USD)", fontsize=14)
ax.set_xlim(0, 130)

# Invert y-axis to have the largest investment on top
ax.invert_yaxis()

# Add gridlines for horizontal reference
ax.xaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax.yaxis.grid(False)

# Ensure the layout is tight to avoid overlaps and optimize spacing
plt.tight_layout()

# Show the plot
plt.show()