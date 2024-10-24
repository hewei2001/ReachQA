import matplotlib.pyplot as plt
import numpy as np

# Data construction
years = np.arange(2010, 2020)

# Number of expeditions for each country
usa_expeditions = [12, 15, 13, 20, 17, 22, 25, 30, 28, 35]
china_expeditions = [10, 13, 17, 19, 22, 26, 29, 33, 36, 40]
india_expeditions = [8, 9, 11, 14, 16, 18, 21, 23, 26, 30]
brazil_expeditions = [7, 8, 10, 12, 14, 15, 17, 20, 22, 25]
russia_expeditions = [11, 12, 15, 18, 21, 24, 27, 31, 34, 38]

# Total distance covered in kilometers
usa_distance = [15000, 18000, 17000, 22000, 21000, 26000, 30000, 35000, 34000, 40000]
china_distance = [14000, 16000, 20000, 23000, 25000, 28000, 32000, 37000, 40000, 45000]
india_distance = [9000, 10000, 12000, 15000, 17000, 19000, 21000, 25000, 27000, 31000]
brazil_distance = [8000, 8500, 11000, 14000, 16000, 17000, 19000, 23000, 26000, 30000]
russia_distance = [13000, 15000, 18000, 22000, 24000, 27000, 31000, 36000, 38000, 43000]

# Colors for each country
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create a figure with 1x2 grid for subplots
fig, axs = plt.subplots(1, 2, figsize=(20, 8))

# Scatter plot of expeditions vs. distance
axs[0].scatter(usa_expeditions, usa_distance, color=colors[0], s=100, edgecolor='k', marker='o', alpha=0.7, label='USA')
axs[0].scatter(china_expeditions, china_distance, color=colors[1], s=100, edgecolor='k', marker='s', alpha=0.7, label='China')
axs[0].scatter(india_expeditions, india_distance, color=colors[2], s=100, edgecolor='k', marker='^', alpha=0.7, label='India')
axs[0].scatter(brazil_expeditions, brazil_distance, color=colors[3], s=100, edgecolor='k', marker='D', alpha=0.7, label='Brazil')
axs[0].scatter(russia_expeditions, russia_distance, color=colors[4], s=100, edgecolor='k', marker='P', alpha=0.7, label='Russia')

axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].set_title('Expeditions vs. Distance Traveled\n(2010-2019)', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Number of Expeditions Launched', fontsize=12)
axs[0].set_ylabel('Total Distance Traveled (in km)', fontsize=12)
axs[0].legend(title='Countries', fontsize=10, title_fontsize='11', loc='upper left')

# Annotations in the scatter plot
axs[0].annotate('USA Rapid Surge', xy=(30, 35000), xytext=(32, 30000),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, fontweight='bold')
axs[0].annotate('China Leading Reach', xy=(36, 40000), xytext=(34, 36000),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, fontweight='bold')

# Line plot showing cumulative expeditions over years
cumulative_usa_expeditions = np.cumsum(usa_expeditions)
cumulative_china_expeditions = np.cumsum(china_expeditions)

axs[1].plot(years, cumulative_usa_expeditions, marker='o', color=colors[0], linestyle='-', linewidth=2, label='USA')
axs[1].plot(years, cumulative_china_expeditions, marker='s', color=colors[1], linestyle='-', linewidth=2, label='China')

axs[1].grid(True, linestyle='--', alpha=0.6)
axs[1].set_title('Cumulative Expeditions Over Years', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Cumulative Expeditions', fontsize=12)
axs[1].legend(title='Countries', fontsize=10, title_fontsize='11', loc='upper left')

# Automatically adjust subplot parameters for better layout
plt.tight_layout()

# Display the plots
plt.show()