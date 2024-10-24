import matplotlib.pyplot as plt
import numpy as np

# Data for job postings (in thousands) and average salary (in thousands)
years = np.array([1980, 1990, 2000, 2010, 2020])
c_job_postings = [150, 120, 100, 70, 60]      
java_job_postings = [20, 60, 120, 100, 90]    
python_job_postings = [5, 10, 30, 70, 150]    
javascript_job_postings = [0, 5, 20, 50, 160] 
cpp_job_postings = [80, 70, 60, 50, 40]       

# Average salary data (in thousands)
c_salary = [70, 80, 90, 95, 100]
java_salary = [60, 65, 80, 85, 90]
python_salary = [50, 55, 70, 90, 120]
javascript_salary = [45, 50, 65, 75, 130]
cpp_salary = [65, 70, 75, 80, 85]

# Create figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Plotting job postings
ax1.plot(years, c_job_postings, marker='o', label='C', color='blue', linestyle='--', linewidth=2)
ax1.plot(years, java_job_postings, marker='o', label='Java', color='green', linestyle='-', linewidth=2)
ax1.plot(years, python_job_postings, marker='o', label='Python', color='orange', linestyle='-.', linewidth=2)
ax1.plot(years, javascript_job_postings, marker='o', label='JavaScript', color='red', linestyle=':', linewidth=2)
ax1.plot(years, cpp_job_postings, marker='o', label='C++', color='purple', linestyle='-', linewidth=2)

# Setting title and labels for the first plot
ax1.set_title("Evolution of Programming Languages:\nJob Postings Over the Decades", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Job Postings (in thousands)", fontsize=12)
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 170, 20))
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(title="Programming Languages", fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))

# Plotting average salary
ax2.plot(years, c_salary, marker='o', label='C', color='blue', linestyle='--', linewidth=2)
ax2.plot(years, java_salary, marker='o', label='Java', color='green', linestyle='-', linewidth=2)
ax2.plot(years, python_salary, marker='o', label='Python', color='orange', linestyle='-.', linewidth=2)
ax2.plot(years, javascript_salary, marker='o', label='JavaScript', color='red', linestyle=':', linewidth=2)
ax2.plot(years, cpp_salary, marker='o', label='C++', color='purple', linestyle='-', linewidth=2)

# Setting title and labels for the second plot
ax2.set_title("Average Salary Trends:\nProgramming Languages (1980-2020)", fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Average Salary (in thousands)", fontsize=12)
ax2.set_xticks(years)
ax2.set_yticks(np.arange(0, 130, 10))
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend(title="Programming Languages", fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()