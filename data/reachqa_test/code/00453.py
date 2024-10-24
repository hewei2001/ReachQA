import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.ticker import AutoMinorLocator

# Defining the years and slightly adjusted sales data
years = np.arange(2000, 2024)
fiction_sales = np.array([120, 130, 140, 145, 150, 160, 180, 195, 210, 225, 240, 250, 260, 275, 290, 310, 330, 350, 370, 390, 410, 430, 450, 470])
non_fiction_sales = np.array([100, 110, 120, 125, 130, 140, 135, 130, 125, 120, 115, 110, 105, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50])
science_fiction_sales = np.array([60, 65, 70, 75, 80, 85, 90, 100, 110, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 240, 255, 270])
fantasy_sales = np.array([50, 55, 60, 65, 70, 75, 80, 90, 100, 110, 120, 130, 140, 150, 165, 180, 195, 210, 230, 250, 270, 290, 310, 330])

# Create the figure and axis
plt.figure(figsize=(14, 10))

# Define color palette
colors = sns.color_palette("Set1", 4)

# Plotting the sales data with area fill under the lines
plt.plot(years, fiction_sales, marker='o', linestyle='-', linewidth=1.8, markersize=5, label='Fiction', color=colors[0], alpha=0.9)
plt.fill_between(years, fiction_sales, alpha=0.1, color=colors[0])

plt.plot(years, non_fiction_sales, marker='s', linestyle='--', linewidth=1.8, markersize=5, label='Non-Fiction', color=colors[1], alpha=0.9)
plt.fill_between(years, non_fiction_sales, alpha=0.1, color=colors[1])

plt.plot(years, science_fiction_sales, marker='^', linestyle='-.', linewidth=1.8, markersize=5, label='Science Fiction', color=colors[2], alpha=0.9)
plt.fill_between(years, science_fiction_sales, alpha=0.1, color=colors[2])

plt.plot(years, fantasy_sales, marker='d', linestyle=':', linewidth=1.8, markersize=5, label='Fantasy', color=colors[3], alpha=0.9)
plt.fill_between(years, fantasy_sales, alpha=0.1, color=colors[3])

# Adding titles and labels
plt.title("Literature Over Time:\nTrends in Book Sales by Genre (2000-2023)", fontsize=18, fontweight='bold')
plt.xlabel("Year", fontsize=14)
plt.ylabel("Book Sales (in thousands)", fontsize=14)
plt.xticks(years[::2], rotation=45)  # Only showing every second year for better readability
plt.yticks(np.arange(0, 550, 50))

# Moving legend inside plot to avoid occlusion
plt.legend(title="Genres", title_fontsize='13', fontsize='12', loc='upper left')

# Adding grid with improved styling
plt.grid(True, linestyle='--', alpha=0.7)

# Annotations for significant years
plt.annotate('Peak Sales', xy=(2023, 470), xytext=(2018, 510),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

# Data source annotation
plt.figtext(0.5, 0.01, "Data Source: Fictional Book Sales Database 2023", ha="center", fontsize=10, color='gray')

# Minor ticks
plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
plt.gca().yaxis.set_minor_locator(AutoMinorLocator())

# Adjust layout to avoid overlapping text
plt.tight_layout(rect=[0, 0.05, 0.95, 1])

# Show the plot
plt.show()