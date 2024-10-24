import matplotlib.pyplot as plt
import squarify
import numpy as np

# Expanded discipline names and corresponding data
disciplines = ['Psychology', 'Sociology', 'Political Science', 'Economics', 
               'Anthropology', 'History', 'Education', 'Philosophy']
funding = [150, 120, 200, 180, 100, 90, 110, 95]  # in millions
research_output = [3500, 2500, 4000, 3000, 1500, 1200, 2000, 1800]  # number of publications
enrollment = [30, 25, 40, 35, 20, 15, 25, 22]  # in thousands

# New metric: Research Impact Factor (hypothetical quality scores)
impact_factors = [3.5, 2.5, 4.0, 3.0, 2.0, 1.8, 2.5, 2.2]

# Calculate sizes for treemap
sizes = [sum(x) for x in zip(funding, research_output, enrollment)]

# Generate additional data
funding_per_publication = [f / r for f, r in zip(funding, research_output)]

# Assign colors to each discipline
colors = plt.cm.viridis(np.linspace(0, 1, len(disciplines)))

# Create labels for each rectangle
labels = [
    f"{d}\nFunding: ${f}M\nPublications: {r}\nEnrollment: {e}K\nImpact Factor: {i}\nFunding/Publication: ${fp:.2f}"
    for d, f, r, e, i, fp in zip(disciplines, funding, research_output, enrollment, impact_factors, funding_per_publication)
]

# Create a figure for the treemap and the additional subplot
fig, axs = plt.subplots(1, 2, figsize=(18, 8))
ax1, ax2 = axs

# Create the treemap
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8, edgecolor='white', ax=ax1)
ax1.set_title('Ecosystem of Knowledge:\nTreemap of Academic Disciplines\nin Social Sciences', fontsize=16, weight='bold')
ax1.axis('off')  # Turn off the axis

# Create a bar plot for funding and research output
bar_width = 0.35
index = np.arange(len(disciplines))

bars1 = ax2.bar(index, funding, bar_width, label='Funding (in millions)', color='b')
bars2 = ax2.bar(index + bar_width, research_output, bar_width, label='Research Output', color='r')

ax2.set_xlabel('Disciplines', fontsize=14)
ax2.set_ylabel('Value', fontsize=14)
ax2.set_title('Funding vs. Research Output\nfor Academic Disciplines', fontsize=16, weight='bold')
ax2.set_xticks(index + bar_width / 2)
ax2.set_xticklabels(disciplines, rotation=45, ha='right')
ax2.legend()

# Adjust layout to avoid overlapping elements
plt.tight_layout()

# Show the chart
plt.show()