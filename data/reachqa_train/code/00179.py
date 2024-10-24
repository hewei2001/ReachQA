import matplotlib.pyplot as plt

# Data and labels for the donut pie chart
tasks = [
    'Data Cleaning', 
    'Modeling', 
    'Meetings', 
    'Research & Development', 
    'Visualization', 
    'Documentation', 
    'Personal Development'
]
hours = [10, 8, 6, 5, 4, 3, 4]

# Define colors for the segments
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ffd700']

# Plotting the donut pie chart
fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(
    hours, 
    labels=tasks, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    pctdistance=0.85, 
    wedgeprops=dict(width=0.3, edgecolor='w'),
    explode=[0.1, 0, 0, 0, 0, 0, 0]  # Highlight Data Cleaning
)

# Equal aspect ratio ensures the pie is drawn as a circle
ax.axis('equal')  

# Title and styling
plt.title("Time Allocation of a Modern Data Scientist's Week", fontsize=14, y=1.05)
plt.setp(autotexts, size=10, weight="bold", color="black")

# Add a legend with a title and positioning
ax.legend(wedges, tasks,
          title="Tasks",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()