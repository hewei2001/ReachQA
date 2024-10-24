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

# Calculate the average adoption rate for each industry
average_adoption = adoption_data.mean(axis=1)

# Simulated growth rate data (in percentages) for each technology
growth_data = np.array([
    [5, 10, 8, 7],    # Tech
    [6, 9, 7, 6],     # Healthcare
    [7, 8, 6, 5],     # Finance
    [8, 7, 5, 6],     # Education
    [5, 6, 5, 4]      # Retail
])
average_growth = growth_data.mean(axis=1)

# Set up the figure with a secondary y-axis
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

# Define colors for each technology
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Plot the horizontal bar chart
y_positions = np.arange(len(industries))
bar_height = 0.15
offset = np.arange(-(len(technologies)-1)/2, (len(technologies)+1)/2) * bar_height

for idx, (tech, color) in enumerate(zip(technologies, colors)):
    ax1.barh(y_positions + offset[idx], adoption_data[:, idx], bar_height, label=tech, color=color, edgecolor='black')

# Overlay a line plot for average adoption rate
ax1.plot(average_adoption, y_positions, color='darkgreen', marker='o', markersize=8, linestyle='-', linewidth=2, label='Avg Adoption Rate')

# Add a secondary line plot for growth rate
ax2.plot(average_growth, y_positions, color='purple', marker='s', markersize=8, linestyle='--', linewidth=2, label='Avg Growth Rate')

# Add labels and titles
ax1.set_xlabel('Percentage of Workforce Using Technology', fontsize=12)
ax1.set_title('Adoption and Growth of Remote Work Technologies by Industry\nSurvey of 2023', fontsize=14, fontweight='bold')
ax1.set_yticks(y_positions)
ax1.set_yticklabels(industries, fontsize=11)
ax2.set_ylabel('Growth Rate (%)', fontsize=12, color='purple')

# Annotate each bar with the percentage values
for i in range(len(industries)):
    for j in range(len(technologies)):
        ax1.text(adoption_data[i, j] + 1, i + offset[j], f'{adoption_data[i, j]}%', 
                 va='center', fontsize=9, color='black')
    ax1.text(average_adoption[i] + 1, i, f'{average_adoption[i]:.1f}%', va='center', fontsize=9, color='darkgreen')

# Add legends
ax1.legend(loc='upper left', fontsize=10, bbox_to_anchor=(0, 1))
ax2.legend(loc='upper right', fontsize=10, bbox_to_anchor=(1, 1))

# Enhance readability with grid lines
ax1.xaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()