import matplotlib.pyplot as plt

# Define expanded activities and their corresponding participation counts with decimals
activities = [
    'Tree Planting', 'Recycling Workshops', 'Clean-Up Drives', 
    'Educational Seminars', 'Solar Panel Installation', 
    'Bike-to-Work Days', 'Sustainability Talks'
]
participation_counts = [300.5, 450.25, 200.75, 150.5, 120.25, 180.3, 250.15]

# Define colors for the activities
colors = ['#4caf50', '#ffeb3b', '#2196f3', '#f44336', '#ff9800', '#8bc34a', '#03a9f4']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the ring chart
wedges, texts, autotexts = ax.pie(participation_counts, labels=activities, autopct='%1.1f%%', startangle=140,
                                  colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w'))

# Set title with a multi-line break
ax.set_title('Community Engagement Activities\nDetailed Overview of Sustainability Month', fontsize=16, fontweight='bold')

# Customize text properties to avoid overlap
for text in texts:
    text.set_fontsize(9)
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('navy')

# Draw center circle to create ring effect
centre_circle = plt.Circle((0, 0), 0.55, fc='white')
fig.gca().add_artist(centre_circle)

# Ensure the pie chart is a circle
ax.axis('equal')

# Add central label inside the ring with dynamic total calculation
total_participation = sum(participation_counts)
central_label = plt.text(0, 0, f'Total\nParticipation\n{total_participation:.2f}', 
                         fontsize=12, va='center', ha='center', fontweight='bold')

# Add legend with adjusted position
ax.legend(wedges, activities, title="Activities", loc='center left', bbox_to_anchor=(1, 0.5))

# Create a secondary plot (subplot) for hierarchical data visualization (optional sunburst)
# Example hierarchical data: Monthly breakdown (fictional data)
monthly_data = [
    ['Tree Planting', 'January', 'February', 'March'],
    ['Recycling Workshops', 'January', 'February', 'March'],
    ['Clean-Up Drives', 'January', 'February', 'March'],
    ['Educational Seminars', 'January', 'February', 'March'],
    ['Solar Panel Installation', 'January', 'February', 'March'],
    ['Bike-to-Work Days', 'January', 'February', 'March'],
    ['Sustainability Talks', 'January', 'February', 'March']
]
monthly_participation = [
    [100, 120, 80], [150, 160, 140], [70, 60, 70], 
    [50, 60, 40], [40, 50, 30], [60, 70, 50], [80, 90, 80]
]

# (Optional) More complex visualization can be constructed separately if needed

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()