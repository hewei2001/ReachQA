import matplotlib.pyplot as plt
import numpy as np

# Define the fashion trends and continents
trends = ['Vintage', 'Minimalist', 'Athleisure', 'Bohemian', 'Sustainable', 'Futuristic', 'Streetwear']
continents = ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Oceania']

# Manually crafted popularity index for each trend on each continent
popularity_index = np.array([
    [80, 65, 70, 75, 60, 85],  # Vintage
    [70, 50, 85, 55, 45, 60],  # Minimalist
    [75, 60, 65, 80, 55, 70],  # Athleisure
    [65, 75, 60, 70, 80, 65],  # Bohemian
    [90, 80, 95, 85, 75, 80],  # Sustainable
    [55, 45, 50, 60, 50, 65],  # Futuristic
    [85, 70, 75, 90, 65, 80]   # Streetwear
])

# Create the heat map
plt.figure(figsize=(12, 8))
plt.imshow(popularity_index, cmap='coolwarm', aspect='auto', interpolation='nearest')

# Title and labels
plt.title('Global Popularity of Fashion Trends Across Continents', fontsize=16, fontweight='bold', pad=20)
plt.xticks(ticks=np.arange(len(continents)), labels=continents, rotation=45, ha='right', fontsize=12)
plt.yticks(ticks=np.arange(len(trends)), labels=trends, fontsize=12)

# Color bar for reference
cbar = plt.colorbar()
cbar.set_label('Popularity Index (0 to 100)', fontsize=12)

# Annotate each cell with the corresponding index
for i in range(len(trends)):
    for j in range(len(continents)):
        plt.text(j, i, popularity_index[i, j], ha='center', va='center', color='white' if popularity_index[i, j] < 70 else 'black', fontsize=10)

# Layout adjustment
plt.tight_layout()

# Show the plot
plt.show()