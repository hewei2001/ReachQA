import matplotlib.pyplot as plt

# Data for the pie chart
commodities = [
    'Food Supplies', 
    'Technological Equipment', 
    'Raw Minerals', 
    'Pharmaceuticals', 
    'Entertainment & Cultural Goods'
]
proportions = [30, 25, 20, 15, 10]

# Colors for each commodity
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Exploding the largest slice for emphasis
explode = (0.1, 0, 0, 0, 0)

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    proportions, 
    labels=commodities, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=explode,
    shadow=True, 
    textprops=dict(color="black", fontsize=10),
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Title with a futuristic theme, broken into two lines for clarity
plt.title('Galactic Trading Hub: Commodity Distribution\non Planetary Outposts', fontsize=14, fontweight='bold', pad=20)

# Adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()