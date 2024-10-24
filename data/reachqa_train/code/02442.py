import matplotlib.pyplot as plt

# Define the thematic areas and corresponding percentage of presentations
topics = ['AI & ML', 'IoT', 'Blockchain & Crypto', 'Quantum Computing', 
          'Renewable Energy', 'Space Exploration']
percentages = [30, 20, 15, 10, 15, 10]

# Define colors for each sector
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#DA70D6']

# Explode to highlight the most covered topic
explode = (0.1, 0, 0, 0, 0, 0)  # Explode the first slice (AI & ML)

# Create the pie chart
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(percentages, labels=topics, colors=colors, explode=explode, 
                                   autopct='%1.1f%%', startangle=140, pctdistance=0.85, 
                                   wedgeprops=dict(width=0.3, edgecolor='w'))

# Improve the autotexts style for better readability
for text in autotexts:
    text.set_color('black')
    text.set_fontsize(10)

# Create the center circle for the 'donut' shape
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Add title, breaking it into multiple lines for clarity
plt.title('Distribution of Presentations at FutureTech Summit 2023\n'
          'Exploring Emerging Technologies & Innovations', 
          fontsize=14, fontweight='bold', pad=20)

# Draw the pie chart as a circle
plt.axis('equal')  

# Ensure the layout is optimized for readability
plt.tight_layout()

# Show the plot
plt.show()