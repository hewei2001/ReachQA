import matplotlib.pyplot as plt
import numpy as np

# Define categories and energy changes
categories = ['Base Demand', 'Solar', 'Wind', 'Hydro', 'Geothermal', 'Residential', 'Commercial', 'Industrial', 'Transport']
energy_changes = [1000, 150, 120, 180, 100, -80, -100, -150, -90]

# Calculate cumulative energy levels
energy_levels = np.cumsum(energy_changes)
starts = np.concatenate(([0], energy_levels[:-1]))

# Define colors with a more varied color palette
colors = ['#6a51a3' if x == 1000 else '#4daf4a' if x > 0 else '#d73027' for x in energy_changes]

# Create a waterfall chart with enhanced features
fig, ax = plt.subplots(figsize=(14, 8))
bars = plt.bar(categories, energy_changes, bottom=starts, color=colors, edgecolor='black', linewidth=1.5, width=0.6)

# Add annotations and lines
for i, (bar, change) in enumerate(zip(bars, energy_changes)):
    y_position = bar.get_height() + bar.get_y()
    # Annotate each bar with the energy change and cumulative energy level
    plt.text(bar.get_x() + bar.get_width() / 2, y_position + (20 if change > 0 else -40), 
             f'{change:+}\n({int(y_position)})', ha='center', va='bottom', fontsize=9, color='black')
    if i < len(categories) - 1:
        plt.plot([i, i + 1], [energy_levels[i], energy_levels[i]], 'k-', lw=0.8)

# Titles and labels
plt.title("Energy Savings from Renewable Sources in Solaria\nYearly Overview of Contributions and Sectoral Savings", fontsize=14, fontweight='bold')
plt.xlabel("Energy Sources and Savings Categories", fontsize=11)
plt.ylabel("Energy Units (in hundreds)", fontsize=11)

# Add grid lines and improve x-tick presentation
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=30, ha='right')

# Subplot for additional data: Visualize percentage contribution
percentage_contribution = [(change / sum(energy_changes)) * 100 for change in energy_changes]
ax2 = ax.twinx()
ax2.plot(categories, percentage_contribution, 'o-', color='blue', markerfacecolor='orange', markersize=5, label='Percentage Contribution')
ax2.set_ylabel("Percentage Contribution (%)", fontsize=11)
ax2.legend(loc='upper right')

# Tighten layout for clearer presentation
plt.tight_layout()

# Show plot
plt.show()