import numpy as np
import matplotlib.pyplot as plt

# Define the evaluation categories
categories = ['R&D', 'Market Penetration', 'User Satisfaction', 'Innovation', 'Sustainability']
num_vars = len(categories)

# Scores for each tech company
companies_scores = {
    'TechCorp A': [8, 6, 7, 9, 5],
    'InnovateX': [6, 9, 8, 7, 6],
    'FutureTech': [7, 8, 6, 8, 7],
    'NextGen Inc.': [9, 7, 8, 6, 8],
    'EcoTech Solutions': [5, 6, 9, 7, 9]
}

# Calculate the angle for each category and complete the loop
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist() + [0]

def create_radar_chart(ax, scores, color, label):
    # Append the first score to close the radar chart
    scores = np.concatenate((scores, [scores[0]]))
    ax.plot(angles, scores, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, scores, color=color, alpha=0.25)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=9)
    ax.set_title(label, size=10, color=color, pad=10)

# Initialize the plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Set colors for each company
colors = plt.cm.tab10(np.linspace(0, 1, len(companies_scores)))

# Plot each company's radar chart
for idx, (company, scores) in enumerate(companies_scores.items()):
    create_radar_chart(ax, scores, colors[idx], company)

# Add a title and legend
plt.title("Tech Company Performance Evaluation\nBased on Key Criteria - 2023", fontsize=16, fontweight='bold', pad=20)
plt.legend(companies_scores.keys(), loc='upper right', bbox_to_anchor=(1.2, 1.1))

# Adjust the layout to prevent overlapping
plt.tight_layout()

# Display the radar chart
plt.show()