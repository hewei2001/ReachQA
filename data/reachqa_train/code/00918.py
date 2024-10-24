import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.arange(2013, 2024)
action_revenue = [6.5, 6.8, 7.2, 7.6, 8.0, 8.5, 8.8, 9.0, 9.5, 10.0, 10.5]
comedy_revenue = [5.2, 5.1, 5.0, 5.3, 5.6, 5.8, 5.9, 6.0, 6.2, 6.3, 6.5]
drama_revenue = [3.5, 3.6, 3.8, 4.0, 4.2, 4.4, 4.5, 4.7, 4.8, 5.0, 5.1]
sci_fi_revenue = [4.0, 4.2, 4.5, 5.0, 5.5, 6.0, 6.8, 7.5, 8.3, 8.8, 9.0]
horror_revenue = [2.5, 2.8, 2.9, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.5]

# Plot configuration
plt.figure(figsize=(14, 8))

# Enhanced color palette
colors = ['#FF5733', '#33C3FF', '#4CFF33', '#FF33F0', '#FFC133']

# Plot each genre with enhancements
plt.plot(years, action_revenue, marker='o', linewidth=2, linestyle='-', label='Action', color=colors[0])
plt.plot(years, comedy_revenue, marker='s', linewidth=2, linestyle='--', label='Comedy', color=colors[1])
plt.plot(years, drama_revenue, marker='^', linewidth=2, linestyle=':', label='Drama', color=colors[2])
plt.plot(years, sci_fi_revenue, marker='d', linewidth=2, linestyle='-.', label='Sci-Fi', color=colors[3])
plt.plot(years, horror_revenue, marker='x', linewidth=2, linestyle='-', label='Horror', color=colors[4])

# Highlighting 2023 data points
for revenue, color in zip([action_revenue, comedy_revenue, drama_revenue, sci_fi_revenue, horror_revenue], colors):
    plt.scatter([2023], [revenue[-1]], color=color, s=100, edgecolor='k', zorder=5)

# Titles and labels with better aesthetics
plt.title('Box Office Revenue Trends\nfor Different Film Genres (2013-2023)', fontsize=18, weight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Revenue (Billions $)', fontsize=14)

# Grid and axes adjustments
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(years, rotation=45, fontsize=10)
plt.yticks(np.arange(2, 12, 1), fontsize=10)

# Adding a legend
plt.legend(title='Film Genres', loc='upper left', fontsize=12, frameon=True)

# Annotations
plt.annotate('Highest Sci-Fi Revenue', xy=(2023, sci_fi_revenue[-1]), xytext=(2019, 9.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
plt.annotate('Action Surges Post-2019', xy=(2019, 8.5), xytext=(2016, 8),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()