import matplotlib.pyplot as plt
import numpy as np

# Extended range of decades and influence data
decades = np.arange(1450, 1560, 10)

# Influence scores for each art style across the expanded decades
humanism = np.array([30, 35, 40, 50, 55, 60, 62, 65, 70, 72, 75])
naturalism = np.array([25, 30, 35, 45, 55, 60, 58, 50, 48, 47, 45])
realism = np.array([20, 25, 30, 35, 40, 45, 50, 52, 55, 57, 60])
classicism = np.array([40, 45, 50, 60, 70, 75, 78, 80, 82, 85, 88])
mannerism = np.array([15, 20, 25, 30, 35, 40, 42, 45, 47, 50, 53])

# Estimated error margins for each style
error_humanism = np.array([5, 5, 5, 5, 4, 3, 3, 3, 3, 3, 2])
error_naturalism = np.array([3, 3, 4, 4, 5, 4, 3, 4, 4, 3, 3])
error_realism = np.array([3, 2, 3, 3, 4, 5, 4, 4, 5, 4, 3])
error_classicism = np.array([4, 4, 5, 4, 3, 3, 2, 2, 3, 2, 2])
error_mannerism = np.array([3, 3, 3, 3, 3, 4, 3, 4, 4, 3, 3])

# Plot setup
fig, ax = plt.subplots(figsize=(14, 10))

# Plot with error bars
ax.errorbar(decades, humanism, yerr=error_humanism, label='Humanism', fmt='-o', capsize=5, linestyle='--', color='blue', alpha=0.8)
ax.errorbar(decades, naturalism, yerr=error_naturalism, label='Naturalism', fmt='-s', capsize=5, linestyle='-.', color='green', alpha=0.8)
ax.errorbar(decades, realism, yerr=error_realism, label='Realism', fmt='-^', capsize=5, linestyle=':', color='red', alpha=0.8)
ax.errorbar(decades, classicism, yerr=error_classicism, label='Classicism', fmt='-d', capsize=5, linestyle='-', color='purple', alpha=0.8)
ax.errorbar(decades, mannerism, yerr=error_mannerism, label='Mannerism', fmt='-p', capsize=5, linestyle='-.', color='orange', alpha=0.8)

# Adding additional elements
ax.fill_between(decades, humanism - error_humanism, humanism + error_humanism, color='blue', alpha=0.1)
ax.fill_between(decades, classicism - error_classicism, classicism + error_classicism, color='purple', alpha=0.1)

# Secondary Y-axis for cumulative influence
ax2 = ax.twinx()
cumulative_influence = humanism + naturalism + realism + classicism + mannerism
ax2.plot(decades, cumulative_influence, label='Cumulative Influence', color='grey', linestyle='--', linewidth=2, alpha=0.7)
ax2.set_ylabel('Cumulative Influence Score', fontsize=14, color='grey')
ax2.tick_params(axis='y', labelcolor='grey')

# Enhanced titles and labels
ax.set_title("Evolution of Renaissance Art Styles\n1450s to 1550s with Cumulative Influence", fontsize=18, fontweight='bold', ha='center')
ax.set_xlabel('Decades', fontsize=14)
ax.set_ylabel('Influence Score (0-100)', fontsize=14)

# Ensure all text fits without overlap
plt.xticks(decades)
ax.set_yticks(np.arange(0, 101, 10))
ax.set_ylim(0, 100)
ax.legend(title='Art Styles', fontsize=12, loc='upper left', bbox_to_anchor=(1.05, 1))
ax2.legend(loc='upper right', fontsize=12, bbox_to_anchor=(1.05, 0.9))

# Layout adjustments
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show plot
plt.show()