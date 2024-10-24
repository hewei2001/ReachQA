import matplotlib.pyplot as plt

# Product categories and their corresponding market share percentages
categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Beauty & Health', 'Sports & Outdoors', 'Toys & Games', 'Books & Stationery']
market_share = [25, 20, 15, 10, 10, 10, 10]

# Colors for each segment of the ring chart
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#F4E1E1', '#B565A7']

# Create a ring chart (donut chart) using matplotlib
fig, ax = plt.subplots(figsize=(10, 7))

# Plot a pie chart and set the 'startangle' for better visualization
wedges, texts, autotexts = ax.pie(
    market_share, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140, 
    pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='white')
)

# Draw a circle at the center of the pie chart to make it a ring (donut chart)
centre_circle = plt.Circle((0, 0), 0.55, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Add a title to the chart
plt.title('E-Commerce Product Categories:\nMarket Share Insights for 2023', fontsize=15, weight='bold', pad=20)

# Beautify the plot with additional formatting
plt.setp(autotexts, size=11, weight="bold", color='black')
plt.setp(texts, size=10)

# Create a legend and place it outside the plot
ax.legend(wedges, categories, title="Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()