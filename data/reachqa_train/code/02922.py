import matplotlib.pyplot as plt
import squarify

# Define the engineering disciplines and their respective student numbers
disciplines = [
    "Mechanical Engineering", "Electrical Engineering", "Civil Engineering",
    "Computer Science", "Chemical Engineering", "Aerospace Engineering",
    "Biomedical Engineering", "Industrial Engineering", "Environmental Engineering",
    "Robotics Engineering"
]

# Student numbers for each discipline (hypothetical)
students = [600, 750, 500, 900, 450, 350, 300, 400, 200, 250]

# Colors for the tree map
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0',
    '#ffb3e6', '#c4e17f', '#6b8e23', '#e6e6fa', '#ffefd5'
]

# Plotting the tree map
plt.figure(figsize=(12, 8))
squarify.plot(sizes=students, label=disciplines, color=colors, alpha=0.8, pad=True, text_kwargs={'fontsize': 10})

# Add title and labels
plt.title("Distribution of Modern Engineering Disciplines\nat FutureTech University", fontsize=16, fontweight='bold')
plt.axis('off')  # No axis for a clean look

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()