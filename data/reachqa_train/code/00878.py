import matplotlib.pyplot as plt

# Define transportation modes and their projected shares in urban transit by 2035
modes = ['Public Transit', 'Ride Sharing', 'Biking', 'Electric Scooters', 'Hyperloop', 'Flying Taxis', 'Walking']
percentages = [25, 20, 15, 10, 15, 10, 5]

# Define colors for each sector
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#FF6F61', '#8B008B']

# Highlight a particular sector for emphasis
explode = (0, 0, 0, 0, 0.1, 0, 0)  # Emphasize Hyperloop

# Create a pie chart
plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(
    percentages, labels=modes, colors=colors, explode=explode,
    autopct='%1.1f%%', startangle=140, pctdistance=0.85
)

# Customize text for readability
for text in texts:
    text.set_fontsize(11)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Draw a circle at the center of the pie to give a donut-like appearance
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Set the aspect ratio to be equal so the pie is circular
plt.axis('equal')

# Add a title with line breaks for readability
plt.title('The Future of Urban Transportation:\nMode Distribution in 2035', fontsize=14, fontweight='bold', ha='center')

# Place the legend outside the pie chart
plt.legend(wedges, modes, title="Transportation Modes", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the pie chart
plt.show()