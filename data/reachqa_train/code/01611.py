import matplotlib.pyplot as plt
import numpy as np

# Extended data for caffeine consumption preferences with nested subcategories
caffeine_sources = [
    'Coffee', 'Tea', 'Energy Drinks', 'Soda', 'Decaf Coffee',
    'Green Tea', 'Herbal Tea', 'Sports Drinks', 'Chocolate', 'Supplements'
]
percentages = [30, 15, 10, 8, 7, 10, 5, 6, 5, 4]

# Choose distinct colors for each category
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700',
          '#8B80F9', '#F97B6D', '#FCB9C8', '#ACFFAD', '#B7C3F3']

# Highlight the largest segment - Coffee
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    percentages, labels=caffeine_sources, autopct='%1.1f%%',
    startangle=90, colors=colors, explode=explode, shadow=True, pctdistance=0.85
)

# Make sure that each label and percentage is properly displayed
for text in texts:
    text.set_size(9)
for autotext in autotexts:
    autotext.set_size(9)
    autotext.set_color('darkgrey')

# Draw a circle in the center to transform it into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Add a title with multiple lines for better readability
plt.title("Caffeine Consumption Preferences\nAcross Different Beverage Types in 2023", fontsize=16, weight='bold', pad=20)

# Add a legend with a title
plt.legend(title='Beverage Types', loc='upper left', bbox_to_anchor=(1, 0.5), fontsize=10, frameon=False)

# Automatically adjust the layout to prevent overlaps
plt.tight_layout()

# Display the plot
plt.show()