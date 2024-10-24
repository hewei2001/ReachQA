import matplotlib.pyplot as plt

# Data for the pie chart
regions = ['Europe', 'Asia', 'North America', 'South America', 'Africa', 'Oceania']
capacity_percentage = [30, 28, 25, 10, 5, 2]

# Colors for each region
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Exploding the largest sectors for emphasis
explode = (0.1, 0, 0.05, 0, 0, 0)

# Creating the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(capacity_percentage, labels=regions, autopct='%1.1f%%',
                                  startangle=140, colors=colors, explode=explode, pctdistance=0.85)

# Formatting for text inside and outside the pie chart
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

# Draw a circle at the center to make it look like a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Aspect ratio to ensure pie is drawn as a circle
ax.axis('equal')  

# Add title
plt.title('Global Renewable Energy Capacity\nby Region in 2023', fontsize=16, fontweight='bold', pad=20)

# Add a legend
ax.legend(wedges, regions, title="Regions", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

# Adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()