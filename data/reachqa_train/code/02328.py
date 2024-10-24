import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart (current engagement scores)
platforms = ['Instagram', 'Facebook', 'Twitter', 'LinkedIn', 'TikTok', 'Snapchat']
engagement_scores = [85, 78, 50, 60, 92, 45]

# Additional data for the line chart (historical engagement scores over years)
years = np.arange(2018, 2024)
historical_engagement = {
    'Instagram': [70, 75, 80, 82, 84, 85],
    'Facebook': [80, 79, 77, 78, 78, 78],
    'Twitter': [55, 53, 52, 51, 50, 50],
    'LinkedIn': [60, 59, 58, 59, 60, 60],
    'TikTok': [50, 60, 70, 80, 90, 92],
    'Snapchat': [48, 50, 46, 45, 44, 45]
}

# Define colors for each platform
colors = ['#FF7F50', '#1E90FF', '#32CD32', '#FFD700', '#FF69B4', '#8A2BE2']

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# Plotting the bar chart on the first subplot
x_pos = np.arange(len(platforms))
bars = ax1.bar(x_pos, engagement_scores, color=colors, width=0.6)
ax1.set_title("Engagement Levels on Social Media Platforms\n in 2023", fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel("Social Media Platforms", fontsize=12)
ax1.set_ylabel("Engagement Score", fontsize=12)
ax1.set_xticks(x_pos)
ax1.set_xticklabels(platforms, fontsize=11, rotation=15)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Annotating the bar chart
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 1, str(yval), ha='center', va='bottom', fontsize=10)

# Plotting the line chart on the second subplot
for idx, platform in enumerate(platforms):
    ax2.plot(years, historical_engagement[platform], label=platform, color=colors[idx], marker='o')

ax2.set_title("Trend of Engagement Scores\n (2018-2023)", fontsize=14, fontweight='bold', pad=15)
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Engagement Score", fontsize=12)
ax2.legend(title="Platforms", fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the charts
plt.show()