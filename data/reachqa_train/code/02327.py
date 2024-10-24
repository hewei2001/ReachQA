import matplotlib.pyplot as plt
import numpy as np

# Social media platforms and their engagement scores
platforms = ['Instagram', 'Facebook', 'Twitter', 'LinkedIn', 'TikTok', 'Snapchat']
engagement_scores = [85, 78, 50, 60, 92, 45]

# Positions of bars on x-axis
x_pos = np.arange(len(platforms))

# Define colors for each platform
colors = ['#FF7F50', '#1E90FF', '#32CD32', '#FFD700', '#FF69B4', '#8A2BE2']

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.bar(x_pos, engagement_scores, color=colors, width=0.6)

# Adding value annotations on each bar
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 1, str(yval), ha='center', va='bottom', fontsize=10)

# Setting title and axis labels
ax.set_title("The Social Architect:\nEngagement Levels on Popular Social Media Platforms in 2023",
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Social Media Platforms", fontsize=12)
ax.set_ylabel("Engagement Score", fontsize=12)

# Customize x-ticks to avoid overlap and improve readability
ax.set_xticks(x_pos)
ax.set_xticklabels(platforms, fontsize=11, rotation=15)

# Add grid lines only on the y-axis
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Optimize layout
plt.tight_layout()

# Display the chart
plt.show()