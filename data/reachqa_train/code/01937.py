import matplotlib.pyplot as plt
import numpy as np

# Months of the year
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Satisfaction scores for each category (hypothetical data)
appetizers_scores = [78, 80, 82, 83, 85, 86, 85, 84, 83, 82, 84, 86]
main_courses_scores = [75, 77, 78, 81, 83, 85, 87, 86, 85, 84, 83, 85]
desserts_scores = [88, 87, 89, 91, 90, 92, 94, 93, 91, 90, 92, 95]
beverages_scores = [70, 72, 75, 76, 77, 79, 81, 80, 79, 78, 80, 82]
specials_scores = [65, 67, 69, 71, 73, 75, 77, 76, 74, 72, 73, 75]

# Error margins (assuming some variation in survey data)
errors = np.array([2, 3, 2, 3, 4, 3, 3, 2, 2, 3, 2, 3])

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each category with error bars
ax.errorbar(months, appetizers_scores, yerr=errors, label='Appetizers', 
            marker='o', capsize=5, linestyle='-', color='tab:blue', alpha=0.8)
ax.errorbar(months, main_courses_scores, yerr=errors, label='Main Courses', 
            marker='s', capsize=5, linestyle='--', color='tab:orange', alpha=0.8)
ax.errorbar(months, desserts_scores, yerr=errors, label='Desserts', 
            marker='^', capsize=5, linestyle='-.', color='tab:green', alpha=0.8)
ax.errorbar(months, beverages_scores, yerr=errors, label='Beverages', 
            marker='D', capsize=5, linestyle=':', color='tab:red', alpha=0.8)
ax.errorbar(months, specials_scores, yerr=errors, label='Specials', 
            marker='P', capsize=5, linestyle='-', color='tab:purple', alpha=0.8)

# Titles and labels
ax.set_title('Evolving Gourmet Trends: Customer Satisfaction\nAcross Five Culinary Categories in 2023', fontsize=14, weight='bold')
ax.set_xlabel('Months', fontsize=12)
ax.set_ylabel('Satisfaction Score (Out of 100)', fontsize=12)

# Legend
ax.legend(title="Culinary Categories", loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title_fontsize=11)

# Grid for better readability
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()