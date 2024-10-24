import matplotlib.pyplot as plt

# Data for the pie chart
categories = ['Streaming Services', 'Social Media', 'E-commerce', 'Educational Platforms', 'Online Gaming']
traffic_share = [30, 25, 20, 15, 10]

# Colors for each category
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']

# Explode the 'Streaming Services' sector to highlight it
explode = (0.1, 0, 0, 0, 0)  

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(traffic_share, labels=categories, colors=colors, autopct='%1.1f%%', startangle=90, 
       explode=explode, wedgeprops=dict(edgecolor='w'), textprops={'fontsize': 10}, pctdistance=0.85)

# Draw a circle to create a donut chart effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Title
ax.set_title('Distribution of Internet Traffic in Cyberia (2023)\nInsights into Changing Online Behavior', 
             fontsize=14, fontweight='bold', pad=20)

# Aspect ratio
ax.axis('equal')  

# Legend
plt.legend(categories, title='Platforms', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()