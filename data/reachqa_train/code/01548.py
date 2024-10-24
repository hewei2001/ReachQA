import matplotlib.pyplot as plt

# Data for conservation efforts
efforts = [30, 20, 15, 25, 10]
categories = ['Habitat Preservation', 'Anti-Poaching', 'Captive Breeding', 'Legal Protection', 'Public Awareness']

# Colors for each category
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(9, 9), dpi=100)
wedges, texts, autotexts = ax.pie(efforts, labels=categories, autopct='%1.1f%%', startangle=90, 
                                  colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w'), 
                                  explode=[0.05, 0, 0, 0, 0])

# Enhance text and shadow
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
ax.add_artist(plt.Circle((0, 0), 0.7, fc='white', edgecolor='lightgray'))

# Add title and legend
plt.title('Global Efforts for\nAnimal Conservation in 2023', fontsize=16, fontweight='bold', pad=20)
ax.legend(wedges, categories, title="Conservation Strategies", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()