import matplotlib.pyplot as plt

# Define activities and their corresponding time allocation in a tech startup
activities = ['Product Dev.', 'Marketing', 'Sales', 'Cust. Support', 'Admin']
time_allocation = [35, 20, 15, 15, 15]

# Choose a distinct color palette for each activity
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']

# Create the ring chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    time_allocation, 
    labels=activities, 
    colors=colors, 
    autopct='%1.1f%%',
    startangle=90, 
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Draw a circle at the center to turn the pie chart into a ring chart
center_circle = plt.Circle((0,0), 0.70, fc='white')
fig.gca().add_artist(center_circle)

# Add title and adjust text properties for better readability
plt.title('Time Allocation in a Tech Startup\n(Percentage of Total Working Hours)', fontsize=16, weight='bold')
plt.setp(texts, size=10, weight='bold')
plt.setp(autotexts, size=9, weight='bold', color='black')

# Ensure the chart is a perfect circle
ax.axis('equal')  

# Adding legend outside of the plot
plt.legend(wedges, activities, title="Activities", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout for better fit
plt.tight_layout()

# Show the final ring chart
plt.show()