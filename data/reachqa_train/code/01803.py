import matplotlib.pyplot as plt

# Define the types of tech gadgets and their popularity percentages
gadgets = ['Smartphones', 'Wearables', 'Drones', 'Smart Home Devices', 'Laptops', 'Gaming Consoles']
popularity_percentages = [35, 20, 10, 15, 12, 8]

# Define colors for each gadget category
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFD433', '#C733FF']

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    popularity_percentages,
    labels=gadgets,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=(0.1, 0, 0, 0, 0, 0),
    shadow=True,
    wedgeprops=dict(edgecolor='w')
)

# Enhance text properties for better readability
plt.setp(autotexts, size=10, weight="bold", color='white')
plt.setp(texts, size=11)

# Chart title with a line break for clarity
ax.set_title("Tech Gadgets Buzz of 2023:\nUnveiling Consumer Favorites",
             fontsize=16, fontweight='bold', pad=20)

# Add a legend outside the pie chart for better clarity
ax.legend(wedges, gadgets, title="Gadgets", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout for better fit and readability
plt.tight_layout()

# Display the chart
plt.show()