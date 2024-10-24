import matplotlib.pyplot as plt

# Data representing the "sparkle rating" of outfits from various interstellar fashion capitals
glitzon = [90, 85, 88, 92, 91, 87, 95, 93, 89, 85]
twinklea = [70, 68, 72, 69, 74, 73, 71, 66, 75, 77]
radiara = [50, 55, 52, 58, 54, 53, 56, 51, 57, 59]
lumino = [40, 42, 38, 45, 43, 47, 41, 39, 44, 46]
dazzlon = [30, 28, 35, 33, 29, 31, 32, 36, 34, 37]

# Combine data into a list for the box plot
data = [glitzon, twinklea, radiara, lumino, dazzlon]
labels = ['Glitzon', 'Twinklea', 'Radiara', 'Lumino', 'Dazzlon']

# Create the box plot
fig, ax = plt.subplots(figsize=(12, 8))
box = ax.boxplot(data, patch_artist=True, labels=labels, notch=True)

# Customize box plot colors
colors = ['#FFD700', '#DAA520', '#B8860B', '#8B4513', '#CD853F']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.5)

# Highlight the median values with a unique style
for median in box['medians']:
    median.set(color='red', linewidth=2)

# Adding a title and labels
ax.set_title('Secrets of Starry Couture:\nGalactic Fashion Trends', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Sparkle Rating (0 to 100)', fontsize=12)
ax.set_xlabel('Interstellar Fashion Capitals', fontsize=12)

# Add grid for better readability
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add legend
ax.legend([box["boxes"][0]], ['Sparkle Rating'], loc='upper right', fontsize=10, frameon=False)

# Tight layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()