import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.arange(2010, 2021)
primary_schools = np.array([5, 8, 12, 16, 20, 25, 30, 36, 45, 55, 60])
secondary_schools = np.array([10, 15, 22, 28, 35, 42, 50, 58, 65, 72, 78])
higher_education = np.array([20, 28, 37, 45, 52, 60, 67, 75, 82, 88, 92])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting the stacked area chart
ax.fill_between(years, primary_schools, label='Primary Schools', color='lightblue', alpha=0.7)
ax.fill_between(years, primary_schools, secondary_schools, label='Secondary Schools', color='lightgreen', alpha=0.7)
ax.fill_between(years, secondary_schools, higher_education, label='Higher Education', color='lightcoral', alpha=0.7)

# Add titles and labels
ax.set_title('Digital Transformation of Education:\nAdoption of Digital Tools (2010-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Adoption of Digital Tools (%)', fontsize=12)

# Customize x-axis ticks
ax.set_xticks(years)
ax.set_xticklabels([str(year) for year in years], rotation=45)

# Add a grid to improve readability
ax.grid(linestyle='--', alpha=0.5)

# Add a legend to distinguish between areas
ax.legend(loc='upper left', fontsize=10)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()