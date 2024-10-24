import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the skill areas with additional complexity
skill_areas = [
    'Data Preprocessing', 'Algorithm Design', 'Model Evaluation',
    'Deployment', 'Collaboration &\nCommunication', 'Research &\nDevelopment'
]

# Define the skill levels for each team with an extra skill category
alpha_team_skills = [8, 6, 7, 5, 9, 6]
beta_team_skills = [5, 7, 8, 6, 7, 5]
gamma_team_skills = [7, 9, 6, 4, 8, 7]
delta_team_skills = [6, 5, 8, 7, 6, 8]

# Combine data into a dictionary for easy plotting
teams_data = {
    'Alpha Team': alpha_team_skills,
    'Beta Team': beta_team_skills,
    'Gamma Team': gamma_team_skills,
    'Delta Team': delta_team_skills
}

# Define colors for each team
team_colors = {
    'Alpha Team': 'red',
    'Beta Team': 'blue',
    'Gamma Team': 'green',
    'Delta Team': 'orange'
}

# Function to create a radar chart
def create_radar_chart(ax, team_data, labels, team_name, color):
    num_vars = len(labels)
    angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
    
    # The radar chart is a closed loop, so complete the loop
    team_data += team_data[:1]
    angles += angles[:1]

    # Create the radar chart
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axis per variable and add labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=8)

    # Draw ylabels
    ax.set_rlabel_position(0)
    ax.yaxis.set_tick_params(labelsize=7)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(["2", "4", "6", "8", "10"])
    ax.set_ylim(0, 10)

    # Plot data
    ax.plot(angles, team_data, linewidth=2, linestyle='solid', label=team_name, color=color)

    # Fill area
    ax.fill(angles, team_data, color=color, alpha=0.3)

# Function to create a bar chart
def create_bar_chart(ax, teams_data, skill_areas):
    num_teams = len(teams_data)
    index = np.arange(len(skill_areas))

    # For bar width and offsets
    bar_width = 0.2
    opacity = 0.8

    for i, (team_name, team_skills) in enumerate(teams_data.items()):
        ax.bar(index + i * bar_width, team_skills, bar_width,
               alpha=opacity, label=team_name, color=team_colors[team_name])

    ax.set_xlabel('Skill Areas', fontsize=10)
    ax.set_ylabel('Skill Level', fontsize=10)
    ax.set_title('Skill Distribution Across Teams', fontsize=12)
    ax.set_xticks(index + bar_width * (num_teams / 2 - 0.5))
    ax.set_xticklabels(skill_areas, rotation=45, ha='right', fontsize=8)
    ax.set_ylim(0, 10)
    ax.legend()

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), subplot_kw={'polar': True})

# Create radar chart for the first subplot
for team_name, skill_levels in teams_data.items():
    create_radar_chart(ax1, skill_levels[:], skill_areas, team_name, team_colors[team_name])
ax1.set_title('Team Skill Set Comparison', size=14, y=1.1)

# Remove polar attribute to create standard axes for bar chart
ax2.remove()
ax2 = fig.add_subplot(1, 2, 2)
create_bar_chart(ax2, teams_data, skill_areas)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()