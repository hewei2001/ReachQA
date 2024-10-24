import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import uniform_filter1d

# Years from 2010 to 2019
years = np.arange(2010, 2020)

# Enrollment data for each academic field
computer_science_enrollments = np.array([150, 170, 190, 220, 250, 280, 310, 340, 370, 400])
mechanical_engineering_enrollments = np.array([130, 135, 140, 150, 160, 165, 170, 180, 185, 190])
psychology_enrollments = np.array([200, 195, 210, 205, 220, 225, 230, 240, 235, 245])
art_history_enrollments = np.array([90, 88, 85, 83, 82, 80, 78, 75, 74, 73])

# Error values for enrollments
cs_errors = np.array([5, 10, 10, 15, 15, 15, 20, 20, 20, 25])
me_errors = np.array([5, 5, 10, 10, 15, 15, 15, 15, 10, 15])
psyc_errors = np.array([10, 10, 10, 10, 15, 15, 15, 10, 15, 10])
art_errors = np.array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])

# Calculate the average enrollments across fields for overlay
average_enrollments = (
    computer_science_enrollments + 
    mechanical_engineering_enrollments + 
    psychology_enrollments + 
    art_history_enrollments
) / 4

# Initialize plot
fig, ax = plt.subplots(figsize=(16, 9))

# Plot each field with error bars
ax.errorbar(years, computer_science_enrollments, yerr=cs_errors, fmt='-o', capsize=5,
             color='#1f77b4', label='Computer Science', linewidth=2)
ax.errorbar(years, mechanical_engineering_enrollments, yerr=me_errors, fmt='-s', capsize=5,
             color='#ff7f0e', label='Mechanical Engineering', linewidth=2)
ax.errorbar(years, psychology_enrollments, yerr=psyc_errors, fmt='-^', capsize=5,
             color='#2ca02c', label='Psychology', linewidth=2)
ax.errorbar(years, art_history_enrollments, yerr=art_errors, fmt='-d', capsize=5,
             color='#d62728', label='Art History', linewidth=2)

# Overlay average enrollments
smooth_averages = uniform_filter1d(average_enrollments, size=3)  # Moving average for smoothing
ax.plot(years, smooth_averages, 'k--', label='Average Enrollment (Smoothed)', linewidth=2)

# Annotations for specific years
for i in range(len(years)):
    if i % 3 == 0:  # Just an example pattern to not clutter
        ax.annotate(f'{average_enrollments[i]:.0f}', (years[i], average_enrollments[i] + 5),
                    textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8, color='darkred')

# Customize the plot
ax.set_title('Enrollment Trends Over a Decade\nAcross Various Academic Fields', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Enrollments', fontsize=12)
ax.set_xticks(years)
ax.set_yticks(np.arange(70, 450, 50))
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='upper left', fontsize=10, title='Academic Fields & Trend', frameon=True)

# Adjust plot to fit elements without overlap
plt.tight_layout()

# Show plot
plt.show()