import matplotlib.pyplot as plt
import numpy as np

# Define yield data in kilograms for different vegetables across urban garden plots
tomatoes_yield = [45, 50, 55, 47, 52, 60, 58, 54, 49, 53]
lettuce_yield = [30, 28, 32, 25, 31, 29, 27, 30, 28, 35]
carrots_yield = [40, 42, 45, 38, 47, 44, 39, 41, 43, 40]
cucumbers_yield = [20, 22, 19, 23, 21, 18, 24, 22, 20, 25]

data = [tomatoes_yield, lettuce_yield, carrots_yield, cucumbers_yield]
vegetable_types = ["Tomatoes", "Lettuce", "Carrots", "Cucumbers"]

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(14, 10))

# Create a horizontal box plot
box = ax.boxplot(data, vert=False, patch_artist=True, 
                 labels=vegetable_types,
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

# Overlay a violin plot to show data distribution
violin = ax.violinplot(data, vert=False, showmeans=False, showmedians=False, widths=0.7)
for pc, color in zip(violin['bodies'], colors):
    pc.set_facecolor(color)
    pc.set_edgecolor('black')
    pc.set_alpha(0.3)

# Annotate the highest variability
ax.annotate('Highest Variability\nin Yield', xy=(55, 1), xytext=(65, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, backgroundcolor='white')

# Add grid for better readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Titles and labels
ax.set_title("Urban Agriculture Initiative:\nYield Distribution Across Urban Gardens", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Yield (kg)", fontsize=14)
ax.set_ylabel("Vegetable Type", fontsize=14)

# Histogram subplot to show yield distribution
ax_hist = ax.twiny()
ax_hist.set_xticks([])
for i, data_series in enumerate(data):
    hist_data = np.histogram(data_series, bins=np.arange(min(data_series), max(data_series)+1, 1))
    ax_hist.barh([i+1]*len(hist_data[0]), hist_data[0], left=hist_data[1][:-1], color=colors[i], alpha=0.2, height=0.3)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()