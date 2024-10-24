import matplotlib.pyplot as plt
import numpy as np

# Years of observation
years = np.arange(2010, 2020)

# Hypothetical data for the popularity of languages (on a scale from 0 to 100)
python_popularity = np.array([50, 55, 60, 65, 70, 78, 85, 90, 93, 97])
javascript_popularity = np.array([60, 63, 67, 70, 72, 75, 78, 80, 82, 85])
java_popularity = np.array([80, 78, 75, 72, 70, 68, 67, 66, 65, 64])

# Hypothetical data for job postings mentioning each language over the years
python_jobs = np.array([30, 40, 45, 50, 55, 65, 72, 78, 85, 90])
javascript_jobs = np.array([35, 38, 40, 42, 45, 48, 52, 55, 58, 60])
java_jobs = np.array([60, 58, 57, 55, 53, 50, 48, 47, 46, 45])

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Line plot for language popularity
axs[0].plot(years, python_popularity, label='Python', color='tab:blue', marker='o', linewidth=2.5)
axs[0].plot(years, javascript_popularity, label='JavaScript', color='tab:green', marker='^', linewidth=2.5)
axs[0].plot(years, java_popularity, label='Java', color='tab:red', marker='s', linewidth=2.5)
axs[0].set_xlabel('Year', fontsize=10)
axs[0].set_ylabel('Popularity Index', fontsize=10)
axs[0].set_title('Programming Language Popularity\n(2010-2019)', fontsize=12)
axs[0].grid(True, linestyle='--', alpha=0.5)
axs[0].legend(loc='lower left', fontsize=9)

# Bar plot for job postings
width = 0.25
x_indexes = np.arange(len(years))
axs[1].bar(x_indexes - width, python_jobs, width=width, label='Python', color='tab:blue', alpha=0.7)
axs[1].bar(x_indexes, javascript_jobs, width=width, label='JavaScript', color='tab:green', alpha=0.7)
axs[1].bar(x_indexes + width, java_jobs, width=width, label='Java', color='tab:red', alpha=0.7)
axs[1].set_xlabel('Year', fontsize=10)
axs[1].set_ylabel('Job Postings (in thousands)', fontsize=10)
axs[1].set_title('Job Postings for Programming Languages\n(2010-2019)', fontsize=12)
axs[1].set_xticks(x_indexes)
axs[1].set_xticklabels(years)
axs[1].legend(loc='upper right', fontsize=9)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()