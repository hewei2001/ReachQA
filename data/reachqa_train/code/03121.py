import matplotlib.pyplot as plt

# Define the sectors and their corresponding funding percentages
sectors = ['Natural Language Processing', 'Computer Vision', 'Robotics', 
           'Machine Learning Algorithms', 'AI in Healthcare']
funding_percentages = [30, 25, 20, 15, 10]

# Define colors for each sector using a cohesive color palette
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the donut pie chart
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(
    funding_percentages, 
    labels=sectors, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    wedgeprops=dict(width=0.3, edgecolor='w'),  # Create the hole and add edge color for better separation
    pctdistance=0.85  # Position the percentage labels closer to the center
)

# Customize the text properties
for text in texts:
    text.set_fontsize(10)
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Title with a clear break for readability
plt.title('Distribution of Research Funding\nin AI Sectors - 2023', fontsize=16, fontweight='bold', pad=20)

# Ensure the pie chart is drawn as a circle
plt.axis('equal')

# Add a shadow for depth
plt.gca().set_facecolor('white')
plt.gca().patch.set_alpha(0.5)

# Add a legend with a shadow effect
plt.legend(wedges, sectors, title="AI Sectors", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10, frameon=True)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()