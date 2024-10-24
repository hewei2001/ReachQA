import matplotlib.pyplot as plt

# Data for the chart
destinations = ["Moon", "Mars", "Venus", "Europa", "Saturn's Rings"]
market_share = [40, 25, 10, 15, 10]  # Market share percentages

# Colors for each pie sector
colors = ['#ffcc00', '#ff5733', '#33ff57', '#339fff', '#9b59b6']

# Explode configuration to emphasize the 'Moon' sector
explode = (0.1, 0, 0, 0, 0)  # 'Moon' will be slightly separated from the pie

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    market_share,
    labels=destinations,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

# Title and styling adjustments
ax.set_title(
    "The Rise of Space Tourism:\nMarket Share of Top Destinations in the Solar System",
    fontsize=16, fontweight='bold', pad=20
)
plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=12)

# Ensuring the pie chart is a circle
ax.axis('equal')

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()