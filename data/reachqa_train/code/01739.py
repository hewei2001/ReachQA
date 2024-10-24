import matplotlib.pyplot as plt
import numpy as np

# Define renewable energy types and their corresponding investment amounts in billion USD
energy_types = ['Solar', 'Wind', 'Hydropower', 'Biomass', 'Geothermal']
investment_amounts = [120, 95, 70, 45, 20]  # Hypothetical values for 2023

# Colors for the charts
colors = ['#f9a825', '#29b6f6', '#66bb6a', '#8d6e63', '#ff7043']

# Calculate the percentage of total investment for each energy type
total_investment = sum(investment_amounts)
percentages = [(amount / total_investment) * 100 for amount in investment_amounts]

# Create a figure with two subplots: one for the bar chart and one for the pie chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Bar Chart: Investment amounts
bars = ax1.barh(energy_types, investment_amounts, color=colors, edgecolor='black')
for bar in bars:
    width = bar.get_width()
    label_x_pos = width - 5 if width > 10 else width + 5
    ax1.text(label_x_pos, bar.get_y() + bar.get_height()/2,
             f'${width}B', ha='center', va='center', fontsize=12,
             color='black' if width > 10 else 'white', fontweight='bold')

ax1.set_title("Global Renewable Energy Investment\nDistribution in 2023", fontsize=16, fontweight='bold')
ax1.set_xlabel("Investment Amount (Billion USD)", fontsize=12)
ax1.set_xlim(0, 130)
ax1.invert_yaxis()
ax1.xaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Pie Chart: Market share as percentages
ax2.pie(percentages, labels=[f'{et} ({p:.1f}%)' for et, p in zip(energy_types, percentages)],
        autopct='%1.1f%%', startangle=140, colors=colors, explode=[0.1 if et == 'Solar' else 0 for et in energy_types],
        wedgeprops=dict(edgecolor='black', linewidth=1.5))

ax2.set_title("Market Share of Renewable Energy\nInvestment in 2023", fontsize=16, fontweight='bold')

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the combined plot
plt.show()