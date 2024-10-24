import matplotlib.pyplot as plt
import numpy as np

# Data setup: Ambient sound intensities in mythical forests
forests = ['Emerald Woods', 'Silver Glade', 'Whispering Pines', 'Twilight Grove']
sounds = ['Rustling Leaves', 'Flowing Streams', 'Chirping Birds', 'Howling Winds']

# Intensity matrix (rows: forests, columns: sound types)
intensity_matrix = np.array([
    [8, 6, 9, 4],  # Emerald Woods
    [5, 9, 4, 7],  # Silver Glade
    [9, 5, 7, 6],  # Whispering Pines
    [4, 7, 6, 8],  # Twilight Grove
])

# Plotting the heatmap
plt.figure(figsize=(10, 6))
heatmap = plt.imshow(intensity_matrix, cmap='YlGnBu', aspect='auto', interpolation='nearest')

# Adding titles and labels
plt.title('Ambient Sound Distribution\nin Mythical Forests', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Sound Types', fontsize=12)
plt.ylabel('Forests', fontsize=12)
plt.xticks(ticks=np.arange(len(sounds)), labels=sounds, fontsize=10, rotation=45, ha='right')
plt.yticks(ticks=np.arange(len(forests)), labels=forests, fontsize=10)

# Adding a color bar to indicate intensity levels
cbar = plt.colorbar(heatmap)
cbar.set_label('Intensity Level (0-10)', fontsize=12)

# Adding annotations for each cell
for i in range(len(forests)):
    for j in range(len(sounds)):
        plt.text(j, i, f'{intensity_matrix[i, j]}', ha='center', va='center', color='black', fontweight='bold')

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the heatmap
plt.show()