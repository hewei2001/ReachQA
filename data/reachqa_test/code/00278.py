import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Ages of participants (in years)
ages = np.array([15, 18, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

# Preference scores for each genre across age groups
fantasy_scores = np.array([90, 85, 80, 75, 70, 60, 55, 50, 45, 40, 35, 30, 25])
mystery_scores = np.array([30, 35, 40, 45, 55, 60, 70, 75, 80, 85, 90, 85, 80])
historical_fiction_scores = np.array([20, 25, 30, 40, 50, 60, 70, 80, 85, 90, 80, 75, 70])

# Average reading hours per week for each age group
reading_hours = np.array([5, 6, 7, 7, 8, 8, 9, 9, 8, 7, 6, 5, 4])

# Create the figure and axes
fig, ax1 = plt.subplots(figsize=(14, 8))

# Scatter and smooth line for Fantasy
ax1.scatter(ages, fantasy_scores, color='purple', label='Fantasy', alpha=0.6)
fantasy_spline = make_interp_spline(ages, fantasy_scores, k=3)
age_range = np.linspace(ages.min(), ages.max(), 300)
ax1.plot(age_range, fantasy_spline(age_range), color='purple', linestyle='-', linewidth=2)

# Scatter and smooth line for Mystery
ax1.scatter(ages, mystery_scores, color='orange', label='Mystery', alpha=0.6)
mystery_spline = make_interp_spline(ages, mystery_scores, k=3)
ax1.plot(age_range, mystery_spline(age_range), color='orange', linestyle='-', linewidth=2)

# Scatter and smooth line for Historical Fiction
ax1.scatter(ages, historical_fiction_scores, color='green', label='Historical Fiction', alpha=0.6)
historical_spline = make_interp_spline(ages, historical_fiction_scores, k=3)
ax1.plot(age_range, historical_spline(age_range), color='green', linestyle='-', linewidth=2)

# Set titles and labels
ax1.set_title('Age and Genre Preference Trends\nwith Average Reading Hours', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Age of Participants', fontsize=12)
ax1.set_ylabel('Preference Score', fontsize=12)

# Add a secondary axis for the bar chart
ax2 = ax1.twinx()
ax2.bar(ages, reading_hours, width=1.5, color='grey', alpha=0.3, label='Avg Reading Hours', edgecolor='black')
ax2.set_ylabel('Average Reading Hours/Week', fontsize=12, color='grey')

# Configure the legend
ax1.legend(loc='upper left', title='Genre')
ax2.legend(loc='upper right', title='Reading Hours')

# Add grid
ax1.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()