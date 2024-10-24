import matplotlib.pyplot as plt
import numpy as np

# Data: Annual book sales in thousands for each genre from 2010 to 2020
fantasy_sales = [340, 365, 400, 390, 420, 410, 450, 460, 455, 490, 480]
scifi_sales = [310, 290, 320, 330, 350, 345, 360, 370, 380, 390, 405]
mystery_sales = [250, 260, 270, 280, 290, 295, 300, 310, 320, 330, 340]
historical_sales = [150, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]

# Combine data into a single list for box plot
data = [fantasy_sales, scifi_sales, mystery_sales, historical_sales]
genres = ['Fantasy', 'Science Fiction', 'Mystery', 'Historical Fiction']

# Create the box plot
fig, ax = plt.subplots(figsize=(10, 6))
boxplot = ax.boxplot(data, vert=True, patch_artist=True, labels=genres, notch=True, widths=0.6)

# Customizing colors for each genre box
colors = ['#FFB6C1', '#B0E0E6', '#FFD700', '#98FB98']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

# Adding title and labels
plt.title("Evolution of Book Sales by Genre\nin Noverra (2010-2020)", fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Genre", fontsize=12)
plt.ylabel("Annual Book Sales (in thousands)", fontsize=12)

# Adding grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Customize other plot elements
plt.setp(boxplot['whiskers'], color='black', linestyle='-', linewidth=1.5)
plt.setp(boxplot['caps'], color='black', linewidth=1.5)
plt.setp(boxplot['medians'], color='red', linewidth=2)

# Adjust layout to prevent clipping of tick-labels
plt.tight_layout()

# Display the plot
plt.show()