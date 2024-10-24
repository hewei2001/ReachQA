import numpy as np
import matplotlib.pyplot as plt

# Years for the x-axis
years = np.arange(2015, 2024)

# Virtual Reality User Estimates (in millions)
gaming_users = np.array([5, 8, 15, 22, 30, 40, 50, 60, 75])
education_users = np.array([1, 2, 5, 10, 20, 30, 40, 50, 65])
healthcare_users = np.array([0.5, 1, 3, 6, 12, 18, 24, 30, 40])
corporate_users = np.array([0.2, 0.5, 1, 3, 5, 10, 15, 20, 30])

# Calculate percentage growth for each category
gaming_growth = np.diff(gaming_users) / gaming_users[:-1] * 100
education_growth = np.diff(education_users) / education_users[:-1] * 100
healthcare_growth = np.diff(healthcare_users) / healthcare_users[:-1] * 100
corporate_growth = np.diff(corporate_users) / corporate_users[:-1] * 100

# Adjust years for growth
growth_years = years[1:]

# Error margins (standard deviation for each category)
gaming_error = np.array([1, 1, 2, 2, 3, 4, 5, 5, 7])
education_error = np.array([0.2, 0.2, 0.5, 1, 2, 2, 3, 4, 5])
healthcare_error = np.array([0.1, 0.2, 0.5, 1, 2, 3, 4, 5, 5])
corporate_error = np.array([0.05, 0.1, 0.2, 0.5, 1, 1.5, 2, 2.5, 3])

# Plot setup
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Line plot with error bars
ax1.errorbar(years, gaming_users, yerr=gaming_error, label='Gaming', 
             marker='o', linestyle='-', color='blue', capsize=5, alpha=0.8)
ax1.errorbar(years, education_users, yerr=education_error, label='Education', 
             marker='s', linestyle='--', color='green', capsize=5, alpha=0.8)
ax1.errorbar(years, healthcare_users, yerr=healthcare_error, label='Healthcare', 
             marker='^', linestyle=':', color='red', capsize=5, alpha=0.8)
ax1.errorbar(years, corporate_users, yerr=corporate_error, label='Corporate Training', 
             marker='d', linestyle='-.', color='purple', capsize=5, alpha=0.8)

# Titles and labels for the line plot
ax1.set_title("Evolution of Virtual Reality Experiences\n(2015-2023)", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Number of Users (in millions)", fontsize=14)
ax1.set_xticks(years)
ax1.set_ylim(0, 80)
ax1.legend(loc='upper left')
ax1.grid(True, linestyle='--', alpha=0.7)

# Bar plot for percentage growth
ax2.bar(growth_years, gaming_growth, width=0.2, label='Gaming', color='blue', align='center', alpha=0.7)
ax2.bar(growth_years + 0.2, education_growth, width=0.2, label='Education', color='green', align='center', alpha=0.7)
ax2.bar(growth_years + 0.4, healthcare_growth, width=0.2, label='Healthcare', color='red', align='center', alpha=0.7)
ax2.bar(growth_years + 0.6, corporate_growth, width=0.2, label='Corporate Training', color='purple', align='center', alpha=0.7)

# Titles and labels for the bar plot
ax2.set_title("Yearly Growth Rate of Virtual Reality Users", fontsize=16, fontweight='bold')
ax2.set_xlabel("Year", fontsize=14)
ax2.set_ylabel("Percentage Growth (%)", fontsize=14)
ax2.set_xticks(growth_years + 0.3)
ax2.set_ylim(0, max(max(gaming_growth), max(education_growth), 
                    max(healthcare_growth), max(corporate_growth)) + 10)
ax2.legend(loc='upper left')
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout for better visibility
plt.tight_layout()
plt.show()