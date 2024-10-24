import matplotlib.pyplot as plt
import numpy as np

# Define guilds and their revenue data (in golden crowns)
guilds = ['Blacksmith Guild', 'Weaver Guild', 'Alchemist Guild', 'Mason Guild']

# Manually crafted revenue data
blacksmith_revenue = [250, 270, 260, 280, 300, 310, 305, 290, 275, 285, 295, 305]
weaver_revenue = [200, 210, 205, 215, 220, 230, 225, 215, 210, 215, 220, 230]
alchemist_revenue = [180, 190, 200, 195, 185, 205, 200, 190, 180, 195, 210, 215]
mason_revenue = [300, 320, 310, 305, 315, 325, 310, 300, 295, 315, 320, 330]

# Organize data in a list for the box plot
guild_revenues = [blacksmith_revenue, weaver_revenue, alchemist_revenue, mason_revenue]

# Create a vertical box plot
plt.figure(figsize=(10, 7))
box = plt.boxplot(guild_revenues, vert=True, patch_artist=True, labels=guilds, notch=True, showfliers=True, whis=1.5)

# Customize colors for each box
colors = ['#DAA520', '#FFD700', '#C0C0C0', '#B8860B']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set whisker and cap colors
for whisker in box['whiskers']:
    whisker.set(color='#8b4513', linewidth=1.5)
for cap in box['caps']:
    cap.set(color='#8b4513', linewidth=1.5)
for median in box['medians']:
    median.set(color='#FF6347', linewidth=2)

# Adding title and axis labels
plt.title('Medieval Kingdom Economy:\nAnnual Revenues of Guilds in Galendra (1423)', fontsize=14, fontweight='bold')
plt.ylabel('Revenue (Golden Crowns)', fontsize=12)
plt.xlabel('Guilds', fontsize=12)

# Add grid for visual aid
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()