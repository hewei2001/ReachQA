import matplotlib.pyplot as plt

# Data Setup: Time allocation in hours per week
activities = ['Coursework', 'Research', 'Self-care', 'Social', 'Sleep', 'Misc']
hours = [30, 25, 15, 10, 56, 32]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0', '#FFB3E6']

# Slightly explode the 'Sleep' slice to highlight its proportion
explode = (0, 0, 0, 0, 0.1, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    hours, labels=activities, colors=colors, autopct='%1.1f%%', startangle=90,
    pctdistance=0.85, explode=explode, textprops={'fontsize': 10, 'weight': 'bold'}
)

# Format the text on the wedges
for autotext in autotexts:
    autotext.set_color('white')

# Draw a circle at the center to give it a doughnut-like appearance
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Ensures that pie chart is drawn as a circle
ax.axis('equal')

# Set the title and break it into two lines for readability
plt.title('Weekly Time Allocation of\nGraduate Students', pad=20, fontsize=14, color='navy', weight='bold')

# Add a legend with the activity descriptions
plt.legend(wedges, activities, title="Activities", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the pie chart
plt.show()