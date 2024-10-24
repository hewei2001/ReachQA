import numpy as np
import matplotlib.pyplot as plt

# Define years and marketing channels
years = np.arange(2010, 2024)
channels = ['Print Media', 'Television', 'Online Advertising', 'Social Media', 'Influencer Marketing']

# Data for each channel (explicitly created to represent market trends)
print_media = np.array([50, 45, 42, 38, 35, 30, 28, 25, 22, 20, 18, 15, 12, 10])
television = np.array([60, 58, 55, 52, 50, 47, 45, 42, 38, 35, 32, 28, 25, 20])
online_advertising = np.array([30, 35, 40, 45, 50, 55, 58, 60, 65, 68, 70, 72, 75, 78])
social_media = np.array([20, 25, 30, 35, 42, 50, 58, 65, 72, 78, 82, 88, 92, 95])
influencer_marketing = np.array([5, 8, 12, 16, 20, 25, 30, 38, 45, 52, 58, 65, 72, 80])

# Aggregate data for stacking
data = np.vstack([print_media, television, online_advertising, social_media, influencer_marketing])

# Plotting the stacked area chart
plt.figure(figsize=(12, 8))

# Create stacked area chart
plt.stackplot(years, data, labels=channels, alpha=0.8, colors=['#ff9999', '#66b2ff', '#99ff99', '#ffcc99', '#c2c2f0'])

# Customizing plot elements
plt.title('Evolution of Marketing Strategies in the Digital Era (2010-2023)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Marketing Focus Intensity', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 300, 20))
plt.legend(loc='upper left', title='Marketing Channels', title_fontsize='13', fontsize='10', bbox_to_anchor=(1.05, 1))
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()