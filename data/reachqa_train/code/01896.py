import matplotlib.pyplot as plt
import squarify

# Data for the tree map
regions = ["North America", "Europe", "Asia", "Africa"]
sources = ["Solar", "Wind", "Hydro", "Geothermal", "Biomass"]

# Fictional data in GW, representing the installed capacity for each energy source by region
north_america = [60, 80, 120, 10, 30]
europe = [70, 100, 140, 20, 40]
asia = [100, 200, 300, 40, 60]
africa = [20, 30, 50, 5, 10]

# Combine the data into a single list for squarify
sizes = north_america + europe + asia + africa

# Creating labels with source and capacity for each region
labels = []
for r, values in zip(regions, [north_america, europe, asia, africa]):
    for s, c in zip(sources, values):
        labels.append(f"{r}\n{s}\n({c} GW)")

# Colors for each energy source, repeated for each region
colors = ["#FF9999", "#66B3FF", "#99FF99", "#FFCC99", "#FFD700"] * len(regions)

# Plotting the tree map
plt.figure(figsize=(14, 10))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.7, edgecolor="white", linewidth=2)

# Adding a title and making aesthetic adjustments
plt.title("Global Renewable Energy Usage by Source\n(A Snapshot of Installed Capacity Across Regions)", fontsize=18, fontweight="bold")
plt.axis('off')  # Turn off the axes

# Automatically adjust layout to fit everything neatly
plt.tight_layout()

# Display the tree map
plt.show()