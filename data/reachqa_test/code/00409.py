import matplotlib.pyplot as plt
import numpy as np

# Enhanced data with subcategories and more survey scores for each century
enhanced_data = {
    '15th Century': {'overall': [82, 85, 81, 80, 83], 'accommodation': [75, 78, 74, 76, 78], 'landscape': [90, 92, 88, 91, 89]},
    '16th Century': {'overall': [86, 87, 88, 84, 89], 'accommodation': [78, 80, 79, 82, 81], 'landscape': [92, 94, 93, 90, 92]},
    '17th Century': {'overall': [80, 83, 78, 82, 81], 'accommodation': [72, 75, 70, 74, 73], 'landscape': [85, 88, 84, 87, 86]},
    '18th Century': {'overall': [84, 87, 86, 89, 85], 'accommodation': [76, 79, 78, 81, 77], 'landscape': [88, 91, 90, 93, 89]},
    '19th Century': {'overall': [87, 89, 90, 88, 92], 'accommodation': [80, 82, 83, 81, 84], 'landscape': [90, 92, 94, 91, 93]},
    '20th Century': {'overall': [90, 92, 93, 91, 95], 'accommodation': [84, 86, 87, 85, 88], 'landscape': [94, 96, 97, 95, 98]},
    '21st Century': {'overall': [92, 93, 94, 92, 96], 'accommodation': [86, 88, 89, 87, 90], 'landscape': [96, 98, 99, 97, 100]},
}

centuries = list(enhanced_data.keys())
mean_overall_scores = [np.mean(scores['overall']) for scores in enhanced_data.values()]
mean_accom_scores = [np.mean(scores['accommodation']) for scores in enhanced_data.values()]
mean_landscape_scores = [np.mean(scores['landscape']) for scores in enhanced_data.values()]
years = np.arange(1, len(centuries) + 1)

# Compute standard deviations for error bars
std_overall_scores = [np.std(scores['overall']) for scores in enhanced_data.values()]
std_accom_scores = [np.std(scores['accommodation']) for scores in enhanced_data.values()]
std_landscape_scores = [np.std(scores['landscape']) for scores in enhanced_data.values()]

# Plotting
plt.figure(figsize=(12, 8))
plt.errorbar(years, mean_overall_scores, yerr=std_overall_scores, marker='o', linestyle='-', color='darkblue', linewidth=2, label='Mean Overall Satisfaction', capsize=4)
plt.errorbar(years, mean_accom_scores, yerr=std_accom_scores, marker='s', linestyle='--', color='darkred', linewidth=2, label='Mean Accommodation Satisfaction', capsize=4)
plt.errorbar(years, mean_landscape_scores, yerr=std_landscape_scores, marker='^', linestyle='-.', color='darkgreen', linewidth=2, label='Mean Landscape Satisfaction', capsize=4)

# Annotate data points
for i in range(len(mean_overall_scores)):
    plt.annotate(f'{mean_overall_scores[i]:.1f}%', (years[i], mean_overall_scores[i]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(f'{mean_accom_scores[i]:.1f}%', (years[i], mean_accom_scores[i]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(f'{mean_landscape_scores[i]:.1f}%', (years[i], mean_landscape_scores[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Customizing plot elements
plt.title("Tourist Satisfaction Over Historical Centuries\nComparing Overall, Accommodation, and Landscape Satisfaction", fontweight="bold", fontsize=14)
plt.xlabel("Century", fontsize=12)
plt.ylabel("Mean Satisfaction (%)", fontsize=12)
plt.xticks(years, centuries, rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc="lower right")

# Adjusting layout to avoid overlaps
plt.tight_layout()

# Display the plot
plt.show()