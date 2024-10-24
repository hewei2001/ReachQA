import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Categories and number of variables
categories = ['Tone Quality', 'Build Quality', 'Playability', 'Visual Aesthetics', 'Innovation']
N = len(categories)

# Data for each guitar brand
fender = [8, 7, 9, 6, 7]
gibson = [9, 8, 8, 7, 6]
ibanez = [7, 6, 9, 8, 8]
prs = [8, 9, 7, 9, 9]
taylor = [7, 8, 8, 8, 7]

# Compute total score for each brand
total_scores = [sum(fender), sum(gibson), sum(ibanez), sum(prs), sum(taylor)]
brands = ['Fender', 'Gibson', 'Ibanez', 'PRS', 'Taylor']

# Radar chart data preparation
angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
data = [fender + fender[:1], gibson + gibson[:1], ibanez + ibanez[:1], prs + prs[:1], taylor + taylor[:1]]
angles += angles[:1]

# Initialize the figure
fig, axs = plt.subplots(1, 2, figsize=(14, 7), subplot_kw=dict(polar=True), gridspec_kw=dict(width_ratios=[2, 3]))

# Radar chart
ax1 = axs[0]
for idx, d in enumerate(data):
    ax1.plot(angles, d, linewidth=2, label=brands[idx])
    ax1.fill(angles, d, alpha=0.15)

# Radar chart settings
ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(categories, fontsize=11, weight='bold')
ax1.set_ylim(0, 10)
ax1.set_yticks(range(1, 11))
ax1.set_yticklabels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], color='grey', size=9)
ax1.set_title('Guitar Brand Attributes Comparison', size=15, pad=20, weight='bold')
ax1.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

# Bar chart for total scores
ax2 = plt.subplot(122)
ax2.bar(brands, total_scores, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
ax2.set_title('Total Attribute Scores by Brand', size=15, weight='bold')
ax2.set_ylabel('Total Score', fontsize=12)
ax2.set_xlabel('Guitar Brand', fontsize=12)
ax2.set_ylim(0, max(total_scores) + 5)
ax2.set_yticks(range(0, max(total_scores) + 1, 5))

# Adjust layout and display
plt.tight_layout()
plt.show()