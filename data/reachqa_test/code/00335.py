import matplotlib.pyplot as plt
import numpy as np

# Original data for donut chart
languages = ['English', 'Chinese', 'Spanish', 'French', 'German', 'Others']
usage_percentages = [60, 15, 10, 5, 5, 5]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Additional data for bar chart
# This data represents a hypothetical change in publication share over the last decade
languages_trend = ['English', 'Chinese', 'Spanish', 'French', 'German', 'Others']
growth_percentages = [2, 10, 8, -1, 0, -3]  # Positive and negative values

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Plot the donut chart
wedges, texts, autotexts = ax1.pie(usage_percentages, labels=languages, autopct='%1.1f%%', startangle=140,
                                   pctdistance=0.85, colors=colors, wedgeprops=dict(width=0.3, edgecolor='w', alpha=0.9))
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax1.add_artist(centre_circle)

# Adjust text in donut chart
for text in texts:
    text.set_color('darkblue')
    text.set_fontsize(12)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(11)

ax1.axis('equal')
ax1.set_title('Linguistic Diversity in Scientific Publications', fontsize=14, fontweight='bold', pad=20)

# Plot the bar chart for trend data
bars = ax2.bar(languages_trend, growth_percentages, color=colors, edgecolor='black', alpha=0.7)

# Annotate each bar with the growth percentage
for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:+.0f}%', ha='center', va='bottom', fontsize=11, fontweight='bold')

# Styling and labels for bar chart
ax2.set_title('Change in Publication Share Over the Last Decade', fontsize=14, fontweight='bold', pad=20)
ax2.axhline(0, color='grey', linewidth=0.8)
ax2.set_ylabel('Growth Percentage', fontsize=12)
ax2.set_xticklabels(languages_trend, rotation=45, ha='right', fontsize=11)
ax2.set_yticks(np.arange(-5, 15, 5))
ax2.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout to ensure all elements fit well
plt.tight_layout()

# Display the plot
plt.show()