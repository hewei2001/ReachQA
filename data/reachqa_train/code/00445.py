import matplotlib.pyplot as plt

# Define activities and time spent in hours
activities = ['Research', 'Maintenance', 'Communication', 'Exercise', 'Leisure', 'Sleep']
hours = [6, 4, 2, 2, 3, 7]

# Define distinct colors for each activity
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#FF6666']

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Plot a pie chart with donut shape
wedges, texts, autotexts = ax.pie(
    hours,
    labels=activities,
    autopct='%1.1f%%',
    startangle=140,  # Rotate for better alignment
    colors=colors,
    wedgeprops=dict(width=0.4),  # Create donut by adjusting width
    pctdistance=0.85,  # Position percentage labels inside the donut
    explode=(0.05, 0.05, 0.1, 0.05, 0.05, 0.1),  # Highlight Communication and Sleep
    shadow=True  # Add shadow for depth
)

# Draw a circle in the middle for the donut appearance
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)

# Set equal aspect ratio to ensure the chart is a circle
ax.axis('equal')

# Set title and customize it to improve readability
ax.set_title("Time Allocation in a Day of a Space Explorer\n(Aboard the International Space Colony)", 
             fontsize=14, fontweight='bold', color='navy')

# Customize the text appearance
plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=11)

# Add a legend outside the chart for clear identification
ax.legend(wedges, activities, title="Activities", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()