import matplotlib.pyplot as plt
import numpy as np

# Data for energy consumption by appliance type (in kWh)
appliance_types = ["Kitchen\nAppliances", "Heating &\nCooling", "Lighting", "Laundry\nMachines", "Electronics", "Other"]
energy_consumption = [250, 400, 150, 100, 200, 50]

# Colors for the bars
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Creating the bar chart
fig, ax = plt.subplots(figsize=(12, 7))
bar_positions = np.arange(len(appliance_types))
bars = ax.bar(bar_positions, energy_consumption, color=colors, width=0.6)

# Adding data labels above each bar
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 10, f'{yval} kWh', ha='center', va='bottom', fontsize=11)

# Customizing the chart
ax.set_title("Energy Consumption by Appliance Type\nin an Average Home", fontsize=18, color='darkblue')
ax.set_xlabel("Appliance Type", fontsize=14)
ax.set_ylabel("Monthly Energy Consumption (kWh)", fontsize=14)
ax.set_xticks(bar_positions)
ax.set_xticklabels(appliance_types, fontsize=12, rotation=45, ha='right')
ax.set_ylim(0, 450)

# Adding a grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()