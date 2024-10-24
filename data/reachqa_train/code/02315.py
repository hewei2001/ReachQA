import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.array([2015, 2016, 2017, 2018, 2019, 2020])
sci_fi = np.array([10, 11, 13, 12, 15, 14])
mystery = np.array([8, 9, 10, 9, 11, 10])
fantasy = np.array([12, 13, 14, 13, 15, 16])
historical_fiction = np.array([7, 8, 9, 8, 10, 9])

errors = {
    "Sci-Fi": np.array([1, 0.8, 1.2, 0.9, 1.1, 0.7]),
    "Mystery": np.array([0.5, 0.4, 0.6, 0.5, 0.7, 0.3]),
    "Fantasy": np.array([1, 0.9, 1.3, 1.1, 1.5, 1.2]),
    "Historical Fiction": np.array([0.4, 0.3, 0.5, 0.4, 0.6, 0.2]),
}

# New related dataset for dual axis plot
literacy_rate = np.array([92, 93, 93.5, 94, 95, 95.5])

colors = ['#8c564b', '#1f77b4', '#2ca02c', '#ff7f0e']

# Create the main plot
fig, ax1 = plt.subplots(figsize=(14, 8))

ax2 = ax1.twinx()  # Create a second y-axis

# Plot each genre with enhancements
ax1.errorbar(years, sci_fi, yerr=errors["Sci-Fi"], label='Sci-Fi', color=colors[0], fmt='-o', capsize=5, alpha=0.8)
ax1.errorbar(years, mystery, yerr=errors["Mystery"], label='Mystery', color=colors[1], fmt='-s', capsize=5, alpha=0.8)
ax1.errorbar(years, fantasy, yerr=errors["Fantasy"], label='Fantasy', color=colors[2], fmt='-^', capsize=5, alpha=0.8)
ax1.errorbar(years, historical_fiction, yerr=errors["Historical Fiction"], label='Historical Fiction', color=colors[3], fmt='-d', capsize=5, alpha=0.8)

# Plot literacy rate on the secondary axis
ax2.plot(years, literacy_rate, label='Literacy Rate (%)', color='darkgrey', linestyle='--', marker='x', linewidth=2, alpha=0.7)

# Enhance layout
ax1.set_title("Literary Trends in Litville: 2015-2020\nWith Literacy Rate Influence", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Avg. Books Read per Person", fontsize=14)
ax2.set_ylabel("Literacy Rate (%)", fontsize=14, color='darkgrey')

# Annotate peak in Fantasy
peak_year = years[np.argmax(fantasy)]
peak_value = fantasy.max()
ax1.annotate(f'Peak: {peak_value} books', xy=(peak_year, peak_value), xytext=(peak_year, peak_value+1),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, backgroundcolor='white')

# Customize legend
ax1.legend(title='Genres', fontsize=12, loc='upper left', frameon=False)
ax2.legend(loc='upper right', frameon=False)

# Add grid for readability
ax1.grid(True, linestyle='--', alpha=0.6)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()