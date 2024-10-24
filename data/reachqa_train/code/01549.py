import matplotlib.pyplot as plt
import numpy as np

# Data for conservation efforts
efforts = [30, 20, 15, 25, 10]
categories = ['Habitat Preservation', 'Anti-Poaching', 'Captive Breeding', 'Legal Protection', 'Public Awareness']
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

# Related data for the bar plot
budget_allocation = [35, 25, 10, 20, 15]  # Hypothetical data in percentage
impact_score = [7, 8.5, 6, 9, 5.5]  # Hypothetical impact scores out of 10

# Set up figure and axes for the subplot
fig, axes = plt.subplots(1, 2, figsize=(16, 8), dpi=100)

# Donut pie chart
wedges, texts, autotexts = axes[0].pie(efforts, labels=categories, autopct='%1.1f%%', startangle=90, 
                                       colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w'), 
                                       explode=[0.05, 0, 0, 0, 0])
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
axes[0].add_artist(plt.Circle((0, 0), 0.7, fc='white', edgecolor='lightgray'))
axes[0].set_title('Efforts in Animal Conservation\nin 2023', fontsize=16, fontweight='bold', pad=20)
axes[0].legend(wedges, categories, title="Conservation Strategies", loc="center left", 
               bbox_to_anchor=(1.2, 0, 0.5, 1), fontsize=10)

# Bar plot for budget allocation and impact score
bar_width = 0.35
indices = np.arange(len(categories))

# Plotting budget allocation
bars1 = axes[1].bar(indices - bar_width/2, budget_allocation, bar_width, label='Budget Allocation (%)', color='#66c2a5')

# Plotting impact score
bars2 = axes[1].bar(indices + bar_width/2, impact_score, bar_width, label='Impact Score', color='#8da0cb')

# Enhancing bar plot aesthetics
axes[1].set_title('Budget Allocation & Impact Scores\nfor Conservation Strategies', fontsize=16, fontweight='bold', pad=20)
axes[1].set_xticks(indices)
axes[1].set_xticklabels(categories, rotation=30, ha='right', fontsize=12)
axes[1].set_ylabel('Values', fontsize=12)
axes[1].legend(loc='upper right', fontsize=10)
axes[1].set_ylim(0, 40)  # Adjust ylim for better visibility

# Add data labels on the bars
for bar in bars1 + bars2:
    yval = bar.get_height()
    axes[1].text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval:.1f}', ha='center', va='bottom', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()