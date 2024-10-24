import matplotlib.pyplot as plt
import numpy as np

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

# Initialize plot
plt.figure(figsize=(14, 8))

# Plot each field with error bars
plt.errorbar(years, computer_science_enrollments, yerr=cs_errors, fmt='-o', capsize=5,
             color='#1f77b4', label='Computer Science', linewidth=2)
plt.errorbar(years, mechanical_engineering_enrollments, yerr=me_errors, fmt='-s', capsize=5,
             color='#ff7f0e', label='Mechanical Engineering', linewidth=2)
plt.errorbar(years, psychology_enrollments, yerr=psyc_errors, fmt='-^', capsize=5,
             color='#2ca02c', label='Psychology', linewidth=2)
plt.errorbar(years, art_history_enrollments, yerr=art_errors, fmt='-d', capsize=5,
             color='#d62728', label='Art History', linewidth=2)

# Customize the plot
plt.title('Enrollment Trends Over a Decade\nAcross Various Academic Fields', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Enrollments', fontsize=12)
plt.xticks(years)
plt.yticks(np.arange(70, 450, 50))
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', fontsize=10, title='Academic Fields', frameon=True)

# Adjust plot to fit elements without overlap
plt.tight_layout()

# Show plot
plt.show()