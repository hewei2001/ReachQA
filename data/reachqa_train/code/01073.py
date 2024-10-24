import numpy as np
import matplotlib.pyplot as plt

# Define skills and students
skills = ['Knife Skills', 'Cooking Techniques', 'Plating', 'Flavor', 'Time Management']
students = ['Alice', 'Bob', 'Clara']

# Scores for each student
data = np.array([
    [8, 6, 7, 8, 7],  # Alice
    [7, 9, 8, 7, 6],  # Bob
    [9, 8, 6, 9, 8]   # Clara
])

# Number of skills
num_skills = len(skills)

# Function to create a radar chart
def create_radar_chart(title, labels, data, student_labels):
    # Calculate angles for each skill
    angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()
    angles += angles[:1]  # Complete the circle

    # Extend data for closure
    data = np.concatenate((data, data[:, [0]]), axis=1)

    # Initialize the plot
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Plot each student's data
    colors = ['#FF6347', '#4682B4', '#32CD32']
    for idx, (d, color) in enumerate(zip(data, colors)):
        ax.fill(angles, d, color=color, alpha=0.25)
        ax.plot(angles, d, color=color, linewidth=2, label=student_labels[idx])

    # Customize the radar chart
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10)

    # Add title and legend
    plt.title(title, size=16, fontweight='bold', pad=20, va='bottom')
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title="Students")

    # Automatically adjust layout
    plt.tight_layout()

    # Display the plot
    plt.show()

# Call the function with the data
create_radar_chart(
    "Culinary Skills Assessment\nAspiring Chefs' Evaluation",
    skills, data, students
)