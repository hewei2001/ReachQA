import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Data for the sector pie chart
genres = ['Classical', 'Folk', 'Jazz', 'Blues', 'Reggae']
continent_distribution = [35, 25, 20, 10, 10]

# Enhanced color palette with distinct colors
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6666']

# Explode both 'Classical' and 'Blues' slices
explode = (0.1, 0, 0, 0.1, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    continent_distribution, explode=explode, labels=genres,
    autopct='%1.1f%%', shadow=True, startangle=90, colors=colors,
    wedgeprops={'edgecolor': 'black'}
)

# Enhance label clarity with lines for distant labels
for text, wedge in zip(texts, wedges):
    text.set_fontsize(11)
    text.set_color('black')
    text.set_fontweight('bold')
    angle = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    y = np.sin(np.deg2rad(angle))
    x = np.cos(np.deg2rad(angle))
    ha = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(angle)
    ax.annotate(
        text.get_text(), xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
        horizontalalignment=ha, arrowprops=dict(arrowstyle="-", connectionstyle=connectionstyle)
    )
    text.set_text('')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')
    autotext.set_fontsize(10)

# Add a dynamic title with multiline for clarity
plt.title(
    "Global Influence of Traditional Music Genres\nAcross Continents\nand Highlighted Trends",
    fontsize=16, fontweight='bold', loc='center', pad=20
)

# Enhanced legend with symbols and descriptors
legend_elements = [mpatches.Patch(facecolor=color, edgecolor='black', label=genre) for color, genre in zip(colors, genres)]
plt.legend(
    handles=legend_elements, title="Music Genres", loc="center left",
    bbox_to_anchor=(1, 0.5), fontsize=11
)

# Annotation for extra context
plt.annotate(
    "Cultural influence spans genres\nClassical and Blues highlighted",
    xy=(-1.2, 1.2), xycoords='data', fontsize=10,
    bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='none')
)

# Add a secondary bar plot to show historical trends for each genre
historical_data = {
    'Classical': [30, 32, 35],
    'Folk': [20, 22, 25],
    'Jazz': [15, 18, 20],
    'Blues': [8, 9, 10],
    'Reggae': [8, 9, 10]
}
years = [2020, 2021, 2022]

# Position secondary plot
ax2 = fig.add_axes([0.7, 0.05, 0.25, 0.35])
for genre, data in historical_data.items():
    ax2.plot(years, data, marker='o', label=genre)

ax2.set_title("Historical Influence Trends", fontsize=10)
ax2.set_xlabel("Year", fontsize=9)
ax2.set_ylabel("Influence Index", fontsize=9)
ax2.legend(fontsize=8)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()