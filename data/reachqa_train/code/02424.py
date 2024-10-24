import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.arange(2010, 2021)
average_sales = np.array([5, 5.8, 6.5, 7.0, 7.6, 8.3, 9.1, 10.2, 11.0, 12.5, 14.0])
sales_variability = np.array([0.3, 0.4, 0.35, 0.5, 0.45, 0.6, 0.5, 0.55, 0.6, 0.65, 0.7])

# Plot creation
fig, ax = plt.subplots(figsize=(12, 7))
ax.errorbar(years, average_sales, yerr=sales_variability, fmt='-o', color='#D9534F', ecolor='#FFADAD', 
            elinewidth=2, capsize=4, label='Average Sales with Variability')

# Axes titles
ax.set_title("The Renaissance of Board Games: Sales Trends and Variability\nfrom 2010 to 2020", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Sales (in millions)", fontsize=12)

# Grid and legend
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left', fontsize=11)

# Fill between for variability
ax.fill_between(years, average_sales - sales_variability, average_sales + sales_variability, 
                color='#FFCCCC', alpha=0.3)

# Annotation
ax.annotate('Major Game Release',
            xy=(2018, 11.0), 
            xytext=(2016, 13.5),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=10, 
            ha='center',
            backgroundcolor='w')

# Layout adjustment
plt.tight_layout()

# Show plot
plt.show()