import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

# Data for weekly study hours and corresponding GPA
study_hours = np.array([5, 8, 12, 15, 18, 22, 26, 30, 35, 40, 45, 50])
gpa_study = np.array([2.1, 2.3, 2.5, 2.7, 3.0, 3.1, 3.4, 3.5, 3.7, 3.8, 3.9, 4.0])

# Additional data: Weekly extracurricular hours and its effect on GPA
extracurricular_hours = np.array([2, 3, 4, 5, 3, 2, 1, 3, 4, 5, 3, 2])
gpa_extra = np.array([2.0, 2.1, 2.2, 2.5, 2.6, 2.5, 2.7, 2.9, 3.0, 3.2, 3.1, 3.3])

# Create the main plot
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot scatter and polynomial fit for study hours vs. GPA
ax1.scatter(study_hours, gpa_study, color='blue', label='Study Data Points', alpha=0.7, edgecolors='black')
p_study = Polynomial.fit(study_hours, gpa_study, deg=3)
fit_line_study = p_study.linspace(n=100, domain=[0, 55])
ax1.plot(fit_line_study[0], fit_line_study[1], color='orange', label='Study Trend Line', linewidth=2, linestyle='--')

# Setting titles and labels
ax1.set_title('Impact of Study and Extracurricular Hours on GPA\nAnalysis of Academic Performance', fontsize=16)
ax1.set_xlabel('Study Hours per Week', fontsize=14)
ax1.set_ylabel('GPA (Study Impact)', fontsize=14, color='blue')

# Add a secondary y-axis for extracurricular data
ax2 = ax1.twinx()
ax2.bar(study_hours, gpa_extra, color='green', label='Extracurricular GPA Impact', alpha=0.3, width=1.5)
ax2.set_ylabel('GPA (Extracurricular Impact)', fontsize=14, color='green')

# Legends and grid
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.85), fontsize=12, frameon=False)
ax1.grid(True, linestyle='--', alpha=0.5)

# Adjust plot layout
plt.xlim(0, 55)
ax1.set_ylim(2, 4.1)
ax2.set_ylim(1.8, 3.5)
fig.tight_layout()

# Show the plot
plt.show()