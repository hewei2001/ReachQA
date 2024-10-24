import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Define the activities and their usage percentages
activities = [
    'Social Media', 
    'Streaming\n(Video/Music)', 
    'Online Shopping', 
    'News Consumption', 
    'Remote Work\n/Meetings', 
    'Online Gaming', 
    'Other Activities'
]
percentages = [30, 25, 15, 10, 10, 5, 5]

# Define colors with a gradient effect for each section
colors = [
    '#FF6384', '#FF85A0',
    '#36A2EB', '#5EB7F2',
    '#FFCE56', '#FFD780',
    '#4BC0C0', '#71D7D7',
    '#9966FF', '#B78EFF',
    '#FF9F40', '#FFB870',
    '#C9CBCF', '#D4D6DC'
]

# Explode the largest sections
explode = [0.1, 0.1, 0, 0, 0, 0, 0]

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    percentages, 
    labels=activities, 
    autopct='%1.1f%%', 
    startangle=140, 
    explode=explode,
    colors=colors[::2],  # Select every alternate color for gradients
    wedgeprops=dict(width=0.3, edgecolor='w', linewidth=2),
    pctdistance=0.85
)

# Add a central circle to create a donut shape
centre_circle = plt.Circle((0, 0), 0.70, fc='white', linewidth=0.5, edgecolor='gray')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that the pie is drawn as a circle
ax.axis('equal')

# Adjust the text size
plt.setp(autotexts, size=10, weight="bold")
plt.setp(texts, size=9)

# Title of the chart
plt.title(
    'Global Internet Usage by Activity Type (2023)\nAn Analysis of Digital Engagement Patterns', 
    fontsize=14, fontweight='bold', pad=30
)

# Add a legend
legend_labels = [f"{activity}" for activity in activities]
legend_patches = [mpatches.Patch(color=color, label=label) for color, label in zip(colors[::2], legend_labels)]
ax.legend(
    handles=legend_patches, 
    title="Activities", 
    loc="center left", 
    bbox_to_anchor=(1, 0, 0.5, 1),
    title_fontsize='13'
)

# Enhance the plot's layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()