import matplotlib.pyplot as plt

# Data for the ring chart
subjects = ['Mathematics', 'Science', 'Literature', 'History', 'Art', 'Physical Education', 'Technology']
study_hours = [8, 6, 7, 3, 5, 4, 7]

# Colors for each segment of the ring chart
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', '#FF6347', '#7FFF00']

# Create the ring chart
fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(
    study_hours, labels=subjects, colors=colors, startangle=140, counterclock=False,
    autopct='%1.1f%%', pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w')
)

# Style the percentage labels
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Adding a circle at the center to convert the pie chart into a ring chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Title and central label
plt.title('Study Time Distribution Among High School Students', fontsize=16, pad=20)
plt.text(0, 0, 'Weekly Study\nHours', horizontalalignment='center', verticalalignment='center', fontsize=14, weight='bold')

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()