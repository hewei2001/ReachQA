import matplotlib.pyplot as plt
import numpy as np

# Decades considered
decades = np.array([1480, 1490, 1500, 1510])

# Influence (scale of 0 to 100) of each art style by decade
humanism = np.array([40, 50, 55, 60])
naturalism = np.array([45, 55, 60, 50])
realism = np.array([30, 35, 40, 45])
classicism = np.array([50, 60, 70, 75])
mannerism = np.array([20, 25, 30, 35])

# Estimated error margins for each style in each decade
error_humanism = np.array([5, 5, 4, 3])
error_naturalism = np.array([4, 6, 5, 4])
error_realism = np.array([3, 3, 4, 5])
error_classicism = np.array([5, 4, 3, 3])
error_mannerism = np.array([2, 3, 3, 4])

# Plotting the line chart with error bars
plt.figure(figsize=(12, 8))

plt.errorbar(decades, humanism, yerr=error_humanism, label='Humanism', fmt='-o', capsize=5, capthick=1, linestyle='--', color='blue', alpha=0.8)
plt.errorbar(decades, naturalism, yerr=error_naturalism, label='Naturalism', fmt='-s', capsize=5, capthick=1, linestyle='-.', color='green', alpha=0.8)
plt.errorbar(decades, realism, yerr=error_realism, label='Realism', fmt='-^', capsize=5, capthick=1, linestyle=':', color='red', alpha=0.8)
plt.errorbar(decades, classicism, yerr=error_classicism, label='Classicism', fmt='-d', capsize=5, capthick=1, linestyle='-', color='purple', alpha=0.8)
plt.errorbar(decades, mannerism, yerr=error_mannerism, label='Mannerism', fmt='-p', capsize=5, capthick=1, linestyle='-.', color='orange', alpha=0.8)

# Adding plot details
plt.title("The Evolution of Renaissance Art Styles\nAcross the Decades (1480s-1510s)", fontsize=16, fontweight='bold', ha='center')
plt.xlabel('Decades', fontsize=14)
plt.ylabel('Influence Score (0-100)', fontsize=14)
plt.xticks(decades)
plt.yticks(np.arange(0, 101, 10))
plt.ylim(0, 100)
plt.legend(title='Art Styles', fontsize=10, loc='upper left')

# Enhance layout to prevent text overlap and ensure readability
plt.tight_layout()

# Show plot
plt.show()