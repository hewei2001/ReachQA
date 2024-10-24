import matplotlib.pyplot as plt
import numpy as np

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

# Set up the figure and axis for the line chart
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the line chart
ax.plot(decades, impact_scores, marker='o', color='teal', linestyle='-', linewidth=2, markersize=8, label="Impact Score")

# Annotate each point with the key innovation
for i, txt in enumerate(annotations):
    ax.annotate(txt, (decades[i], impact_scores[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, rotation=45)

# Adding titles and labels
ax.set_title('Technological Innovations Over the Decades\n1960s to 2020s', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Impact Score (0-10)', fontsize=12)

# Add grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Add a legend
ax.legend(loc='upper left', fontsize=10)

# Adjust layout for neatness
plt.tight_layout()

# Display the plot
plt.show()