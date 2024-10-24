import matplotlib.pyplot as plt

# Define the activity data
activities = ['Work', 'Sleep', 'Leisure', 'Commute', 'Exercise', 'Other']
time_spent = [35, 30, 15, 10, 5, 5]  # Percentage of time

# Define colors for the pie sections
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Define an explode value to highlight 'Leisure'
explode = (0.05, 0, 0.1, 0, 0, 0)  # 'Work' and 'Leisure' sections are slightly exploded

# Create the pie chart
plt.figure(figsize=(10, 7))
plt.pie(
    time_spent, 
    explode=explode, 
    labels=activities, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140, 
    pctdistance=0.85, 
    shadow=True
)

# Draw a circle in the center to make it a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.title(
    "Time Allocation in Pleasantville:\nA Typical Weekday", 
    fontsize=16, 
    fontweight='bold', 
    pad=20
)

# Add legend
plt.legend(
    activities, 
    loc='lower left', 
    title="Activities", 
    fontsize=10, 
    bbox_to_anchor=(1, 0.5)
)

# Adjust layout for better display
plt.tight_layout()

# Show the plot
plt.show()