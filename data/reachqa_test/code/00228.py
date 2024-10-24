import matplotlib.pyplot as plt
import numpy as np

# Modified productivity data (output units per week)
tech_productivity = [75, 80, 82, 78, 85, 90, 88, 95, 70, 77, 92]
finance_productivity = [65, 70, 68, 72, 75, 74, 69, 73, 71, 76]
healthcare_productivity = [58, 60, 65, 63, 62, 68, 67, 59, 61, 64]
retail_productivity = [50, 52, 55, 51, 53, 58, 56, 54, 57, 60]
education_productivity = [60, 63, 61, 65, 66, 64, 62, 67, 68, 69]

# Constructing a secondary dataset for overlay (e.g., industry growth rates)
tech_growth = [5, 7, 6, 8, 6, 9, 7, 6, 4, 5, 6]
finance_growth = [3, 4, 4, 5, 5, 4, 3, 4, 3, 5]
healthcare_growth = [2, 3, 3, 4, 3, 5, 4, 3, 4, 3]
retail_growth = [1, 2, 2, 2, 3, 4, 3, 2, 3, 2]
education_growth = [4, 5, 4, 5, 5, 4, 3, 5, 6, 5]

# Combine the productivity data into a list
productivity_data = [
    tech_productivity,
    finance_productivity,
    healthcare_productivity,
    retail_productivity,
    education_productivity
]

# Combine the growth data into a list
growth_data = [
    np.mean(tech_growth),
    np.mean(finance_growth),
    np.mean(healthcare_growth),
    np.mean(retail_growth),
    np.mean(education_growth)
]

# Industry labels
industries = ['Technology', 'Finance', 'Healthcare', 'Retail', 'Education']

# Set up the figure and axes
fig, ax1 = plt.subplots(figsize=(14, 8))

# Create the horizontal box plot
boxprops = dict(linestyle='-', linewidth=2, color='darkblue')
medianprops = dict(color='firebrick', linewidth=2)
ax1.boxplot(productivity_data, vert=False, patch_artist=True, notch=True,
           boxprops=boxprops, medianprops=medianprops,
           whiskerprops=dict(color='darkblue', linewidth=1.5),
           capprops=dict(color='darkblue', linewidth=1.5),
           flierprops=dict(marker='o', color='darkblue', alpha=0.6),
           widths=0.6)

# Color the boxes
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightgoldenrodyellow', 'lightpink']
for patch, color in zip(ax1.artists, colors):
    patch.set_facecolor(color)

# Customize the y-axis with industry names
ax1.set_yticklabels(industries)

# Set the title and axis labels
ax1.set_title('Remote Work Productivity and Industry Growth\nAnalysis Across Different Industries', 
              fontsize=16, fontweight='bold', loc='left')
ax1.set_xlabel('Productivity (Output Units per Week)', fontsize=13)
ax1.set_ylabel('Industries', fontsize=13)

# Adding a secondary y-axis for industry growth rates
ax2 = ax1.twiny()
ax2.plot(growth_data, range(1, len(industries) + 1), 's-', color='purple', label='Avg. Growth Rate (%)')
ax2.set_xlabel('Average Growth Rate (%)', fontsize=13, color='purple')
ax2.tick_params(axis='x', colors='purple')
ax2.legend(loc='upper right', fontsize=10)

# Add grid lines for better readability
ax1.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to ensure everything fits without overlap
plt.tight_layout()

# Show the plot
plt.show()