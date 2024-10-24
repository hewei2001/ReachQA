import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from math import pi

# Innovation categories
categories = ['Renewable Energy', 'Waste Management', 'Green Transport', 
              'Urban Green Spaces', 'Water Conservation', 'Carbon Reduction']

# Performance scores for each city
eco_city_alpha_scores = [85, 78, 92, 88, 80, 90]
greenopolis_beta_scores = [78, 85, 79, 86, 92, 84]
sustainaville_gamma_scores = [82, 80, 83, 90, 86, 88]

# Combine data into a list of lists
data = [eco_city_alpha_scores, greenopolis_beta_scores, sustainaville_gamma_scores]
city_names = ['EcoCity Alpha', 'Greenopolis Beta', 'Sustainaville Gamma']

# Calculate average scores for each category
average_scores = np.mean(data, axis=0)

# Setup the plot layout
fig = plt.figure(figsize=(14, 8))
gs = GridSpec(1, 2, figure=fig)

# First subplot: Radar chart
ax1 = fig.add_subplot(gs[0, 0], polar=True)
angles = np.linspace(0, 2 * pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

for scores, city, color in zip(data, city_names, ['#3CB371', '#4682B4', '#FF6347']):
    scores = scores + scores[:1]  # Fix: create a new list with closed loop
    ax1.plot(angles, scores, linewidth=2, linestyle='solid', color=color)
    ax1.fill(angles, scores, color=color, alpha=0.25, label=city)

ax1.set_theta_offset(pi / 2)
ax1.set_theta_direction(-1)
ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(categories, fontsize=10, color='darkblue')
ax1.set_ylim(0, 100)
ax1.yaxis.grid(True, linestyle='--', color='grey', alpha=0.7)
ax1.set_yticks(range(0, 101, 20))
ax1.set_yticklabels(map(str, range(0, 101, 20)), fontsize=8)
ax1.set_title('Sustainability Innovation Index:\nPerformance of Leading Eco-Cities', 
              size=15, color='darkgreen', y=1.1, ha='center')
ax1.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), title="Cities", fontsize=9)

# Second subplot: Bar chart
ax2 = fig.add_subplot(gs[0, 1])
x = np.arange(len(categories))
bar_width = 0.2

ax2.bar(x - bar_width, eco_city_alpha_scores, width=bar_width, label='EcoCity Alpha', color='#3CB371')
ax2.bar(x, greenopolis_beta_scores, width=bar_width, label='Greenopolis Beta', color='#4682B4')
ax2.bar(x + bar_width, sustainaville_gamma_scores, width=bar_width, label='Sustainaville Gamma', color='#FF6347')
ax2.plot(x, average_scores, 'k--', marker='o', label='Average Scores')

ax2.set_xticks(x)
ax2.set_xticklabels(categories, rotation=45, ha='right', fontsize=10)
ax2.set_ylim(0, 100)
ax2.set_ylabel('Scores', fontsize=12)
ax2.set_title('Average Category Scores\nAcross Eco-Cities', fontsize=15, color='darkgreen')
ax2.legend(title="Cities", fontsize=9, loc='upper right')

plt.tight_layout()
plt.show()