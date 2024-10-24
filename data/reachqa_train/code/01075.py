import matplotlib.pyplot as plt

# Data for the chart
categories = ['Smartphones', 'Laptops', 'Tablets', 'Wearables', 'Smart Home Devices']
market_share = [40, 25, 15, 10, 10]

# Colors for each category
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Explode the first slice to highlight Smartphones
explode = (0.1, 0, 0, 0, 0)  # Only explode the 1st slice

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(market_share, labels=categories, autopct='%1.1f%%', startangle=140,
                                  colors=colors, explode=explode, textprops=dict(color="black", fontsize=12))

# Customize the display of percentage text inside the pie chart
plt.setp(autotexts, size=10, weight="bold")

# Set the title and break it into two lines for better readability
ax.set_title("Global Technology Gadget\nMarket Share by Product Category 2023", fontsize=16, fontweight='bold')

# Add a legend
ax.legend(wedges, categories, title="Gadget Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Ensure equal aspect ratio so pie is drawn as a circle.
ax.axis('equal')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()