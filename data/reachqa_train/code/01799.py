import matplotlib.pyplot as plt
import numpy as np

# Define the decades for the analysis
decades = np.array([1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])

# Popularity indices for each literary theme over the decades
romance_popularity = np.array([30, 40, 60, 70, 65, 55, 50, 45])
war_popularity = np.array([80, 70, 40, 20, 30, 35, 25, 15])
technology_popularity = np.array([10, 15, 20, 35, 60, 70, 80, 90])
nature_popularity = np.array([50, 45, 40, 60, 55, 50, 45, 40])
justice_popularity = np.array([20, 30, 45, 50, 60, 75, 85, 80])

# Error values for the popularity of themes (representing variability in data)
errors = {
    'Romance': np.array([5, 3, 4, 5, 4, 3, 5, 4]),
    'War': np.array([7, 5, 6, 4, 5, 6, 4, 3]),
    'Technology': np.array([3, 2, 4, 5, 4, 6, 5, 4]),
    'Nature': np.array([6, 5, 4, 5, 6, 5, 4, 3]),
    'Justice': np.array([5, 6, 4, 3, 5, 4, 3, 2])
}

# Plotting the data
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each theme with error bars
ax.errorbar(decades, romance_popularity, yerr=errors['Romance'], label='Romance', fmt='-o', color='#FF69B4', capsize=5, alpha=0.8)
ax.errorbar(decades, war_popularity, yerr=errors['War'], label='War', fmt='-^', color='#B22222', capsize=5, alpha=0.8)
ax.errorbar(decades, technology_popularity, yerr=errors['Technology'], label='Technology', fmt='-s', color='#4682B4', capsize=5, alpha=0.8)
ax.errorbar(decades, nature_popularity, yerr=errors['Nature'], label='Nature', fmt='-D', color='#32CD32', capsize=5, alpha=0.8)
ax.errorbar(decades, justice_popularity, yerr=errors['Justice'], label='Justice', fmt='-p', color='#FFD700', capsize=5, alpha=0.8)

# Customize the chart
ax.set_title('Evolution of Literary Themes in Award-Winning Novels\n1950-2020', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Popularity Index', fontsize=12)
ax.set_xticks(decades)
ax.set_yticks(range(0, 101, 10))
ax.set_xlim(1945, 2025)
ax.set_ylim(0, 100)
ax.legend(title='Themes', fontsize=10, loc='upper right', shadow=True)
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add contextual annotations
ax.annotate('Rise of Technology', xy=(2010, 80), xytext=(2000, 85),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='navy')
ax.annotate('Peak of War Theme', xy=(1950, 80), xytext=(1960, 85),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkred')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()