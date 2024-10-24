import matplotlib.pyplot as plt
import numpy as np

# Years of the study
years = np.array([2015, 2016, 2017, 2018, 2019, 2020])

# Average number of books read per person for each genre
sci_fi = np.array([10, 11, 13, 12, 15, 14])
mystery = np.array([8, 9, 10, 9, 11, 10])
fantasy = np.array([12, 13, 14, 13, 15, 16])
historical_fiction = np.array([7, 8, 9, 8, 10, 9])

# Define standard deviations for error bars
errors = {
    "Sci-Fi": np.array([1, 0.8, 1.2, 0.9, 1.1, 0.7]),
    "Mystery": np.array([0.5, 0.4, 0.6, 0.5, 0.7, 0.3]),
    "Fantasy": np.array([1, 0.9, 1.3, 1.1, 1.5, 1.2]),
    "Historical Fiction": np.array([0.4, 0.3, 0.5, 0.4, 0.6, 0.2]),
}

# Colors for each genre
colors = ['#8c564b', '#1f77b4', '#2ca02c', '#ff7f0e']

# Create the line chart with error bars
fig, ax = plt.subplots(figsize=(12, 7))

# Plot each genre's data with error bars
ax.errorbar(years, sci_fi, yerr=errors["Sci-Fi"], label='Sci-Fi', color=colors[0], fmt='-o', capsize=5, alpha=0.8)
ax.errorbar(years, mystery, yerr=errors["Mystery"], label='Mystery', color=colors[1], fmt='-s', capsize=5, alpha=0.8)
ax.errorbar(years, fantasy, yerr=errors["Fantasy"], label='Fantasy', color=colors[2], fmt='-^', capsize=5, alpha=0.8)
ax.errorbar(years, historical_fiction, yerr=errors["Historical Fiction"], label='Historical Fiction', color=colors[3], fmt='-d', capsize=5, alpha=0.8)

# Customize the plot
ax.set_title("Literary Trends in Litville:\n2015-2020", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Average Number of Books Read per Person", fontsize=14)
ax.set_xticks(years)
ax.legend(title='Genres', fontsize=12, loc='upper left')

# Adding grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()