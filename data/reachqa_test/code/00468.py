import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from math import pi

# Personality traits categories
categories = ['Openness', 'Conscientiousness', 'Extraversion', 
              'Agreeableness', 'Neuroticism', 'Honesty-Humility']

N = len(categories)

# User type trait data
influencer_traits = [9, 5, 9, 6, 4, 5]
casual_user_traits = [5, 6, 5, 5, 3, 4]
data_driven_user_traits = [6, 8, 4, 7, 2, 6]

data = np.array([influencer_traits, casual_user_traits, data_driven_user_traits])
data = np.concatenate((data, data[:, [0]]), axis=1)

angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

# Improved colors and markers
colors = ['#FF6347', '#4682B4', '#32CD32']
markers = ['o', 's', '^']
labels = ['Influencer', 'Casual User', 'Data-Driven User']

for d, color, label, marker in zip(data, colors, labels, markers):
    ax.fill(angles, d, color=color, alpha=0.25, label=label)
    ax.plot(angles, d, color=color, linewidth=2, marker=marker, markersize=10)

    # Annotate the maximum trait value for each user type
    max_index = np.argmax(d[:-1])
    ax.text(angles[max_index], d[max_index], str(d[max_index]), 
            horizontalalignment='center', verticalalignment='bottom', fontsize=10, color=color)

plt.xticks(angles[:-1], categories, color='grey', size=12, weight='bold')

# Dynamically adjust radial limits
ax.set_ylim(0, 10)

# Enhanced grid lines
ax.yaxis.grid(True, color='lightgrey', linestyle=':', linewidth=1.0, alpha=0.7)
ax.xaxis.grid(True, color='darkgrey', linestyle='--', linewidth=1.0, alpha=0.5)

# Title with line breaks
plt.title('Personality Traits Analysis\nof Social Media Users', size=18, color='darkslategray', y=1.1, fontweight='bold')

# Enhanced legend with custom markers
legend_elements = [Patch(facecolor='#FF6347', edgecolor='none', label='Influencer'),
                   Patch(facecolor='#4682B4', edgecolor='none', label='Casual User'),
                   Patch(facecolor='#32CD32', edgecolor='none', label='Data-Driven User')]
ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10, frameon=False, title='User Types')

ax.tick_params(axis='both', which='major', labelsize=10)

plt.tight_layout()
plt.show()