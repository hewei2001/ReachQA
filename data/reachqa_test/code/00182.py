import numpy as np
import matplotlib.pyplot as plt

# Time in months
months = np.arange(1, 13)

# Performance data for art supplies (consistency scale: 0 to 10)
acrylic_paints = np.array([8.2, 8.4, 8.6, 8.5, 8.7, 8.9, 8.8, 8.6, 8.7, 8.5, 8.8, 8.9])
watercolors = np.array([7.0, 7.1, 7.3, 7.2, 7.4, 7.3, 7.5, 7.4, 7.6, 7.3, 7.5, 7.6])
oil_pastels = np.array([6.5, 6.4, 6.6, 6.8, 6.7, 6.8, 7.0, 7.1, 7.0, 6.9, 7.2, 7.3])

# Errors (standard deviation of measurements)
acrylic_errors = np.array([0.2, 0.1, 0.15, 0.2, 0.18, 0.22, 0.25, 0.2, 0.24, 0.19, 0.25, 0.22])
watercolor_errors = np.array([0.3, 0.25, 0.3, 0.28, 0.35, 0.32, 0.33, 0.31, 0.34, 0.29, 0.3, 0.33])
oil_pastel_errors = np.array([0.35, 0.3, 0.32, 0.31, 0.29, 0.34, 0.35, 0.33, 0.32, 0.3, 0.33, 0.35])

# New data for an additional subplot (average user satisfaction scale: 0 to 10)
acrylic_satisfaction = 8.7
watercolor_satisfaction = 7.8
oil_pastel_satisfaction = 7.2

# Create a figure with 2 subplots (side by side)
fig, ax = plt.subplots(1, 2, figsize=(15, 7))

# Plot the first subplot: Error bars
ax[0].errorbar(months, acrylic_paints, yerr=acrylic_errors, label='Acrylic Paints',
               fmt='-o', capsize=5, color='orange', alpha=0.8, linestyle='solid')
ax[0].errorbar(months, watercolors, yerr=watercolor_errors, label='Watercolors',
               fmt='-s', capsize=5, color='blue', alpha=0.8, linestyle='dashed')
ax[0].errorbar(months, oil_pastels, yerr=oil_pastel_errors, label='Oil Pastels',
               fmt='-^', capsize=5, color='green', alpha=0.8, linestyle='dashdot')

ax[0].set_title('Art Supplies Performance Evaluation\nConsistency of Color and Texture',
                fontsize=14, fontweight='bold')
ax[0].set_xlabel('Month', fontsize=12)
ax[0].set_ylabel('Consistency Score (0-10)', fontsize=12)
ax[0].set_xticks(months)
ax[0].set_yticks(np.arange(6, 10.5, 0.5))
ax[0].grid(True, linestyle='--', alpha=0.5)
ax[0].legend(title='Art Supplies', loc='lower right', fontsize=10)

# Plot the second subplot: Bar chart for user satisfaction
categories = ['Acrylic Paints', 'Watercolors', 'Oil Pastels']
satisfaction_scores = [acrylic_satisfaction, watercolor_satisfaction, oil_pastel_satisfaction]
colors = ['orange', 'blue', 'green']

ax[1].bar(categories, satisfaction_scores, color=colors, alpha=0.7)
ax[1].set_title('Average User Satisfaction\n(Scale: 0 to 10)', fontsize=14, fontweight='bold')
ax[1].set_ylabel('Satisfaction Score', fontsize=12)
ax[1].set_ylim(0, 10)

# Enhance layout
plt.tight_layout()

# Display the plot
plt.show()