import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# Define artistic movements and their influence scores
art_movements = [
    'Renaissance', 'Baroque', 'Romanticism', 'Impressionism',
    'Cubism', 'Surrealism', 'Abstract Expressionism', 'Pop Art',
    'Minimalism', 'Contemporary'
]

# Influence scores (out of 100)
influence_scores = [95, 85, 78, 80, 88, 75, 82, 70, 60, 90]

# Sort movements by influence scores for visual coherence
sorted_indices = np.argsort(influence_scores)
sorted_art_movements = np.array(art_movements)[sorted_indices]
sorted_influence_scores = np.array(influence_scores)[sorted_indices]

# Prepare grouped data for the pie chart
period_labels = ['Historical', 'Modern', 'Contemporary']
period_scores = [
    sum(influence_scores[:3]),  # Historical: Renaissance to Romanticism
    sum(influence_scores[3:7]), # Modern: Impressionism to Abstract Expressionism
    sum(influence_scores[7:])   # Contemporary: Pop Art to Contemporary
]

# Plot creation with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Generate a color map
colors = cm.viridis(np.linspace(0, 1, len(sorted_art_movements)))

# Horizontal bar chart
bars = ax1.barh(sorted_art_movements, sorted_influence_scores, color=colors, edgecolor='black', height=0.6)
ax1.set_title('Evolution of Influence:\nKey Artistic Movements Over Time', fontsize=16, weight='bold', pad=15)
ax1.set_xlabel('Influence Score (out of 100)', fontsize=12)
ax1.set_ylabel('Artistic Movements', fontsize=12)
ax1.grid(visible=True, which='both', axis='x', linestyle='--', linewidth=0.7, alpha=0.7)
for bar in bars:
    width = bar.get_width()
    ax1.text(width + 1, bar.get_y() + bar.get_height() / 2, f'{width}', 
             va='center', ha='left', fontsize=11, fontweight='bold', color='black')
ax1.set_xlim(0, max(sorted_influence_scores) + 10)

# Pie chart for periods
pie_colors = [cm.viridis(0.2), cm.viridis(0.5), cm.viridis(0.8)]
wedges, texts, autotexts = ax2.pie(period_scores, labels=period_labels, autopct='%1.1f%%', startangle=140, colors=pie_colors, textprops=dict(color="w"))
ax2.set_title('Influence Over Artistic Periods', fontsize=16, weight='bold')
for text in texts + autotexts:
    text.set_fontsize(12)
ax2.legend(wedges, period_labels, title="Periods", loc="center left", bbox_to_anchor=(0.85, 0, 0.5, 1), fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()