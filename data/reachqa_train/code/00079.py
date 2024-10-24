import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.array([2019, 2020, 2021, 2022, 2023])

# Production data for each region and fruit type
northland_apples = np.array([500, 520, 540, 560, 580])
northland_bananas = np.array([200, 210, 220, 230, 240])
northland_cherries = np.array([100, 105, 110, 115, 120])

midlands_apples = np.array([450, 460, 470, 480, 490])
midlands_bananas = np.array([250, 260, 270, 280, 290])
midlands_cherries = np.array([150, 155, 160, 165, 170])

southshore_apples = np.array([550, 570, 590, 610, 630])
southshore_bananas = np.array([300, 320, 340, 360, 380])
southshore_cherries = np.array([200, 205, 210, 215, 220])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Stacking the bars
ax.bar(years, northland_apples, label='Northland Apples', color='#66c2a5')
ax.bar(years, northland_bananas, bottom=northland_apples, label='Northland Bananas', color='#fc8d62')
ax.bar(years, northland_cherries, bottom=northland_apples+northland_bananas, label='Northland Cherries', color='#8da0cb')

ax.bar(years, midlands_apples, bottom=northland_apples+northland_bananas+northland_cherries, label='Midlands Apples', color='#e78ac3')
ax.bar(years, midlands_bananas, bottom=northland_apples+northland_bananas+northland_cherries+midlands_apples, label='Midlands Bananas', color='#a6d854')
ax.bar(years, midlands_cherries, bottom=northland_apples+northland_bananas+northland_cherries+midlands_apples+midlands_bananas, label='Midlands Cherries', color='#ffd92f')

ax.bar(years, southshore_apples, bottom=northland_apples+northland_bananas+northland_cherries+midlands_apples+midlands_bananas+midlands_cherries, label='Southshore Apples', color='#e5c494')
ax.bar(years, southshore_bananas, bottom=northland_apples+northland_bananas+northland_cherries+midlands_apples+midlands_bananas+midlands_cherries+southshore_apples, label='Southshore Bananas', color='#b3b3b3')
ax.bar(years, southshore_cherries, bottom=northland_apples+northland_bananas+northland_cherries+midlands_apples+midlands_bananas+midlands_cherries+southshore_apples+southshore_bananas, label='Southshore Cherries', color='#1b9e77')

# Adding title and labels
ax.set_title('Annual Fruit Production in Three Regions\n(2019-2023)', fontsize=16)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Production in Tons', fontsize=14)

# Adding legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Fruits and Regions', fontsize=10, frameon=False)

# Adjust the y-axis to comfortably fit the data
ax.set_ylim(0, 2500)

# Rotate x-axis labels if needed
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()