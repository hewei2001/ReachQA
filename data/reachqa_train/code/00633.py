import matplotlib.pyplot as plt
import numpy as np

# Define industries and remote work technologies
industries = ['Tech', 'Healthcare', 'Finance', 'Education', 'Retail']
technologies = ['Video Conf.', 'Cloud Storage', 'Proj. Mgmt', 'Collab. Tools']

# Data representing the percentage of workforce using each technology in different industries
adoption_data = np.array([
    [85, 90, 80, 75],  # Tech
    [70, 85, 60, 65],  # Healthcare
    [60, 80, 70, 60],  # Finance
    [75, 65, 80, 70],  # Education
    [55, 70, 65, 50]   # Retail
])

# Set up the figure
fig, ax = plt.subplots(figsize=(12, 8))

# Define colors for each technology
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Plot the horizontal bar chart
y_positions = np.arange(len(industries))
bar_height = 0.15
offset = np.arange(-(len(technologies)-1)/2, (len(technologies)+1)/2) * bar_height

for idx, (tech, color) in enumerate(zip(technologies, colors)):
    ax.barh(y_positions + offset[idx], adoption_data[:, idx], bar_height, label=tech, color=color)

# Add labels and title
ax.set_xlabel('Percentage of Workforce Using Technology', fontsize=12)
ax.set_title('Adoption of Remote Work Technologies by Industry\nSurvey of 2023', fontsize=14, fontweight='bold')
ax.set_yticks(y_positions)
ax.set_yticklabels(industries, fontsize=11)
ax.legend(title='Technology', loc='upper right', fontsize=10)

# Annotate each bar with the percentage values
for i in range(len(industries)):
    for j in range(len(technologies)):
        ax.text(adoption_data[i, j] + 1, i + offset[j], f'{adoption_data[i, j]}%', 
                va='center', fontsize=9, color='black')

# Enhance readability with grid lines
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to ensure no overlapping
plt.tight_layout()

# Display the plot
plt.show()