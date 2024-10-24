import matplotlib.pyplot as plt
import numpy as np

# Define yield data in kilograms for different vegetables across urban garden plots
# Adjusted data to show variability and patterns
tomatoes_yield = [45, 50, 55, 47, 52, 60, 58, 54, 49, 53]
lettuce_yield = [30, 28, 32, 25, 31, 29, 27, 30, 28, 35]
carrots_yield = [40, 42, 45, 38, 47, 44, 39, 41, 43, 40]
cucumbers_yield = [20, 22, 19, 23, 21, 18, 24, 22, 20, 25]

# Combine data into a list for plotting
data = [tomatoes_yield, lettuce_yield, carrots_yield, cucumbers_yield]

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create a horizontal box plot
box = ax.boxplot(data, vert=False, patch_artist=True, 
                 labels=["Tomatoes", "Lettuce", "Carrots", "Cucumbers"],
                 flierprops=dict(marker='o', color='red', alpha=0.5),
                 boxprops=dict(color='darkblue', linewidth=1.5),
                 whiskerprops=dict(color='blue', linestyle='--'),
                 capprops=dict(color='blue'),
                 medianprops=dict(color='orange', linewidth=2),
                 notch=True)

# Set colors for each box
colors = ['skyblue', 'lightgreen', 'orange', 'lightcoral']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add grid for better readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Add titles and axis labels
ax.set_title("Urban Agriculture Initiative:\nYield Distribution Across Urban Gardens", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Yield (kg)", fontsize=14)
ax.set_ylabel("Vegetable Type", fontsize=14)

# Annotate the key area of highest variability
ax.annotate('Highest Variability\nin Yield', xy=(55, 1), xytext=(60, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()