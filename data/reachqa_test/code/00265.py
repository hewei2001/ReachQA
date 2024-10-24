import matplotlib.pyplot as plt
import numpy as np

# Decades representing time intervals
decades = np.array(['1990s', '2000s', '2010s', '2020s'])

# Renewable energy storage capacity (in GWh) for each decade
storage_capacity = np.array([5, 50, 200, 800])

# Hypothetical investment in renewable energy storage (in billion USD) for each decade
investment = np.array([0.5, 2, 5, 15])

# Significant breakthroughs in renewable energy storage
breakthroughs = [
    "Introduction of\nLithium-Ion Batteries",
    "Rise of Grid-Scale\nBattery Projects",
    "Advancements in\nFlywheel Technology",
    "Commercialization of\nThermal Storage"
]

# Creating the plot
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plotting storage capacity over the decades
ax1.plot(decades, storage_capacity, marker='o', linestyle='-', color='green', linewidth=2, markersize=8, label='Storage Capacity (GWh)')

# Annotate key breakthroughs
for (x, y, label) in zip(decades, storage_capacity, breakthroughs):
    ax1.annotate(label, (x, y), textcoords="offset points", xytext=(-50, 15 if y != 800 else -30), ha='center', fontsize=9,
                 arrowprops=dict(arrowstyle='->', color='gray', lw=1.5), bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='white', alpha=0.8))

# Adding a secondary y-axis for investment plot
ax2 = ax1.twinx()
ax2.bar(decades, investment, color='orange', alpha=0.6, width=0.4, align='center', label='Investment (Billion USD)')

# Titles and labels
ax1.set_title("Evolution of Renewable Energy Storage\nCapacity and Investment (1990s-2020s)", fontsize=14, fontweight='bold')
ax1.set_xlabel("Decade", fontsize=12)
ax1.set_ylabel("Storage Capacity (GWh)", fontsize=12, color='green')
ax2.set_ylabel("Investment (Billion USD)", fontsize=12, color='orange')

# Setting ticks and grid
ax1.set_xticks(decades)
ax1.set_yticks(np.arange(0, 901, 100))
ax2.set_yticks(np.arange(0, 16, 2))

ax1.grid(True, linestyle='--', alpha=0.5)

# Legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left')

# Adjust layout automatically
fig.tight_layout()

# Display the plot
plt.show()