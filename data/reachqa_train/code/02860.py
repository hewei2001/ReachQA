import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2015, 2026)

# Adoption rates of online learning in different education levels
elementary = [5, 6, 7, 9, 12, 15, 18, 22, 25, 28, 30]
secondary = [7, 9, 11, 14, 17, 21, 25, 30, 35, 38, 40]
higher_education = [10, 13, 16, 20, 24, 29, 35, 40, 45, 50, 55]
vocational = [4, 5, 6, 8, 10, 13, 16, 20, 24, 27, 30]
adult_education = [3, 4, 6, 9, 12, 16, 20, 25, 30, 35, 40]

# Aggregate data for stacking
data = np.array([elementary, secondary, higher_education, vocational, adult_education])

# Colors for each educational level
colors = ['#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the stacked area chart
ax.stackplot(years, data, labels=['Elementary', 'Secondary', 'Higher Education', 'Vocational', 'Adult Education'],
             colors=colors, alpha=0.8)

# Set the title and axis labels
ax.set_title('Global Educational Trends:\nOnline Learning Adoption Rates (2015-2025)', fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Adoption Rate (%)', fontsize=12)

# Add legend outside the plot area
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Education Levels', fontsize=10)

# Annotate significant changes or insights directly on the plot
ax.annotate('Significant increase in Higher Education', xy=(2020, 90), xytext=(2016, 110),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='center')

# Add grid lines for improved readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust the layout to fit all elements
plt.tight_layout(rect=[0, 0, 0.9, 1])  # Adjust right side to make space for legend

# Display the plot
plt.show()