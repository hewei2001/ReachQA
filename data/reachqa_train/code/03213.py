import matplotlib.pyplot as plt

# Define the years and number of voyages
years = [1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900]
voyages = [5, 15, 50, 100, 150, 200, 250, 300, 400, 450, 500]

# Notable exploration points (years and voyages)
milestones = {
    "1492: Columbus' Voyage": (1492, 30),
    "1521: Magellan's Circumnavigation": (1521, 60),
    "1770: Cook in Australia": (1770, 290),
    "1804: Lewis & Clark": (1804, 410)
}

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the data
ax.plot(years, voyages, marker='o', linestyle='-', color='b', linewidth=2, markersize=6)

# Annotate notable exploration points
for note, (year, voyage) in milestones.items():
    ax.annotate(note, xy=(year, voyage), xytext=(year - 10, voyage + 40),
                arrowprops=dict(facecolor='gray', arrowstyle='->', lw=1),
                fontsize=9, ha='center', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow'))

# Add title and labels
plt.title("A Voyage Through Time: Key Exploration Milestones\nFrom the Age of Discovery to the Modern Era", fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Number of Exploration Voyages", fontsize=12)

# Customize the legend and grid
plt.legend(["Voyages"], loc='upper left', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.5)

# Adjust the ticks
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Improve layout
plt.tight_layout()

# Show the plot
plt.show()