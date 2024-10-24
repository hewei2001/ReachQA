import matplotlib.pyplot as plt

# Data representing the number of different communication methods observed in each region
# This data is hypothetical and represents a variety of communication forms used by species
earth_proximity = [5, 7, 9, 6, 8, 7, 10, 6, 7, 8]
outer_planets = [10, 12, 11, 15, 14, 13, 10, 11, 13, 12]
andromeda_sector = [17, 20, 19, 18, 22, 24, 23, 21, 19, 20]
zeta_quadrant = [8, 9, 10, 9, 12, 11, 13, 11, 10, 11]
galactic_core = [22, 25, 23, 26, 27, 28, 26, 24, 25, 27]

# Combine data into a list for plotting
data = [earth_proximity, outer_planets, andromeda_sector, zeta_quadrant, galactic_core]

# Create the vertical box plot
plt.figure(figsize=(10, 6))
bp = plt.boxplot(data, vert=True, patch_artist=True, notch=True,
                 boxprops=dict(facecolor='#ccebc5', color='black'),
                 medianprops=dict(color='red', linewidth=2),
                 whiskerprops=dict(color='blue', linewidth=1.5),
                 capprops=dict(color='blue', linewidth=1.5),
                 flierprops=dict(marker='o', color='orange', markersize=8, linestyle='none', markeredgecolor='orange'))

# Set title and labels
plt.title('Interstellar Language Studies:\nDiversity of Communication Methods Across Galactic Regions', fontsize=14, fontweight='bold')
plt.xlabel('Galactic Regions', fontsize=12)
plt.ylabel('Number of Communication Methods', fontsize=12)

# Set x-tick labels
plt.xticks([1, 2, 3, 4, 5], ['Earth\'s Proximity', 'Outer Planets', 'Andromeda Sector', 'Zeta Quadrant', 'Galactic Core'], rotation=15)

# Add gridlines for readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate notable features
plt.annotate('High Diversity in Galactic Core', 
             xy=(5, 27), 
             xytext=(3.5, 30), 
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), 
             fontsize=10, color='black')

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()