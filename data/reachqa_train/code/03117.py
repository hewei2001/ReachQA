import matplotlib.pyplot as plt

# Coffee types and their global popularity percentages
coffee_types = ['Espresso', 'Cappuccino', 'Latte', 'Americano', 'Mocha', 'Macchiato']
popularity_percentages = [30, 25, 20, 10, 8, 7]

# Colors for each coffee type slice
colors = ['#6F4E37', '#D2691E', '#8B4513', '#A0522D', '#CD853F', '#8B0000']

# Explode settings to highlight the Espresso section slightly
explode = (0.1, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    popularity_percentages,
    labels=coffee_types,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    shadow=True,
    wedgeprops=dict(edgecolor='w')
)

# Customize the autotexts for better readability
plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=12)

# Set the title of the chart
ax.set_title(
    'Global Popularity of Coffee Types',
    fontsize=16,
    fontweight='bold',
    pad=20
)

# Position the legend
ax.legend(
    wedges,
    coffee_types,
    title="Coffee Types",
    loc="upper right",
    bbox_to_anchor=(1.2, 0.8),
    fontsize=10
)

# Ensure the pie is drawn as a circle
ax.set_aspect('equal')

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()