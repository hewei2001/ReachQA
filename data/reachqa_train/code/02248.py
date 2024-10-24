import matplotlib.pyplot as plt
import numpy as np

# Define the activities and the hours allocated to each
activities = ['Work', 'Meetings', 'Exercise', 'Meals', 'Family Time', 'Leisure', 'Sleep']
hours = np.array([8, 2, 1, 2, 3, 3, 5])

# Define colors for each activity
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7']

# Create the pie chart
fig, ax = plt.subplots(figsize=(9, 9))

# Plot pie chart with exploded slices for better emphasis
explode = [0.1 if activity == 'Work' else 0.05 for activity in activities]  # Highlight 'Work' more prominently
wedges, texts, autotexts = ax.pie(hours, labels=activities, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)

# Customize text properties
plt.setp(texts, size=12, fontweight='semibold')
plt.setp(autotexts, size=10, color='white')

# Ensure the pie is a perfect circle
ax.set_aspect('equal')

# Set the title of the plot
plt.title("Balancing Act:\nA Day in the Life of a Remote Worker", fontsize=16, fontweight='bold', y=1.05)

# Add a legend with detailed description
ax.legend(wedges, activities, title="Activities", loc="upper right", bbox_to_anchor=(1.3, 0.9))

# Adjust layout for better fit and visibility
plt.tight_layout()

# Display the plot
plt.show()