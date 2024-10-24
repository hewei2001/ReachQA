import matplotlib.pyplot as plt
import numpy as np

# Define the green spaces and their data
green_spaces = ['Central Park', 'Riverside Park', 'Community Garden', 'Botanical Garden', 'Urban Trail']
monthly_visitors = [120, 90, 70, 60, 80]  # in thousands
satisfaction_ratings = [8.5, 8.0, 9.0, 8.8, 7.5]  # Current satisfaction ratings
months = np.arange(1, 13)  # Representing months

# Construct synthetic satisfaction rating trends over 12 months
satisfaction_trends = {
    'Central Park': [8.0, 8.2, 8.3, 8.5, 8.4, 8.6, 8.8, 8.7, 8.9, 8.9, 8.8, 8.5],
    'Riverside Park': [8.0, 8.1, 8.0, 8.0, 8.2, 8.4, 8.3, 8.2, 8.1, 8.2, 8.1, 8.0],
    'Community Garden': [8.9, 9.0, 9.1, 9.2, 9.1, 9.3, 9.4, 9.3, 9.4, 9.3, 9.2, 9.0],
    'Botanical Garden': [8.5, 8.6, 8.7, 8.8, 8.8, 8.9, 9.0, 9.0, 8.9, 8.9, 8.8, 8.8],
    'Urban Trail': [7.4, 7.5, 7.6, 7.7, 7.5, 7.6, 7.7, 7.7, 7.6, 7.8, 7.7, 7.5]
}

# Set up the figure and subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))

# Bar Plot for Monthly Visitors
ax1 = axes[0]
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']
bars = ax1.bar(green_spaces, monthly_visitors, color=colors, alpha=0.8)
for bar, rating in zip(bars, satisfaction_ratings):
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 3, f'{yval}', ha='center', va='bottom', fontsize=10)
    ax1.text(bar.get_x() + bar.get_width() / 2, yval - 12, f'Sat: {rating}', ha='center', va='bottom', fontsize=9, color='darkgreen')

ax1.set_xlabel('Types of Urban Green Spaces')
ax1.set_ylabel('Average Monthly Visitors (in thousands)')
ax1.set_title('Visitor Data and Satisfaction\nin Greenfield City', fontweight='bold', pad=10)
ax1.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Line Plot for Satisfaction Trends
ax2 = axes[1]
for park, trend in satisfaction_trends.items():
    ax2.plot(months, trend, marker='o', label=park)

ax2.set_xlabel('Months')
ax2.set_ylabel('Satisfaction Rating')
ax2.set_title('Satisfaction Rating Trends Over a Year', fontweight='bold', pad=10)
ax2.legend(loc='lower left')
ax2.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# General configuration
plt.xticks(rotation=30, ha='right')
plt.tight_layout()

# Display the plots
plt.show()