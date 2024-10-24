import numpy as np
import matplotlib.pyplot as plt

# Extended art styles
art_styles = [
    "Abstract", "Modern", "Impressionism", "Surrealism",
    "Minimalism", "Cubism", "Pop Art", "Street Art", "Realism",
    "Baroque", "Renaissance", "Neoclassicism", "Futurism",
    "Expressionism", "Art Nouveau", "Folk Art", "Dada"
]

# Updated data: Number of artworks in each category
artworks_count = np.array([
    75, 120, 50, 60, 30, 55, 80, 45, 90, 
    65, 100, 70, 35, 85, 40, 95, 55
])

# Define bins for histogram
bins = np.arange(len(art_styles) + 1)

# Create a figure with subplots
fig, ax = plt.subplots(2, 1, figsize=(14, 12), sharex=True)

# Main Histogram for total artworks
ax[0].hist(np.repeat(range(len(art_styles)), artworks_count), bins=bins, color='skyblue', edgecolor='black', alpha=0.7)
ax[0].set_title("Artistic Diversity Across Styles:\nExploration of Exhibition Counts", fontsize=16, fontweight='bold', pad=20)
ax[0].set_ylabel("Total Artworks", fontsize=14)
ax[0].grid(axis='y', linestyle='--', alpha=0.7)

# Cumulative distribution plot
cumulative_counts = np.cumsum(artworks_count)
ax[1].step(range(len(art_styles)), cumulative_counts, where='mid', color='orange', linewidth=2, label='Cumulative Count')
ax[1].set_title("Cumulative Trend of Artworks", fontsize=16, fontweight='bold', pad=10)
ax[1].set_xlabel("Art Styles", fontsize=14)
ax[1].set_ylabel("Cumulative Artworks", fontsize=14)
ax[1].legend()
ax[1].grid(axis='y', linestyle='--', alpha=0.7)

# Setting x-tick labels
plt.xticks(ticks=np.arange(len(art_styles)), labels=art_styles, rotation=45, ha='right', fontsize=12)

# Add annotations
for style_index, count in enumerate(artworks_count):
    ax[0].annotate(f'{count}', xy=(style_index, count), 
                   xytext=(style_index, count + 5), 
                   ha='center', fontsize=10, color='black')

# Highest artwork count annotation
max_style_index = np.argmax(artworks_count)
ax[0].annotate(f'Highest: {art_styles[max_style_index]}', xy=(max_style_index, np.max(artworks_count)), 
               xytext=(max_style_index + 1, np.max(artworks_count) + 10),
               arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
               fontsize=12, color='black')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()