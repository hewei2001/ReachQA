import matplotlib.pyplot as plt
import numpy as np

# Years covered in the study
years = np.array(['2018', '2019', '2020', '2021', '2022', '2023'])

# Total meditation hours annually
meditation_hours = np.array([120, 140, 160, 200, 220, 250])

# Self-reported emotional well-being scores (out of 100)
wellbeing_scores = np.array([65, 70, 75, 82, 88, 90])

# Initialize the plot
plt.figure(figsize=(12, 6))

# Plotting the line chart
plt.plot(years, wellbeing_scores, '-o', color='#2ca02c', label='Emotional Well-being Score', linewidth=2, markersize=8)

# Add title and labels
plt.title('Annual Meditation Practice Hours and Their Impact on Emotional Well-being\nComprehensive Study from 2018 to 2023', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Well-being Score (0 to 100)', fontsize=12)

# Customize x-ticks
plt.xticks(years)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Add legend
plt.legend(loc='lower right', fontsize=10)

# Adding annotations for significant changes
plt.annotate('New Techniques Introduced', xy=('2020', 75), xytext=('2019', 80),
             arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=10, color='blue')

plt.annotate('Peak in Consistency', xy=('2023', 90), xytext=('2021', 85),
             arrowprops=dict(facecolor='purple', arrowstyle='->'), fontsize=10, color='purple')

# Annotate each data point with its value
for i, (year, score) in enumerate(zip(years, wellbeing_scores)):
    plt.text(year, score + 1, f'{score}', fontsize=9, ha='center', va='bottom', color='black')

# Ensure the layout fits well without overlap
plt.tight_layout()

# Show plot
plt.show()