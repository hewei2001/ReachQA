import matplotlib.pyplot as plt

# Define the data
activities = ['Social Media', 'Streaming Services', 'Online Gaming', 'E-learning', 'E-commerce']
time_spent = [12, 10, 8, 6, 4]

# Define colors for each activity
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6666']

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    time_spent, 
    labels=activities, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140, 
    pctdistance=0.85, 
    wedgeprops=dict(width=0.3, edgecolor='w'),
    explode=(0.05, 0.05, 0.05, 0.05, 0.05),
    shadow=True
)

# Draw circle for the donut shape
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Set the title with a line break for better readability
ax.set_title('Digital Time Allocation in TechHaven:\nInsights from a 2023 Survey', fontsize=14, fontweight='bold')

# Adjust text properties for better readability
plt.setp(autotexts, size=10, weight="bold", color="black")
plt.setp(texts, size=10)

# Equal aspect ratio ensures that pie chart is drawn as a circle
ax.axis('equal')

# Add a legend outside the plot area
ax.legend(wedges, activities, title="Activities", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()