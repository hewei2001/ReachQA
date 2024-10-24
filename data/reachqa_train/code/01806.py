import matplotlib.pyplot as plt

# Define the cuisine categories and their popularity percentages
cuisines = ['Martian Desserts', 'Venusian Beverages', 'Jovian Sandwiches', 'Saturnian Salads', 'Neptunian Noodles']
popularity = [25, 15, 20, 10, 30]

# Colors for each cuisine category
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']

# Explode the largest category (Neptunian Noodles) for emphasis
explode = (0, 0, 0, 0, 0.1)

# Create the pie chart
plt.figure(figsize=(10, 7))
plt.pie(popularity, labels=cuisines, autopct='%1.1f%%', startangle=140, colors=colors, 
        explode=explode, shadow=True, wedgeprops=dict(edgecolor='w'))

# Title and layout
plt.title('Galactic Cuisine:\nA Tasting Tour Across the Universe', fontsize=16, weight='bold', pad=20)
plt.axis('equal')  # Ensures the pie chart is a circle
plt.legend(cuisines, title="Cuisines", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()