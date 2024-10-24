import matplotlib.pyplot as plt

# Time allocation for activities in minutes
activities = ['Meetings', 'Desk Work', 'Breaks', 'Emails', 'Commuting']
time_spent = [90, 210, 60, 60, 60]  # 480 minutes total

# Define colors for each activity
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create a donut pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    time_spent, 
    labels=activities, 
    autopct='%1.1f%%', 
    startangle=140, 
    pctdistance=0.85, 
    colors=colors, 
    wedgeprops={'width': 0.3, 'edgecolor': 'black'},
    textprops=dict(color="black", fontsize=10, weight='bold')
)

# Enhance the appearance of percentages
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')

# Add a circle at the center to turn the pie into a donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Add title and adjust layout
plt.title('A Day in the Life of an Office Worker:\nTime Allocation (8-hour Workday)', fontsize=14, fontweight='bold', pad=20)

# Ensure the pie chart is a perfect circle
ax.axis('equal')

# Add a legend to the right side of the chart
ax.legend(wedges, activities, title="Activities", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Adjust layout to fit everything nicely
plt.tight_layout()

# Display the chart
plt.show()