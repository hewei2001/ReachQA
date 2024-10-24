import matplotlib.pyplot as plt

# Define the subjects and their corresponding study hours
subjects = ['Mathematics', 'Science', 'English', 'History', 'Art', 'Physical Ed.']
study_hours = [12, 10, 8, 6, 4, 2]

# Colors for each subject, aiming for a diverse and attractive palette
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Create a ring chart
wedges, texts, autotexts = ax.pie(
    study_hours, labels=subjects, autopct='%1.1f%%', startangle=140,
    colors=colors, wedgeprops=dict(width=0.4, edgecolor='w'), pctdistance=0.85,
    textprops={'fontsize': 10, 'weight': 'bold'}
)

# Set title and center text
plt.title("Study Time Distribution\nAmong Subjects for Greenfield Academy Students",
          fontsize=14, fontweight='bold', pad=20)

# Enhance label appearance
for text in texts:
    text.set_horizontalalignment('center')

# Adjust autotexts to be more visible against the colored wedges
for autotext in autotexts:
    autotext.set_color('white')

# Add a legend with a title
ax.legend(wedges, subjects, title="Subjects", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Draw a central circle to highlight the donut shape
centre_circle = plt.Circle((0, 0), 0.7, fc='white')
fig.gca().add_artist(centre_circle)

# Ensure layout is optimal
plt.tight_layout()

# Display the ring chart
plt.show()