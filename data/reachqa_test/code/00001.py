import matplotlib.pyplot as plt
import numpy as np

# Years for the data
years = [str(year) for year in range(2015, 2024)]

# Market share data for each platform
whatsapp_share = [25, 28, 30, 35, 40, 45, 50, 55, 60]
facebook_share = [45, 43, 40, 38, 36, 35, 34, 32, 30]
instagram_share = [10, 12, 15, 16, 17, 18, 19, 20, 22]
tiktok_share = [1, 3, 5, 12, 15, 18, 20, 22, 25]
snapchat_share = [5, 6, 7, 8, 9, 10, 11, 12, 14]
twitter_share = [14, 12, 11, 10, 9, 8, 7, 6, 5]

# Initialize a figure and axis
fig, ax = plt.subplots(figsize=(14, 9))

# Plot stacked bars
ax.bar(years, whatsapp_share, label='WhatsApp', color='lightgreen', alpha=0.8)
ax.bar(years, facebook_share, bottom=whatsapp_share, label='Facebook', color='royalblue', alpha=0.8)
ax.bar(years, instagram_share, bottom=np.array(whatsapp_share) + np.array(facebook_share), label='Instagram', color='mediumvioletred', alpha=0.8)
ax.bar(years, tiktok_share, bottom=np.array(whatsapp_share) + np.array(facebook_share) + np.array(instagram_share), label='TikTok', color='orange', alpha=0.8)
ax.bar(years, snapchat_share, bottom=np.array(whatsapp_share) + np.array(facebook_share) + np.array(instagram_share) + np.array(tiktok_share), label='Snapchat', color='yellowgreen', alpha=0.8)
ax.bar(years, twitter_share, bottom=np.array(whatsapp_share) + np.array(facebook_share) + np.array(instagram_share) + np.array(tiktok_share) + np.array(snapchat_share), label='Twitter', color='lightskyblue', alpha=0.8)

# Add title and labels with enhanced details
ax.set_title('Evolving Landscape of Social Media Platforms\nMarket Share in Emerging Markets (2015-2023)', fontsize=16, pad=30)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Market Share (%)', fontsize=14)

# Add a legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='medium', title='Platforms')

# Draw a grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Highlight trends with dashed line
trendline = np.array([sum(x) for x in zip(whatsapp_share, facebook_share, instagram_share, tiktok_share, snapchat_share, twitter_share)])
ax.plot(years, trendline, color='darkslategray', linestyle='--', marker='o', label='Total Market Share')

# Adjust x-axis labels to avoid overlap
plt.xticks(rotation=45, ha='right')

# Automatically adjust the layout to make sure everything fits
plt.tight_layout()

# Display the plot
plt.show()