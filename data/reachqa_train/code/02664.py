import matplotlib.pyplot as plt
import numpy as np

# Extended Data Setup (2000-2020)
years = np.arange(2000, 2021)

# Constructed data arrays for different categories
primary_schools = np.array([2, 3, 4, 6, 8, 12, 14, 16, 18, 20, 22, 24, 26, 30, 35, 40, 45, 50, 55, 60, 65])
secondary_schools = primary_schools + np.array([3, 4, 5, 6, 8, 10, 12, 14, 16, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75])
higher_education = secondary_schools + np.array([5, 6, 7, 8, 10, 12, 14, 16, 18, 22, 28, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])
vocational_training = higher_education + np.array([1, 2, 3, 4, 6, 7, 8, 10, 12, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the stacked area chart
ax.fill_between(years, primary_schools, label='Primary Schools', color='lightblue', alpha=0.7)
ax.fill_between(years, primary_schools, secondary_schools, label='Secondary Schools', color='lightgreen', alpha=0.7)
ax.fill_between(years, secondary_schools, higher_education, label='Higher Education', color='lightcoral', alpha=0.7)
ax.fill_between(years, higher_education, vocational_training, label='Vocational Training', color='wheat', alpha=0.7)

# Title and labels
ax.set_title('Digital Transformation of Education (2000-2020):\nAdoption of Digital Tools Across Different Education Levels', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Adoption of Digital Tools (%)', fontsize=12)

# Customize x-axis ticks
ax.set_xticks(years[::2])  # Show every second year
ax.set_xticklabels([str(year) for year in years[::2]], rotation=45, ha='right')

# Grid for readability
ax.grid(linestyle='--', alpha=0.5)

# Legend
ax.legend(loc='upper left', fontsize=10)

# Cumulative Total Line Plot (as a secondary view)
ax.plot(years, vocational_training, label='Total Adoption', color='black', linestyle='--', linewidth=2)

# Layout adjustment
plt.tight_layout()

# Display the plot
plt.show()