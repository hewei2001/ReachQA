import matplotlib.pyplot as plt
import numpy as np

# Data: Annual book sales in thousands for each genre from 2010 to 2020
fantasy_sales = [340, 365, 400, 390, 420, 410, 450, 460, 455, 490, 480]
scifi_sales = [310, 290, 320, 330, 350, 345, 360, 370, 380, 390, 405]
mystery_sales = [250, 260, 270, 280, 290, 295, 300, 310, 320, 330, 340]
historical_sales = [150, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]

# Combine data into a list for box plot
data = [fantasy_sales, scifi_sales, mystery_sales, historical_sales]
genres = ['Fantasy', 'Science Fiction', 'Mystery', 'Historical Fiction']
years = np.arange(2010, 2021)

# Calculate average annual sales
average_sales = [np.mean([fantasy_sales[i], scifi_sales[i], mystery_sales[i], historical_sales[i]]) for i in range(len(years))]

# Create a subplot layout: 1 row, 2 columns
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Box Plot (Distribution)
boxplot = axs[0].boxplot(data, vert=True, patch_artist=True, labels=genres, notch=True, widths=0.6)
colors = ['#FFB6C1', '#B0E0E6', '#FFD700', '#98FB98']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

axs[0].set_title("Book Sales Distribution by Genre\nin Noverra (2010-2020)", fontsize=12, fontweight='bold')
axs[0].set_xlabel("Genre", fontsize=10)
axs[0].set_ylabel("Annual Book Sales (in thousands)", fontsize=10)
axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)
axs[0].set_axisbelow(True)
plt.setp(boxplot['whiskers'], color='black', linestyle='-', linewidth=1.5)
plt.setp(boxplot['caps'], color='black', linewidth=1.5)
plt.setp(boxplot['medians'], color='red', linewidth=2)

# Line Plot (Trend)
axs[1].plot(years, fantasy_sales, marker='o', color='#FFB6C1', label='Fantasy')
axs[1].plot(years, scifi_sales, marker='o', color='#B0E0E6', label='Science Fiction')
axs[1].plot(years, mystery_sales, marker='o', color='#FFD700', label='Mystery')
axs[1].plot(years, historical_sales, marker='o', color='#98FB98', label='Historical Fiction')
axs[1].plot(years, average_sales, marker='x', linestyle='--', color='gray', label='Average')
axs[1].set_title("Book Sales Trend (2010-2020)", fontsize=12, fontweight='bold')
axs[1].set_xlabel("Year", fontsize=10)
axs[1].set_ylabel("Annual Book Sales (in thousands)", fontsize=10)
axs[1].legend(loc='upper left', fontsize=8)
axs[1].grid(True, linestyle='--', alpha=0.7)

# Adjust layout to ensure everything fits without overlap
plt.tight_layout()

# Display the plots
plt.show()