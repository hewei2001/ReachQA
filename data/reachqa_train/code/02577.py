import matplotlib.pyplot as plt
import numpy as np

# Define the categories for the radar chart
categories = ['Strategic Planning', 'Player Development', 'Communication', 'Adaptability', 'Mental Toughness']
num_categories = len(categories)

# Skill ratings for each coach
coach_a_skills = [9, 7, 8, 6, 9]
coach_b_skills = [8, 9, 7, 8, 7]
coach_c_skills = [6, 8, 9, 9, 8]
coach_d_skills = [7, 6, 8, 7, 9]

# Function to plot the radar chart
def plot_radar_chart(data, labels, categories):
    # Calculate the angles for each category
    angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()

    # Append the start value to close the loop
    data = [np.array(d + [d[0]]) for d in data]
    angles += angles[:1]

    # Create the radar chart
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Plot each coach's data and fill the area
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    for i, (d, label, color) in enumerate(zip(data, labels, colors)):
        ax.plot(angles, d, label=label, color=color, linewidth=2, linestyle='solid')
        ax.fill(angles, d, color=color, alpha=0.25)

    # Add the category labels
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10)

    # Add title and legend
    plt.title('Skill Profiles of Renowned Sports Coaches\nComparison of Key Coaching Attributes',
              size=16, fontweight='bold', pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

    # Add grid and customize appearance
    ax.grid(True, linestyle='--', linewidth=0.5)

    # Automatically adjust layout to prevent overlap
    plt.tight_layout()

    # Display the plot
    plt.show()

# Plot the radar chart with the skill data
plot_radar_chart([coach_a_skills, coach_b_skills, coach_c_skills, coach_d_skills],
                 ['Coach A', 'Coach B', 'Coach C', 'Coach D'],
                 categories)