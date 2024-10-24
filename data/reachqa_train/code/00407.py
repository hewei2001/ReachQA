import matplotlib.pyplot as plt
import numpy as np

# Define continents and platforms
continents = ['North America', 'Europe', 'Asia', 'South America', 'Africa']
platforms = ['Facebook', 'Instagram', 'Twitter', 'TikTok', 'LinkedIn']

# Social media platform preferences for each continent (percentage)
data = np.array([
    [40, 30, 15, 10, 5],   # North America
    [35, 25, 20, 15, 5],   # Europe
    [20, 25, 30, 20, 5],   # Asia
    [45, 20, 10, 20, 5],   # South America
    [50, 20, 10, 10, 10]   # Africa
])

# Define colors for the platforms
colors = ['#3b5998', '#E1306C', '#1DA1F2', '#69C9D0', '#0e76a8']

# Create a subplot for each continent
fig, axes = plt.subplots(2, 3, figsize=(14, 8), subplot_kw=dict(aspect="equal"))
axes = axes.flatten()
fig.delaxes(axes[-1])  # Remove the last empty subplot

# Plot pie charts for each continent
for i, ax in enumerate(axes[:-1]):  # Only iterate over the first 5 axes
    wedges, texts, autotexts = ax.pie(
        data[i], labels=platforms, autopct='%1.1f%%', startangle=140,
        colors=colors, textprops=dict(color="w"), explode=(0.1, 0, 0, 0, 0)
    )
    
    # Set properties for the wedges and text
    for wedge in wedges:
        wedge.set_edgecolor('white')
    for autotext in autotexts:
        autotext.set_size(10)
        autotext.set_weight('bold')

    ax.set_title(continents[i], fontsize=12, weight='bold', color='navy')

# Set the main title for the figure
plt.suptitle(
    'Global Social Media Usage\nPlatform Preferences by Continent',
    fontsize=16, weight='bold', y=0.95
)

# Adjust layout to avoid overlap
plt.tight_layout()
plt.subplots_adjust(top=0.85)

# Create a legend outside the plot for clarity
fig.legend(
    platforms, loc='lower center', ncol=5, fontsize=10,
    frameon=False, title='Social Media Platforms', title_fontsize='11'
)

# Display the plot
plt.show()