import matplotlib.pyplot as plt

# Data for the pie chart
countries = ['United States', 'European Union', 'China', 'Japan', 'Australia', 'Canada', 'Others']
contributions = [25, 20, 18, 15, 10, 7, 5]

# Colors for each section of the pie chart
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Creating the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    contributions, 
    labels=countries, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=(0.1, 0, 0, 0, 0, 0, 0),  # Exploding the largest contribution slice
    shadow=True,
    textprops=dict(color="white", fontsize=10, weight="bold")
)

# Customizing the plot
ax.set_title(
    "Global Contributions to Ocean Exploration Missions\n(2023)", 
    fontsize=16, 
    fontweight='bold', 
    color='#333'
)

# Annotating the largest contributor
ax.annotate(
    'Leading Contributor',
    xy=(0.9, 0.3),
    xytext=(1.5, 0.5),
    arrowprops=dict(facecolor='black', arrowstyle='->'),
    fontsize=10,
    fontweight='bold',
    color='black'
)

# Adding a legend
ax.legend(
    wedges, 
    countries, 
    title="Countries/Regions", 
    loc="center left", 
    bbox_to_anchor=(1, 0, 0.5, 1), 
    fontsize=9
)

# Adjusting layout to avoid overlap
plt.tight_layout()

# Displaying the plot
plt.show()