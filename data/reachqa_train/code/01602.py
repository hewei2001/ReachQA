import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Decades and their corresponding technological impact scores
decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
impact_scores = [2, 3, 5, 7, 8, 9, 9.5]

# Description for annotations, representing key innovations
annotations = [
    'Integrated Circuit',
    'Personal Computers',
    'The Internet',
    'World Wide Web',
    'Smartphones',
    'Social Media',
    'AI & Machine Learning'
]

# Calculate the rate of change for a secondary y-axis
rate_of_change = [0] + [impact_scores[i] - impact_scores[i-1] for i in range(1, len(impact_scores))]

# Set up the figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

# Define colors
colors = list(mcolors.TABLEAU_COLORS.values())
line_color = colors[0]

# Plot the line chart
ax1.plot(decades, impact_scores, marker='o', color=line_color, linestyle='-', linewidth=2.5, markersize=10, label="Impact Score")

# Fill the area under the curve
ax1.fill_between(decades, impact_scores, color=line_color, alpha=0.1)

# Plot the secondary rate of change as a bar chart
ax2.bar(decades, rate_of_change, color=colors[1], alpha=0.6, label='Rate of Change', width=0.4, align='center')

# Annotate each point with the key innovation
for i, txt in enumerate(annotations):
    ax1.annotate(txt, (decades[i], impact_scores[i]), textcoords="offset points", xytext=(0, 15), ha='center',
                 fontsize=9, rotation=45, backgroundcolor='w', bbox=dict(facecolor='white', alpha=0.5, boxstyle='round,pad=0.2'))

# Add titles and labels
ax1.set_title('Technological Innovations Over the Decades\n(1960s to 2020s)', fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel('Decade', fontsize=14)
ax1.set_ylabel('Impact Score (0-10)', fontsize=14, color=line_color)
ax2.set_ylabel('Rate of Change', fontsize=14, color=colors[1])

# Add grid lines
ax1.grid(True, linestyle='--', alpha=0.7)

# Add legends
ax1.legend(loc='upper left', fontsize=11)
ax2.legend(loc='upper right', fontsize=11)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()