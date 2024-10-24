import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Define the years and mock average scores with standard deviation
years = np.arange(2010, 2020)
average_scores = [75, 77, 76, 78, 79, 80, 82, 81, 83, 85]
score_std_dev = [3, 2, 4, 3, 5, 3, 4, 2, 3, 4]
student_count = [300, 320, 330, 310, 340, 345, 360, 355, 370, 380]

# Creating the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Primary line chart with error bars
ax1.errorbar(
    years, average_scores, yerr=score_std_dev, fmt='-o', color='navy',
    ecolor='orange', elinewidth=2, capsize=5, capthick=2, markerfacecolor='white',
    label='Average Mathematics Score'
)

# Regression line for mathematics scores
X = years.reshape(-1, 1)
y = np.array(average_scores)
model = LinearRegression().fit(X, y)
trend_line = model.predict(X)
ax1.plot(years, trend_line, color='green', linestyle='--', linewidth=1.5, label='Score Trend Line')

# Second y-axis for the bar chart of student count
ax2 = ax1.twinx()
ax2.bar(years, student_count, color='lightblue', alpha=0.5, label='Student Count', width=0.5)

# Adding plot details
ax1.set_title('Evolution of Student Performance in Mathematics\nand Student Participation Over a Decade', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Average Score', fontsize=12, color='navy')
ax2.set_ylabel('Student Count', fontsize=12, color='lightblue')

ax1.set_xticks(years)
ax1.set_yticks(np.arange(70, 90, 2))
ax2.set_yticks(np.arange(200, 450, 50))

ax1.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.5)
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Annotation for key insights
ax1.annotate(
    'New Curriculum Introduced', xy=(2014, 79), xytext=(2011, 83),
    arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkred'
)

# Setting limits for better visualization
ax1.set_xlim(2009, 2020)
ax1.set_ylim(70, 90)
ax2.set_ylim(200, 450)

# Final layout adjustment and display
plt.tight_layout()
plt.show()