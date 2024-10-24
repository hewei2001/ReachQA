import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import cm
import numpy as np

# Data for the market share of different cuisines
cuisines = ['Italian', 'Asian Fusion', 'Mexican', 'Middle Eastern', 'American', 'Vegan/Vegetarian']
market_share = [20, 25, 15, 10, 15, 15]

# Create a colormap for gradient effect
cmap = cm.get_cmap('Set3')

# Create a figure and axis with two subplots
fig, ax = plt.subplots(1, 2, figsize=(16, 8), subplot_kw=dict(aspect="equal"))

# Plot a donut pie chart with explosion for the largest segment
explode = [0, 0.1, 0, 0, 0, 0]
wedges, texts, autotexts = ax[0].pie(market_share, labels=cuisines, autopct='%1.1f%%', startangle=140,
                                     explode=explode, shadow=True, colors=cmap.colors[:6],
                                     wedgeprops=dict(width=0.3, edgecolor='w'))

# Add a gradient effect
for i, wedge in enumerate(wedges):
    wedge.set_facecolor(cmap(0.1 * i + 0.1))

# Add a circle at the center to make it a donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax[0].add_artist(centre_circle)

# Add a title
ax[0].set_title('The Culinary Evolution\nof Urban Cuisine:\nMarket Share in 2023', fontsize=14, fontweight='bold', ha='center')

# Improve readability of the text
plt.setp(texts, size=12, weight="bold")
plt.setp(autotexts, size=10, weight="bold", color="darkblue")

# Add a legend outside the plot area
ax[0].legend(wedges, cuisines, title="Cuisines", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Second subplot: Bar chart for comparative visualization
x = np.arange(len(cuisines))
bar_colors = cmap.colors[:6]
ax[1].barh(x, market_share, color=bar_colors, edgecolor='darkgray')

# Adding text labels inside bars
for i, (val, color) in enumerate(zip(market_share, bar_colors)):
    ax[1].text(val, i, f'{val}%', va='center', ha='right', fontsize=10, color='black')

# Set the labels and title
ax[1].set_yticks(x)
ax[1].set_yticklabels(cuisines, fontsize=12, fontweight='bold')
ax[1].set_xlabel('Market Share (%)', fontsize=12, fontweight='bold')
ax[1].set_title('Comparative Market Share\nby Cuisine Type', fontsize=14, fontweight='bold', ha='center')

# Enhance layout
plt.tight_layout()

# Display the plot
plt.show()