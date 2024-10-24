import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2015 to 2022
years = np.arange(2015, 2023)

# Define the hypothetical user growth data for each social media platform (in millions)
users_chatverse = np.array([50, 55, 63, 75, 90, 110, 135, 160])
users_mediahub = np.array([70, 78, 85, 92, 95, 97, 99, 100])
users_picshare = np.array([20, 27, 35, 45, 60, 80, 105, 130])
users_buzztalk = np.array([10, 20, 30, 50, 75, 110, 150, 200])

# Calculate growth rates as a percentage from year to year
growth_chatverse = np.diff(users_chatverse) / users_chatverse[:-1] * 100
growth_mediahub = np.diff(users_mediahub) / users_mediahub[:-1] * 100
growth_picshare = np.diff(users_picshare) / users_picshare[:-1] * 100
growth_buzztalk = np.diff(users_buzztalk) / users_buzztalk[:-1] * 100

# Years for growth rates (excluding the first year)
growth_years = years[1:]

# Create a figure with two subplots side-by-side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# First subplot: Line plot for user growth
ax1.plot(years, users_chatverse, marker='o', linestyle='-', color='#1f77b4', linewidth=2, label='ChatVerse')
ax1.plot(years, users_mediahub, marker='s', linestyle='--', color='#2ca02c', linewidth=2, label='MediaHub')
ax1.plot(years, users_picshare, marker='^', linestyle='-.', color='#ff7f0e', linewidth=2, label='PicShare')
ax1.plot(years, users_buzztalk, marker='d', linestyle=':', color='#d62728', linewidth=2, label='BuzzTalk')
ax1.set_title('Digital Evolution: Social Media Platform User Growth\n(2015-2022)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Users (in millions)', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend(title='Platforms', fontsize=10, title_fontsize=12, loc='upper left')
ax1.set_xticks(years)

# Second subplot: Bar chart for annual growth rates
ax2.bar(growth_years - 0.2, growth_chatverse, width=0.2, color='#1f77b4', align='center', label='ChatVerse')
ax2.bar(growth_years, growth_mediahub, width=0.2, color='#2ca02c', align='center', label='MediaHub')
ax2.bar(growth_years + 0.2, growth_picshare, width=0.2, color='#ff7f0e', align='center', label='PicShare')
ax2.bar(growth_years + 0.4, growth_buzztalk, width=0.2, color='#d62728', align='center', label='BuzzTalk')
ax2.set_title('Annual Growth Rates of Users (%)\n(2016-2022)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend(title='Platforms', fontsize=10, title_fontsize=12, loc='upper right')
ax2.set_xticks(growth_years)

# Automatically adjust the layout for neatness
plt.tight_layout()

# Display the plots
plt.show()