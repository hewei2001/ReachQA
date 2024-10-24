import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Art forms and months
art_forms = ['Sculpture', 'Fresco Painting', 'Wood Carving', 'Mosaic', 'Tapestry', 'Illuminated Manuscripts']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Workshop frequency data
workshop_frequencies = np.array([
    [10, 8, 15, 7, 10, 5, 12, 9, 13, 16, 11, 14],  # Sculpture
    [14, 16, 12, 18, 20, 14, 13, 19, 15, 17, 16, 18],  # Fresco Painting
    [8, 10, 9, 12, 7, 10, 8, 11, 9, 6, 7, 8],  # Wood Carving
    [5, 4, 6, 5, 7, 8, 5, 6, 9, 7, 8, 5],  # Mosaic
    [6, 5, 7, 8, 9, 6, 5, 4, 7, 6, 8, 7],  # Tapestry
    [4, 6, 5, 3, 4, 5, 3, 4, 5, 6, 7, 4]   # Illuminated Manuscripts
])

# Initialize the figure
plt.figure(figsize=(16, 9))

# Plot the heatmap
im = plt.imshow(workshop_frequencies, aspect='auto', cmap='coolwarm', interpolation='nearest')

# Add titles and labels
plt.title('Renaissance Art Workshop Frequencies\nFlorence, 16th Century', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Months', fontsize=12)
plt.ylabel('Art Forms', fontsize=12)

# Set ticks
plt.xticks(ticks=np.arange(len(months)), labels=months, rotation=45, ha='right')
plt.yticks(ticks=np.arange(len(art_forms)), labels=art_forms)

# Add annotations for each cell
for i in range(len(art_forms)):
    for j in range(len(months)):
        text = plt.text(j, i, f'{workshop_frequencies[i, j]}', ha='center', va='center', color='black', fontsize=10)

# Add a color bar with more detailed labeling
cbar = plt.colorbar(im, orientation='vertical')
cbar.set_label('Number of Workshops', fontsize=12)

# Highlight cells with max and min frequencies
max_value = np.max(workshop_frequencies)
min_value = np.min(workshop_frequencies)
for i in range(len(art_forms)):
    for j in range(len(months)):
        if workshop_frequencies[i, j] == max_value:
            plt.gca().add_patch(patches.Rectangle((j-0.5, i-0.5), 1, 1, fill=False, edgecolor='red', linewidth=2))
        elif workshop_frequencies[i, j] == min_value:
            plt.gca().add_patch(patches.Rectangle((j-0.5, i-0.5), 1, 1, fill=False, edgecolor='blue', linewidth=2))

# Ensure layout is optimal
plt.tight_layout()

# Show the heat map
plt.show()