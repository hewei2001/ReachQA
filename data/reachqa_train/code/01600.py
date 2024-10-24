import matplotlib.pyplot as plt
import numpy as np

# Define the decades and fashion styles
decades = ["1960s", "1970s", "1980s", "1990s", "2000s", "2010s", "2020s"]
styles = ["Vintage", "Modern", "Bohemian", "Avant-garde", "Casual"]

# Data representing the popularity of each style by decade (in percentages)
vintage_popularity = [30, 25, 20, 15, 10, 5, 3]
modern_popularity = [20, 25, 30, 35, 40, 45, 50]
bohemian_popularity = [10, 15, 20, 15, 10, 12, 10]
avantgarde_popularity = [5, 10, 15, 20, 25, 20, 15]
casual_popularity = [35, 25, 15, 15, 15, 18, 22]

# Stack the popularity data
popularity_data = np.array([vintage_popularity, modern_popularity, bohemian_popularity, avantgarde_popularity, casual_popularity])

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(decades, popularity_data, labels=styles, colors=['#b5651d', '#4b8b3b', '#c697ce', '#6a0dad', '#d3d3d3'], alpha=0.85)

# Title and labels
ax.set_title('Evolution of Fashion Styles\nThrough the Decades', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('Popularity (%)', fontsize=12)

# Customize x-ticks to avoid overlap
plt.xticks(rotation=45, ha='right')

# Adding grid for better readability
ax.yaxis.grid(True, linestyle='--', which='major', color='gray', alpha=0.7)

# Adding a legend
ax.legend(loc='upper left', fontsize=10, title='Fashion Styles', title_fontsize='12', bbox_to_anchor=(1, 1))

# Automatic layout adjustment to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()