import matplotlib.pyplot as plt
import numpy as np

# Subjects and percentage of student preferences
subjects = ['Mathematics', 'Science', 'Literature', 'History', 'Art', 'Physical Education', 'Music']
student_preferences = [22, 18, 15, 10, 13, 12, 10]

# Color scheme for the sectors
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF9966', '#C49CFF', '#FFA07A']

# Emphasize 'Mathematics' sector for example
explode = (0.1, 0, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    student_preferences, 
    labels=subjects, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140, 
    explode=explode
)

# Customize the chart with title and label adjustments
plt.title("Distribution of Favorite Learning Subjects\nAmong Middle School Students", fontsize=16, weight='bold')
plt.setp(texts, size=10, weight='bold')
plt.setp(autotexts, size=10, weight='bold', color='black')

# Draw a circle at the center of pie to make it look like a donut
center_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(center_circle)

# Ensure the pie chart is perfectly circular
ax.axis('equal')

# Position the legend outside the pie chart to avoid overlap
plt.legend(wedges, subjects, title="Subjects", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Automatically adjust subplot params for better layout
plt.tight_layout()

# Display the chart
plt.show()