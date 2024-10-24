import numpy as np
import matplotlib.pyplot as plt

# Define the tech skills
skills = ['Programming Languages', 'Data Analysis', 'UI/UX Design', 
          'Digital Marketing', 'Cloud Computing', 'Cybersecurity',
          'Machine Learning', 'Artificial Intelligence', 
          'Project Management', 'DevOps']

# Create proficiency data for each department
development = np.array([90, 75, 65, 55, 85, 70, 80, 70, 60, 65])
marketing = np.array([50, 65, 75, 90, 55, 40, 60, 50, 45, 50])
design = np.array([70, 80, 90, 60, 50, 30, 65, 55, 70, 60])
sales = np.array([60, 50, 70, 75, 80, 65, 60, 55, 50, 65])
hr = np.array([55, 70, 65, 80, 60, 70, 50, 60, 65, 55])

# Create a 2D array to hold all the data
data = np.array([development, marketing, design, sales, hr])

# Define department names
departments = ['Development', 'Marketing', 'Design', 'Sales', 'HR']

# Set up the figure
fig = plt.figure(figsize=(12, 12))

# Create a polar subplot for the radar chart
ax = fig.add_subplot(111, polar=True)

# Calculate angles for each skill
angles = np.linspace(0, 2 * np.pi, len(skills), endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Plot each department's proficiency
for i, (department, values) in enumerate(zip(departments, data)):
    values = np.concatenate((values, [values[0]]))  # Close the circle
    ax.plot(angles, values, label=department, 
            linewidth=2, marker='o', color=plt.cm.tab20(i), alpha=0.7)

# Set the angle for each skill
ax.set_thetagrids(np.degrees(angles[:-1]), skills)

# Set limits for the radial axis
ax.set_ylim(0, 100)

# Calculate and plot the average proficiency
average_values = np.mean(data, axis=0)
average_values = np.concatenate((average_values, [average_values[0]]))  # Close the circle
ax.plot(angles, average_values, label='Average Proficiency', 
        linewidth=2, marker='x', color='black', linestyle='--', alpha=0.9)

# Set the title with line breaks for visibility
ax.set_title("Tech Skills Proficiency Across Departments\nA 2023 Overview", 
             va='bottom', fontsize=16)

# Add a legend
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1))

# Improve layout to avoid occlusion
plt.tight_layout()

# Display the plot
plt.show()