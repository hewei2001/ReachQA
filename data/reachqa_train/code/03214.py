import matplotlib.pyplot as plt

# Define the years and number of voyages
years = [1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900]
voyages = [5, 15, 50, 100, 150, 200, 250, 300, 400, 450, 500]

# New data: Number of new territories discovered in corresponding years
discoveries = [1, 3, 10, 20, 30, 35, 40, 45, 50, 55, 60]

# Notable exploration points (years and voyages)
milestones = {
    "1492: Columbus' Voyage": (1492, 30),
    "1521: Magellan's Circumnavigation": (1521, 60),
    "1770: Cook in Australia": (1770, 290),
    "1804: Lewis & Clark": (1804, 410)
}

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the voyages data
ax1.plot(years, voyages, marker='o', linestyle='-', color='b', linewidth=2, markersize=6, label="Voyages")

# Annotate notable exploration points
for note, (year, voyage) in milestones.items():
    ax1.annotate(note, xy=(year, voyage), xytext=(year - 30, voyage + 40),
                 arrowprops=dict(facecolor='gray', arrowstyle='->', lw=1),
                 fontsize=9, ha='center', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow'))

# Add a secondary y-axis for discoveries
ax2 = ax1.twinx()
ax2.bar(years, discoveries, width=20, color='orange', alpha=0.6, label="Discoveries")

# Title and labels
plt.title("A Voyage Through Time\nKey Exploration Milestones and Discoveries", fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Number of Exploration Voyages", fontsize=12)
ax2.set_ylabel("Number of Discoveries", fontsize=12, color='orange')

# Customize the legend and grid
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.5)

# Adjust the ticks
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Improve layout
plt.tight_layout()

# Show the plot
plt.show()