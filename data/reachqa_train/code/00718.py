import matplotlib.pyplot as plt
import numpy as np

# Define the categories and their respective market share percentages
beverage_categories = ['Coffee', 'Tea', 'Soft Drinks', 'Energy Drinks', 'Bottled Water', 'Juices', 'Alcoholic Beverages']
market_shares = [25, 20, 15, 10, 15, 5, 10]

# Define colors and patterns for each category
colors = ['#6B4226', '#C5A880', '#FF9999', '#FFCC99', '#66B3FF', '#99FF99', '#FF6666']
patterns = ['/', '\\', '|', '-', '+', 'x', 'o']

# Explode the 'Coffee' slice for emphasis
explode = (0.1, 0, 0, 0, 0, 0, 0)

# Creating a donut chart with an inner circle
plt.figure(figsize=(12, 8))
wedges, texts, autotexts = plt.pie(market_shares, labels=beverage_categories, autopct='%1.1f%%', startangle=140, 
                                   colors=colors, explode=explode, shadow=True, wedgeprops=dict(width=0.3))

# Apply patterns to each wedge
for i, wedge in enumerate(wedges):
    wedge.set_hatch(patterns[i])

# Add annotations
for i, (text, autotext) in enumerate(zip(texts, autotexts)):
    autotext.set_text(f'{autotext.get_text()}\n({market_shares[i]}%)')
    text.set_color('black')
    autotext.set_color('white')

# Title and layout adjustments
plt.title('Beverage Consumption Preferences Worldwide\n2023 Analysis', fontsize=16, fontweight='bold', pad=20)
plt.axis('equal')  # Ensure the donut chart is circular
plt.legend(wedges, beverage_categories, title="Beverage Categories", loc='center left', bbox_to_anchor=(1.0, 0.5))

# Inner circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
plt.gca().add_artist(centre_circle)

# Add source citation
plt.text(-2, -1.1, 'Source: Global Beverage Market Study 2023', fontsize=9, color='gray')

# Automatically adjust layout to accommodate elements
plt.tight_layout()

# Display the plot
plt.show()