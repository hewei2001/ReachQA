import matplotlib.pyplot as plt
import squarify

# Define the engineering disciplines and their respective student numbers
disciplines = [
    "Mechanical Engineering", "Electrical Engineering", "Civil Engineering",
    "Computer Science", "Chemical Engineering", "Aerospace Engineering",
    "Biomedical Engineering", "Industrial Engineering", "Environmental Engineering",
    "Robotics Engineering"
]

students = [600, 750, 500, 900, 450, 350, 300, 400, 200, 250]

# Colors for the tree map
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0',
    '#ffb3e6', '#c4e17f', '#6b8e23', '#e6e6fa', '#ffefd5'
]

# Calculate the percentage of total students for each discipline
total_students = sum(students)
percentages = [(student / total_students) * 100 for student in students]

# Set up a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
fig.suptitle("Analysis of Engineering Disciplines at FutureTech University", fontsize=18, fontweight='bold', ha='center')

# First plot: Treemap for student distribution
squarify.plot(
    sizes=students, 
    label=[f"{disc}\n({num} students)" for disc, num in zip(disciplines, students)],
    color=colors, 
    alpha=0.8, 
    ax=ax1, 
    pad=True, 
    text_kwargs={'fontsize': 9}
)
ax1.set_title("Distribution of Students by Discipline", fontsize=14)
ax1.axis('off')

# Second plot: Bar chart for percentage distribution
ax2.barh(disciplines, percentages, color=colors, alpha=0.8)
ax2.set_xlabel("Percentage of Total Students (%)", fontsize=12)
ax2.set_title("Percentage of Total Students by Discipline", fontsize=14)
ax2.invert_yaxis()  # To keep the largest bar at the top

# Adjust layout for better fit and clarity
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plots
plt.show()