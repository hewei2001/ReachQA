import matplotlib.pyplot as plt

# Data on culinary preferences in Tasteopia
cuisines = ['Italian', 'Chinese', 'Mexican', 'Indian', 'Japanese', 'French', 'Other']
popularity_percentages = [30, 20, 15, 12, 10, 8, 5]

# Colors for each cuisine
colors = ['#FF9999', '#FFCC99', '#99FF99', '#66B3FF', '#FFB6C1', '#C2C2F0', '#FFDB4D']

# Create the pie chart
plt.figure(figsize=(10, 8))
plt.pie(popularity_percentages, labels=cuisines, autopct='%1.1f%%', startangle=140,
        colors=colors, explode=[0.1, 0, 0, 0, 0, 0, 0], shadow=True)

# Add a creative title, splitting it for readability
plt.title('Culinary Preferences in Tasteopia:\nA Survey of Global Cuisines', fontsize=16, fontweight='bold', pad=20)

# Position the legend outside the pie chart
plt.legend(cuisines, title="Cuisines", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()