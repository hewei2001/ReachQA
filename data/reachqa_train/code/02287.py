import matplotlib.pyplot as plt

# Define streaming platforms and their market shares
platforms = ['Netflix', 'Amazon Prime', 'Disney+', 'HBO Max', 'Apple TV+', 'StreamX']
market_shares = [30, 25, 20, 10, 8, 7]

# Define colors for each platform
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0', '#FFB3E6']

# Explode the 'Netflix' slice to emphasize it
explode = (0.1, 0, 0, 0, 0, 0)

# Create the pie chart
plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(market_shares, explode=explode, labels=platforms, colors=colors,
                                   autopct='%1.1f%%', startangle=140, shadow=True)

# Customize the pie chart
plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=12, weight='bold')

# Draw a circle in the center of the pie chart to create a donut chart effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Add a title, breaking it into two lines
plt.title('Online Streaming Platform Market Share\nin 2023', fontsize=16, weight='bold', pad=20)

# Position the legend to the right of the chart
plt.legend(wedges, platforms, title="Platforms", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust the layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()