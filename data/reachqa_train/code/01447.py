import matplotlib.pyplot as plt
import squarify

# Define data
cities = ["EcoVille", "Greenburgh", "Renewapolis", "Sustainable City", "Future Bay", "Harmony Town"]
energy_types = ["Solar", "Wind", "Hydroelectric", "Geothermal", "Biomass"]
investments = [
    [120, 80, 60, 40, 20],   # EcoVille
    [150, 90, 50, 60, 30],   # Greenburgh
    [180, 70, 40, 70, 40],   # Renewapolis
    [130, 110, 70, 50, 60],  # Sustainable City
    [140, 95, 65, 45, 35],   # Future Bay
    [110, 85, 55, 35, 45]    # Harmony Town
]

# Flatten investment data and prepare labels for the tree map
flat_investments = [value for sublist in investments for value in sublist]
labels = [f"{city}\n{etype}\n${amount}M" for city, sublist in zip(cities, investments) for etype, amount in zip(energy_types, sublist)]

# Define a color palette for distinct city visualization
colors = plt.cm.viridis([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])

# Plotting
plt.figure(figsize=(14, 10))
squarify.plot(sizes=flat_investments, label=labels, color=colors, alpha=0.8, edgecolor="white", linewidth=2)

# Customize the plot
plt.title("Investment in Renewable Energy\nAcross Future Cities", fontsize=18, fontweight='bold', pad=15)
plt.axis('off')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()