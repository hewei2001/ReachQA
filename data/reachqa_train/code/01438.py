import matplotlib.pyplot as plt
import numpy as np

# Manuscripts data for each region
regions = ['Greece', 'Egypt', 'Rome', 'Carthage', 'Phoenicia', 'Anatolia']
manuscripts = [120, 200, 180, 80, 110, 90]

# Define gradient colors for each region using a colormap
cmap = plt.get_cmap('viridis')
colors = [cmap(i / len(manuscripts)) for i in range(len(manuscripts))]

# Determine if any sector should be highlighted
explode = (0.1, 0, 0, 0, 0, 0)  # Highlighting Greece for emphasis

# Create the pie chart
fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect='equal'))
wedges, texts, autotexts = ax.pie(manuscripts, labels=regions, autopct='%1.1f%%', startangle=140,
                                  colors=colors, explode=explode, wedgeprops=dict(edgecolor='black', linewidth=1.5))

# Enhance text style
for text in texts:
    text.set_size(11)
    text.set_fontweight('bold')
    text.set_color('navy')
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_weight('bold')

# Create an inset bar chart showing manuscript growth over time for a region
ax_inset = fig.add_axes([0.8, 0.1, 0.15, 0.3])
years = ['100 BC', '50 BC', '0 AD', '50 AD', '100 AD']
growth = [20, 45, 70, 90, 120]  # Hypothetical data for Greece
ax_inset.bar(years, growth, color='skyblue')
ax_inset.set_title('Greece Manuscripts\nOver Time', fontsize=9)
ax_inset.set_ylabel('Manuscripts', fontsize=8)
ax_inset.tick_params(axis='x', rotation=45, labelsize=8)

# Enhanced legend with additional spacing and icons (represented by wedge colors here)
plt.legend(wedges, regions, title="Regions", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9)

# Add the title with multiple lines
plt.title('Distribution of Ancient Manuscripts\nFound Around the Mediterranean Regions',
          fontsize=16, fontweight='bold', pad=20)

# Adjust layout to fit everything neatly
plt.tight_layout()

# Show plot
plt.show()