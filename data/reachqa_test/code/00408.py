import numpy as np
import matplotlib.pyplot as plt

# Define models and datasets
models = ['Logistic Regression', 'Decision Tree', 'Random Forest', 'SVM', 'KNN', 'Gradient Boosting']
datasets = ['Healthcare', 'Finance', 'Social Sciences', 'Environmental',
            'Geoscience', 'Astronomy', 'Consumer Behavior', 'E-commerce',
            'Tech Industry', 'Energy']

# Performance scores adjusted for models across datasets
scores = np.array([
    [75, 75, 80, 65, 70, 60, 75, 78, 80, 79],  # Logistic Regression
    [60, 55, 58, 50, 60, 55, 62, 60, 62, 60],  # Decision Tree
    [85, 86, 89, 80, 86, 82, 86, 89, 91, 90],  # Random Forest
    [75, 76, 73, 70, 75, 71, 77, 76, 74, 73],  # SVM
    [65, 64, 62, 60, 66, 63, 65, 64, 62, 61],  # KNN
    [90, 92, 95, 85, 91, 88, 92, 94, 97, 95]   # Gradient Boosting
])

# Calculate average scores for each model
average_scores = scores.mean(axis=1)

# Plotting the heat map
plt.figure(figsize=(16, 8))
cax = plt.imshow(scores, cmap='viridis', aspect='auto', origin='lower')

# Labeling axes
plt.yticks(np.arange(len(models)), models)
plt.xticks(np.arange(len(datasets)), datasets, rotation=70, ha='right')

# Title
title_text = 'Performance Consistency of ML Models\nAcross Diverse Datasets (2023)'
plt.title(title_text, fontsize=16)

# Colorbar
plt.colorbar(cax, label='Accuracy (%)', fraction=0.046, pad=0.04)

# Annotations
for i in range(len(models)):
    for j in range(len(datasets)):
        plt.text(j, i, f'{scores[i, j]:.1f}', ha='center', va='center', color='w', fontsize=8)

# Line plot overlay for average scores
plt.hlines(np.arange(len(models)) - 0.5, -0.5, len(datasets) - 0.5, colors='w', linestyle='--')
for i, model_avg in enumerate(average_scores):
    plt.plot([-0.5, len(datasets) - 0.5], [i - 0.5, i - 0.5], color='white', label='_nolegend_', alpha=0.7)
    plt.text(-1, i - 0.5, f'Avg: {model_avg:.1f}', color='white', ha='right', va='center')

# Adjust layout
plt.tight_layout()

# Show the heat map
plt.show()