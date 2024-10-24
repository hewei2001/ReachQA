import matplotlib.pyplot as plt

# Define the activities and their corresponding participation counts
activities = ['Tree Planting', 'Recycling Workshops', 'Clean-Up Drives', 'Educational Seminars']
participation_counts = [300, 450, 200, 150]

# Define colors for the activities
colors = ['#4caf50', '#ffeb3b', '#2196f3', '#f44336']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the ring chart
wedges, texts, autotexts = ax.pie(participation_counts, labels=activities, autopct='%1.1f%%', startangle=140,
                                  colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w'))

# Set title
ax.set_title('Community Engagement Activities\nSustainability Month Overview', fontsize=14, fontweight='bold')

# Customize text properties
for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('navy')

# Draw center circle to create ring effect
centre_circle = plt.Circle((0, 0), 0.55, fc='white')
fig.gca().add_artist(centre_circle)

# Ensure the pie chart is a circle
ax.axis('equal')

# Add central label inside the ring
central_label = plt.text(0, 0, 'Total\nParticipation\n1100', fontsize=12, va='center', ha='center', fontweight='bold')

# Add legend with adjusted position
ax.legend(wedges, activities, title="Activities", loc='center left', bbox_to_anchor=(1, 0.3, 0.5, 1))

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()