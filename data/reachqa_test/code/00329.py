import matplotlib.pyplot as plt
import numpy as np

# Expanded centuries and regions
centuries = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100]
regions = ['East Africa', 'West Africa', 'South Asia', 'East Asia', 'Western Europe',
           'Eastern Europe', 'North America', 'Central America', 'South America', 'Oceania']

# Expanded and more detailed language diversity index data
diversity_data = np.array([
    [0.85, 0.82, 0.7, 0.65, 0.6, 0.58, 0.3, 0.2, 0.5, 0.72],  # 1000 AD
    [0.87, 0.83, 0.72, 0.67, 0.61, 0.59, 0.32, 0.22, 0.53, 0.74],  # 1100 AD
    [0.8, 0.78, 0.68, 0.63, 0.6, 0.58, 0.35, 0.25, 0.55, 0.73],   # 1200 AD
    [0.82, 0.77, 0.7, 0.65, 0.62, 0.6, 0.4, 0.28, 0.58, 0.75],    # 1300 AD
    [0.85, 0.8, 0.72, 0.68, 0.65, 0.63, 0.45, 0.3, 0.6, 0.78],   # 1400 AD
    [0.87, 0.82, 0.75, 0.7, 0.68, 0.67, 0.5, 0.35, 0.62, 0.79],   # 1500 AD
    [0.9, 0.84, 0.78, 0.73, 0.7, 0.69, 0.55, 0.4, 0.65, 0.82],   # 1600 AD
    [0.88, 0.85, 0.8, 0.75, 0.72, 0.71, 0.6, 0.45, 0.68, 0.85],   # 1700 AD
    [0.86, 0.88, 0.82, 0.78, 0.75, 0.73, 0.65, 0.5, 0.7, 0.87],   # 1800 AD
    [0.83, 0.9, 0.85, 0.82, 0.78, 0.76, 0.7, 0.55, 0.72, 0.88],   # 1900 AD
    [0.81, 0.92, 0.88, 0.85, 0.8, 0.78, 0.75, 0.6, 0.74, 0.9],    # 2000 AD
    [0.78, 0.93, 0.9, 0.88, 0.82, 0.8, 0.78, 0.65, 0.76, 0.92],   # 2100 AD
])

# Create the figure with subplots
fig, ax = plt.subplots(figsize=(12, 8))
cax = ax.imshow(diversity_data, cmap='coolwarm', aspect='auto', interpolation='nearest')

# Add color bar with label
cbar = fig.colorbar(cax, ax=ax)
cbar.set_label('Language Diversity Index', rotation=270, labelpad=20)

# Set axis labels and ticks
ax.set_xticks(range(len(regions)))
ax.set_xticklabels(regions, fontsize=10, rotation=45, ha='right')
ax.set_yticks(range(len(centuries)))
ax.set_yticklabels(centuries, fontsize=10)
ax.set_xlabel('Region', fontsize=12)
ax.set_ylabel('Century (AD)', fontsize=12)

# Title split into two lines for clarity
ax.set_title('Comprehensive Evolution of Language Diversity Index\nAcross Global Regions (1000 AD - 2100 AD)', 
             fontsize=14, fontweight='bold', pad=20)

# Add grid lines for better readability and distinction
ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.2)
ax.grid(which='major', color='gray', linestyle='-', linewidth=0.5)

# Automatically adjust the layout for better fitting elements
plt.tight_layout()

# Display the plot
plt.show()