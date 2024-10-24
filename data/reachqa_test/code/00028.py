import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from mpl_toolkits.mplot3d import Axes3D

# Fictional effectiveness scores for digital marketing strategies (1-10 scale)
effectiveness_scores = np.array([8, 7, 5, 9, 4, 8, 6, 7, 5, 9, 10, 6, 8, 7, 9, 7, 6, 5, 8, 9,
                                 6, 8, 7, 9, 8, 6, 7, 8, 9, 6, 5, 10, 9, 7, 8, 7, 6, 8, 9, 7])

# Corresponding increase in monthly website visits (in percentage)
traffic_increase = np.array([40, 30, 20, 55, 15, 45, 28, 32, 18, 50, 60, 25, 35, 33, 53, 31, 27, 22, 43, 58,
                             42, 36, 39, 54, 41, 26, 30, 29, 47, 20, 18, 59, 56, 37, 40, 30, 25, 46, 52, 35])

# Simulated budget for each strategy ($K)
strategy_budget = np.array([12, 15, 8, 20, 5, 18, 10, 11, 7, 19, 25, 9, 14, 12, 22, 13, 11, 8, 15, 21,
                            17, 14, 12, 23, 16, 11, 13, 14, 20, 9, 6, 24, 22, 15, 19, 13, 10, 17, 23, 14])

# Assigning more detailed marketing strategies to each data point
detailed_strategies = ['SEO', 'Social Media - Facebook', 'Email - Weekly', 'Paid Ads - Google', 'Social Media - Instagram']
detailed_strategy_labels = np.random.choice(detailed_strategies, len(effectiveness_scores))

# Color map for different strategies
color_map = {'SEO': 'blue', 'Social Media - Facebook': 'green', 'Email - Weekly': 'red', 
             'Paid Ads - Google': 'purple', 'Social Media - Instagram': 'orange'}
colors = [color_map[strategy] for strategy in detailed_strategy_labels]

# Marker size based on a combination of effectiveness score and strategy budget
marker_sizes = (effectiveness_scores * strategy_budget) * 0.5

# Create a 3D scatter plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(effectiveness_scores, traffic_increase, strategy_budget, c=colors, s=marker_sizes, alpha=0.7, edgecolors='w', linewidth=0.5)

# Title and axis labels
ax.set_title('3D Analysis of Digital Marketing Strategies\nEffectiveness vs. Traffic Increase vs. Budget', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Strategy Effectiveness Score (1-10)', fontsize=12)
ax.set_ylabel('Increase in Monthly Website Visits (%)', fontsize=12)
ax.set_zlabel('Budget ($K)', fontsize=12)

# Legend creation using custom handles for clarity
legend_elements = [Line2D([0], [0], marker='o', color='w', markerfacecolor=color_map[strategy], markersize=10, label=strategy) for strategy in detailed_strategies]
ax.legend(handles=legend_elements, title="Marketing Strategy", loc='upper left')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()