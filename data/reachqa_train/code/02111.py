import matplotlib.pyplot as plt
import numpy as np

# Define the extended fitness categories and scores for sample astronauts
categories = ['Cardio Endurance', 'Muscle Strength', 'Flexibility', 'Balance', 
              'Agility', 'Speed', 'Coordination', 'Power', 'Reaction Time', 'Endurance']

# Sample scores for two astronauts on a scale of 0 to 10
scores_astronaut1 = [8, 7, 5, 9, 7, 6, 8, 7, 9, 8]
scores_astronaut2 = [7, 8, 6, 8, 6, 7, 7, 8, 6, 7]

# Append the first score to the end to complete the loop for radar chart
scores_astronaut1 += scores_astronaut1[:1]
scores_astronaut2 += scores_astronaut2[:1]

# Calculate angle for each axis
num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot data for both astronauts
ax.fill(angles, scores_astronaut1, color='skyblue', alpha=0.4, label='Astronaut 1')
ax.plot(angles, scores_astronaut1, color='blue', linewidth=2)
ax.fill(angles, scores_astronaut2, color='lightcoral', alpha=0.4, label='Astronaut 2')
ax.plot(angles, scores_astronaut2, color='red', linewidth=2)

# Set category labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10)

# Add statistical markers
max_value = max(max(scores_astronaut1), max(scores_astronaut2))
ax.annotate('Highest\nScore', xy=(angles[scores_astronaut1.index(max_value)], max_value), 
            xytext=(angles[scores_astronaut1.index(max_value)] - 0.2, max_value + 0.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adjust for overlap
plt.title('Comparative Astronaut Fitness Evaluation\nMars 2035 Mission', size=16, fontweight='bold', pad=40)
plt.tight_layout(pad=2)

# Set radial ticks and labels
ax.set_rlabel_position(30)
ax.yaxis.set_ticks(np.arange(0, 11, 2.5))

# Include a legend
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10)

# Display the radar chart
plt.show()