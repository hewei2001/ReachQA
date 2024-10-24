import matplotlib.pyplot as plt
import numpy as np

# Culinary techniques and their popularity scores
culinary_techniques = [
    "Sous Vide",
    "Fermentation",
    "Smoking",
    "Pickling",
    "Braising",
    "Sautéing",
    "Grilling",
    "Poaching",
    "Steaming",
    "Roasting"
]

# Popularity scores in percentage
popularity_scores = [15, 25, 20, 18, 17, 40, 50, 30, 35, 45]

# Assigning colors for each bar
colors = ['#c7e9b4', '#7fcdbb', '#41b6c4', '#1d91c0', '#225ea8', 
          '#253494', '#081d58', '#b30000', '#e34a33', '#fc8d59']

# Plotting the horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))
y_pos = np.arange(len(culinary_techniques))

# Create horizontal bars
ax.barh(y_pos, popularity_scores, color=colors, edgecolor='black', alpha=0.8)

# Set y-ticks with the culinary techniques
ax.set_yticks(y_pos)
ax.set_yticklabels(culinary_techniques, fontsize=10, fontweight='medium')
ax.invert_yaxis()  # Highest score on top

# Titles and labels
ax.set_title('Top Culinary Techniques in World Cuisines\nBased on Global Chef Survey', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Popularity Score (%)', fontsize=12)
ax.set_ylabel('Culinary Techniques', fontsize=12)

# Annotate each bar with the popularity score
for i in range(len(popularity_scores)):
    ax.text(popularity_scores[i] + 1, i, f'{popularity_scores[i]}%', 
            va='center', color='black', fontsize=10)

# Add grid lines for x-axis
ax.grid(axis='x', linestyle='--', alpha=0.6)

# Ensure layout is tight
plt.tight_layout()

# Display the plot
plt.show()