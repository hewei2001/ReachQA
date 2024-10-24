import matplotlib.pyplot as plt
import numpy as np

# Define the years and fashion styles
years = np.arange(2010, 2021)
styles = ["Minimalism", "Vintage", "Bohemian", "Streetwear", "Athleisure"]

# Popularity data for each style over the years
popularity_data = np.array([
    [15, 18, 20, 24, 28, 34, 36, 35, 40, 45, 50],   # Minimalism
    [30, 28, 25, 22, 20, 19, 18, 17, 15, 14, 13],   # Vintage
    [10, 12, 15, 18, 25, 28, 30, 32, 34, 37, 40],   # Bohemian
    [25, 22, 20, 18, 17, 20, 24, 28, 30, 33, 35],   # Streetwear
    [5, 8, 10, 14, 20, 22, 25, 30, 32, 35, 38]      # Athleisure
])

# Revenue data for each style over the years (in millions)
revenue_data = np.array([
    [20, 22, 23, 25, 30, 35, 38, 40, 42, 45, 50],   # Minimalism
    [50, 48, 45, 40, 38, 35, 30, 28, 26, 24, 22],   # Vintage
    [15, 18, 20, 25, 30, 32, 35, 38, 42, 45, 50],   # Bohemian
    [40, 38, 37, 35, 36, 38, 40, 42, 45, 48, 50],   # Streetwear
    [10, 15, 18, 20, 25, 28, 32, 35, 40, 45, 50]    # Athleisure
])

# Stack the data for the area chart
cumulative_popularity = np.cumsum(popularity_data, axis=0)

# Set up the plot with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Define colors for each style
colors = ['#E63946', '#F1FAEE', '#A8DADC', '#457B9D', '#1D3557']

# Plot each fashion style's area for the popularity subplot
for i, (style, color) in enumerate(zip(styles, colors)):
    ax1.fill_between(years, cumulative_popularity[i-1] if i > 0 else 0, cumulative_popularity[i],
                     color=color, label=style, alpha=0.8)

ax1.set_title('Evolution of Fashion Trends\nPopularity Index (2010-2020)', fontsize=14, fontweight='bold', color='navy')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Popularity Index', fontsize=12)
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Fashion Styles', fontsize=10)
ax1.annotate('Athleisure Boom', xy=(2015, cumulative_popularity[-1][5]), 
             xytext=(2016, 160), arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Plot the line chart for the revenue subplot
for i, (style, color) in enumerate(zip(styles, colors)):
    ax2.plot(years, revenue_data[i], label=style, color=color, marker='o', linewidth=2, alpha=0.8)

ax2.set_title('Revenue Contribution by Fashion Style\n(2010-2020)', fontsize=14, fontweight='bold', color='navy')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Revenue (in millions)', fontsize=12)
ax2.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax2.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Fashion Styles', fontsize=10)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)

# Automatically adjust layout
plt.tight_layout(rect=[0, 0, 0.9, 1])

# Display the plot
plt.show()