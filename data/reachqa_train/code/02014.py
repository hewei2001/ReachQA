import matplotlib.pyplot as plt
import numpy as np

# Data for household energy consumption in kWh per month
data = [
    [250, 270, 290, 310, 320, 330, 350, 360, 370, 380],  # Urban Apartments
    [500, 520, 540, 580, 600, 620, 640, 660, 700, 720],  # Rural Single-Family Homes
    [400, 420, 440, 460, 480, 500, 520, 540, 560, 580],  # Urban Single-Family Homes
    [300, 320, 340, 350, 370, 390, 410, 430, 450, 470],  # Rural Apartments
    [150, 160, 170, 180, 190, 200, 210, 220, 230, 240],  # Eco-Friendly Homes
]

# Labels for the horizontal box plot
labels = [
    'Urban Apartments', 
    'Rural Single-Family Homes', 
    'Urban Single-Family Homes', 
    'Rural Apartments', 
    'Eco-Friendly Homes'
]

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(10, 6))
box = ax.boxplot(data, patch_artist=True, vert=False, notch=True, 
                 boxprops=dict(facecolor='#b3cde3', color='#005b96'),
                 whiskerprops=dict(color='#005b96'),
                 capprops=dict(color='#005b96'),
                 medianprops=dict(color='#d73027'))

# Customize colors for each box
colors = ['#b3cde3', '#6497b1', '#005b96', '#03396c', '#011f4b']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add customizations
ax.set_title('Diverse Energy Consumption Patterns:\nA Study of Household Energy Usage', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Energy Consumption (kWh per month)', fontsize=12)
ax.set_ylabel('Household Type', fontsize=12)
ax.set_yticklabels(labels, fontsize=10)
ax.grid(True, linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()