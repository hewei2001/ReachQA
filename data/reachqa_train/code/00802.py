import matplotlib.pyplot as plt
import numpy as np

# List of skyscrapers
skyscrapers = ['Burj Khalifa', 'Shanghai Tower', 'Abraj Al Bait', 'Ping An\nFinance Centre', 'Lotte\nWorld Tower']

# Synthetic data: Stress test scores over the decade
stress_scores = [
    [85, 88, 90, 87, 85, 89, 91, 88, 86, 89, 90],  # Burj Khalifa
    [82, 84, 86, 83, 85, 87, 89, 84, 83, 85, 86],  # Shanghai Tower
    [78, 80, 82, 79, 81, 83, 85, 80, 79, 81, 82],  # Abraj Al Bait
    [87, 89, 91, 88, 90, 92, 94, 89, 87, 90, 91],  # Ping An Finance Centre
    [83, 85, 87, 84, 86, 88, 90, 85, 84, 86, 87]   # Lotte World Tower
]

# Create a vertical box plot
plt.figure(figsize=(10, 6))
box = plt.boxplot(stress_scores, labels=skyscrapers, patch_artist=True, notch=True,
                  boxprops=dict(facecolor='#cce5ff', color='#0000ff'),
                  whiskerprops=dict(color='#0000ff'), capprops=dict(color='#0000ff'),
                  medianprops=dict(color='orange'), flierprops=dict(marker='o', color='#00ff00', alpha=0.5))

# Set title and labels
plt.title("Structural Integrity Assessments\nof Iconic Skyscrapers (2010-2020)", fontsize=14, fontweight='bold', pad=20)
plt.ylabel("Stress Test Score", fontsize=12)
plt.xlabel("Skyscrapers", fontsize=12)

# Annotate average scores on the chart
for i, scores in enumerate(stress_scores):
    avg_score = np.mean(scores)
    plt.annotate(f'Avg: {avg_score:.1f}', (i + 1, avg_score), textcoords="offset points", xytext=(0, 10),
                 ha='center', fontsize=10, color='red')

# Grid for readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to ensure everything fits well
plt.tight_layout()

# Display the plot
plt.show()