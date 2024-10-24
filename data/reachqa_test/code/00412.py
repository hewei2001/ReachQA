import matplotlib.pyplot as plt

# Platform names and their market shares in percentages
platforms = ['Facebook', 'YouTube', 'WhatsApp', 'Instagram', 'TikTok', 'WeChat', 'Qzone', 'Twitter', 'LinkedIn', 'Reddit', 'Pinterest']
market_share = [22, 18, 16, 12, 10, 8, 5, 4, 3, 1, 1]

# Explode slices for larger market shares
explode = [0.1 if share >= 10 else 0 for share in market_share]

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(market_share, explode=explode, labels=platforms, autopct='%1.1f%%', 
                                  pctdistance=0.85, startangle=140, textprops=dict(color="w", fontweight="bold"))

# Ensure the pie chart is a circle
ax.axis('equal')

# Title with padding
ax.set_title("Market Share of Social Media Platforms in 2023", pad=20)

# Apply a custom color palette
colors = plt.cm.Set3(range(len(platforms)))
for wedge, color in zip(wedges, colors):
    wedge.set_facecolor(color)
    wedge.set_edgecolor('white')
    wedge.set_linewidth(1)

# Adjust text properties for better visibility
for text in texts:
    text.set_fontsize(12)
    text.set_color('black')
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('black')

# Legend with percentages
custom_labels = [f"{platform}: {share:.1f}%" for platform, share in zip(platforms, market_share)]
ax.legend(wedges, custom_labels, title="Platforms", loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3)

# Adjust layout and display the chart
plt.tight_layout()
plt.show()