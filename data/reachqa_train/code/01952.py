import matplotlib.pyplot as plt

# Categories of futuristic technologies and their investment shares
categories = ['Artificial Intelligence', 'Quantum Computing', 'Renewable Energy', 
              'Space Exploration', 'Bioengineering']
investment_shares = [25, 15, 30, 10, 20]

# Define distinct colors for each category
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']

# Create the pie chart
plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(
    investment_shares,
    labels=categories,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=(0.1, 0, 0.1, 0, 0),
    pctdistance=0.85,
    shadow=True
)

# Customize the text properties
for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('darkblue')
    autotext.set_weight('bold')

# Draw a circle in the center of the pie chart to create a doughnut chart effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Set title and styling
plt.title('Global Investment Projections\nin Futuristic Technologies for 2050', fontsize=16, fontweight='bold')

# Place the legend outside the chart
plt.legend(wedges, categories, title="Technologies", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the pie chart
plt.show()