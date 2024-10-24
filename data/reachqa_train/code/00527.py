import matplotlib.pyplot as plt

# Mythical creatures and their market share percentages
creatures = ['Dragons', 'Elves', 'Dwarves', 'Fairies', 'Unicorns', 'Goblins', 'Mermaids']
market_share = [30, 20, 15, 10, 5, 10, 10]

# Colors for each sector
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666']

# Explode the largest sector for emphasis
explode = (0.1, 0, 0, 0, 0, 0, 0)

# Set up the figure
fig, ax = plt.subplots(figsize=(8, 8))

# Create the pie chart with styling
wedges, texts, autotexts = ax.pie(
    market_share, explode=explode, labels=creatures, colors=colors, autopct='%1.1f%%',
    startangle=140, wedgeprops=dict(edgecolor='w', linewidth=2)
)

# Customize text for visibility
for text in texts:
    text.set_fontsize(12)
    text.set_color('black')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_weight('bold')

# Title
plt.title('Market Share of Mythical Creatures\nin Fantasy Literature', fontsize=14, fontweight='bold', pad=20)

# Legend outside the chart
ax.legend(wedges, creatures, title='Creatures', loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)

# Adjust layout to ensure clarity
plt.tight_layout()

# Display the chart
plt.show()