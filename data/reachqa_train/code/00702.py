import numpy as np
import matplotlib.pyplot as plt

# Define years and marketing channels
years = np.arange(2010, 2024)
channels = ['Print Media', 'Television', 'Online Advertising', 'Social Media', 'Influencer Marketing']

# Data for each channel
print_media = np.array([50, 45, 42, 38, 35, 30, 28, 25, 22, 20, 18, 15, 12, 10])
television = np.array([60, 58, 55, 52, 50, 47, 45, 42, 38, 35, 32, 28, 25, 20])
online_advertising = np.array([30, 35, 40, 45, 50, 55, 58, 60, 65, 68, 70, 72, 75, 78])
social_media = np.array([20, 25, 30, 35, 42, 50, 58, 65, 72, 78, 82, 88, 92, 95])
influencer_marketing = np.array([5, 8, 12, 16, 20, 25, 30, 38, 45, 52, 58, 65, 72, 80])

# Aggregate data for stacking
data = np.vstack([print_media, television, online_advertising, social_media, influencer_marketing])

# Calculate cumulative sum to use for the line plot
cumulative_trends = data.sum(axis=0)

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# Stacked area chart on the first subplot
axs[0].stackplot(years, data, labels=channels, alpha=0.8, 
                 colors=['#ff9999', '#66b2ff', '#99ff99', '#ffcc99', '#c2c2f0'])
axs[0].set_title('Evolution of Marketing Strategies\nin the Digital Era (2010-2023)', fontsize=16, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Marketing Focus Intensity', fontsize=12)
axs[0].set_xticks(years)
axs[0].set_yticks(np.arange(0, 300, 20))
axs[0].legend(loc='upper left', title='Marketing Channels', fontsize=10)
axs[0].grid(axis='y', linestyle='--', alpha=0.7)

# Line plot for cumulative trend on the second subplot
axs[1].plot(years, cumulative_trends, marker='o', color='#66c2a5', linestyle='-', linewidth=2)
axs[1].fill_between(years, 0, cumulative_trends, color='#a6dba0', alpha=0.5)
axs[1].set_title('Cumulative Marketing Trend (2010-2023)', fontsize=16, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Cumulative Intensity', fontsize=12)
axs[1].set_xticks(years)
axs[1].set_yticks(np.arange(0, 300, 20))
axs[1].grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()