import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2005 to 2020
years = np.arange(2005, 2021)

# Adjusted market share data for better distribution
cd_market_share = np.array([80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5])
digital_downloads_share = np.array([10, 15, 20, 25, 30, 35, 35, 30, 25, 20, 15, 10, 7, 5, 4, 3])
streaming_share = 100 - (cd_market_share + digital_downloads_share)

# Adjusted revenue data (in millions) for better distribution
cd_revenue = np.array([1200, 1100, 950, 850, 700, 600, 450, 400, 300, 200, 100, 80, 60, 40, 20, 10])
digital_downloads_revenue = np.array([150, 180, 200, 240, 280, 350, 370, 350, 320, 290, 250, 220, 180, 150, 120, 100])
streaming_revenue = np.array([20, 30, 50, 100, 160, 220, 300, 400, 500, 650, 800, 950, 1100, 1250, 1400, 1600])

# Create the figure and two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8), sharex=True)

# Subplot 1: Stacked bar chart for market share
ax1.bar(years, cd_market_share, color='skyblue', width=0.6, edgecolor='black', label='CDs', alpha=0.8)
ax1.bar(years, digital_downloads_share, bottom=cd_market_share, color='lightcoral', width=0.6, edgecolor='black', label='Digital Downloads', alpha=0.8)
ax1.bar(years, streaming_share, bottom=cd_market_share + digital_downloads_share, color='lightgreen', width=0.6, edgecolor='black', label='Streaming', alpha=0.8)

ax1.set_title('Market Share Evolution of Music Formats\n(2005-2020)', fontsize=14, fontweight='bold')
ax1.set_ylabel('Market Share (%)', fontsize=12)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, fontsize=10)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.legend(title='Music Formats', fontsize=10)

ax1.annotate('Streaming overtakes Downloads', xy=(2014, 70), xytext=(2010, 85),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='navy')

# Subplot 2: Line chart for revenue
ax2.plot(years, cd_revenue, color='skyblue', marker='o', label='CDs', linewidth=2)
ax2.plot(years, digital_downloads_revenue, color='lightcoral', marker='o', label='Digital Downloads', linewidth=2)
ax2.plot(years, streaming_revenue, color='lightgreen', marker='o', label='Streaming', linewidth=2)

ax2.set_title('Revenue from Music Formats (Millions)\n(2005-2020)', fontsize=14, fontweight='bold')
ax2.set_ylabel('Revenue (Millions)', fontsize=12)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45, fontsize=10)
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)
ax2.legend(title='Music Formats', fontsize=10)

# Automatically adjust layout for better spacing
plt.tight_layout(pad=5)

# Show the plot
plt.show()