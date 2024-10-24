import numpy as np
import matplotlib.pyplot as plt

# Art styles and corresponding fictitious data representing artworks exhibited
art_styles = [
    "Abstract", "Modern", "Impressionism", "Surrealism", 
    "Minimalism", "Cubism", "Pop Art", "Street Art", "Realism"
]

# Data: Number of artworks in each category (artificially crafted)
artworks_count = np.array([
    75, 120, 50, 60, 30, 
    55, 80, 45, 90
])

# Define bin edges for histogram
bins = np.arange(len(art_styles) + 1)

# Plotting the histogram
plt.figure(figsize=(12, 8))
plt.hist(np.repeat(range(len(art_styles)), artworks_count), bins=bins, color='skyblue', edgecolor='black', alpha=0.7)

# Customizing the plot
plt.title("The Artistic Palette of the 21st Century:\nA Journey Through Popular Art Styles", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Art Styles", fontsize=14)
plt.ylabel("Number of Artworks Exhibited", fontsize=14)

# Setting x-tick labels
plt.xticks(ticks=np.arange(len(art_styles)) + 0.5, labels=art_styles, rotation=45, ha='right', fontsize=12)

# Adding grid lines for clarity
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Annotations for additional context
max_style = art_styles[np.argmax(artworks_count)]
plt.annotate(f'Highest: {max_style}', xy=(np.argmax(artworks_count) + 0.5, np.max(artworks_count)),
             xytext=(np.argmax(artworks_count) + 1.5, np.max(artworks_count) + 10),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=12, color='black')

# Ensure layout doesn't overlap
plt.tight_layout()

# Display the plot
plt.show()