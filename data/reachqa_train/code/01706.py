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

# Compiling the data and brand labels
data = [fender, gibson, ibanez, prs, taylor]
brands = ['Fender', 'Gibson', 'Ibanez', 'PRS', 'Taylor']

# Compute angle for each category
angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()

# Extend the data so the radar chart closes
data = [d + d[:1] for d in data]
angles += angles[:1]

# Initialize radar plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one axis per variable and add labels
plt.xticks(angles[:-1], categories, fontsize=12, weight='bold')

# Draw y-labels and limit them within the radar chart
ax.set_rscale('linear')
plt.yticks(range(1, 11), ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], color='grey', size=10)
ax.set_ylim(0, 10)

# Plot each brand's data
for idx, d in enumerate(data):
    ax.plot(angles, d, linewidth=2, linestyle='solid', label=brands[idx])
    ax.fill(angles, d, alpha=0.1)

# Add title and legend
plt.title('Guitar Brand Attributes Comparison', size=18, pad=20, weight='bold')
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10, title='Brands')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()