import matplotlib.pyplot as plt
import numpy as np

years = list(range(2010, 2021))

instagram_influencers = [100, 200, 500, 1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000]
tiktok_influencers = [0, 0, 0, 100, 500, 1000, 2000, 3000, 4000, 5000, 6000]
youtube_influencers = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

ax1.plot(years, instagram_influencers, label='Instagram', marker='o', linestyle='-', linewidth=2, color='blue')
ax1.plot(years, tiktok_influencers, label='TikTok', marker='s', linestyle='--', linewidth=2, color='green')
ax1.plot(years, youtube_influencers, label='YouTube', marker='D', linestyle='-.', linewidth=2, color='red')

ax1.set_title("The Rise of Social Media Influencers:\nA Decade of Growth")
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Influencers')
ax1.grid(True)
ax1.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

# Secondary chart: Influencer growth rate
growth_rates = [np.diff(instagram_influencers), np.diff(tiktok_influencers), np.diff(youtube_influencers)]
labels = ['Instagram', 'TikTok', 'YouTube']
colors = ['blue', 'green', 'red']
ax2.bar(labels, [np.mean(growth_rate) for growth_rate in growth_rates], color=colors)
ax2.set_title("Average Annual Growth Rate")
ax2.set_ylabel("Growth Rate")
ax2.set_ylim(0, 2000)

plt.tight_layout()
plt.show()