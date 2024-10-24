import matplotlib.pyplot as plt

# Data representing the sustainability practices in Greentown
practices = ['Recycling', 'Composting', 'Energy-saving', 'Water Conservation', 'Public Transportation']
percentages = [30, 25, 20, 15, 10]
colors = ['#76C7C0', '#FFD700', '#FF6F61', '#6B8E23', '#4682B4']

# Plotting the donut pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    percentages,
    colors=colors,
    startangle=90,
    labels=practices,
    autopct='%1.1f%%',
    pctdistance=0.75,
    wedgeprops=dict(width=0.3),
    shadow=True,
    explode=(0.05, 0.05, 0.05, 0.05, 0.05)
)

# Adding a circle in the middle to create a donut shape
centre_circle = plt.Circle((0, 0), 0.55, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures the pie is drawn as a circle
ax.axis('equal')

# Title and legend
plt.title('Distribution of Sustainability Practices\nin Greentown', size=16, color='green', loc='center', pad=30)
plt.legend(wedges, practices, title='Practices', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Customizing the autotext labels
for autotext in autotexts:
    autotext.set_color('darkblue')
    autotext.set_weight('bold')

# Automatically adjust the layout to prevent clipping of text
plt.tight_layout()

# Display the chart
plt.show()