import matplotlib.pyplot as plt
import numpy as np

# Salary data (in thousands of dollars) for each role
software_engineers = [70, 85, 100, 120, 150, 180, 210, 220, 230, 250]
data_scientists = [80, 95, 110, 130, 140, 150, 165, 180, 190, 205]
product_managers = [60, 75, 95, 105, 125, 145, 155, 165, 175, 190]
ux_designers = [55, 65, 80, 90, 105, 115, 130, 140, 160, 175]

# Combine the data into a list for boxplotting
salary_data = [software_engineers, data_scientists, product_managers, ux_designers]

# Define the roles for the x-axis
roles = ['Software Engineers', 'Data Scientists', 'Product Managers', 'UX Designers']

# Create the box plot
plt.figure(figsize=(12, 8))
box = plt.boxplot(salary_data, patch_artist=True, labels=roles, notch=True, vert=True, flierprops=dict(markerfacecolor='r', marker='o'))

# Set colors for the boxes
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels with optimal alignment
plt.title("Tech Industry Salaries by Role\nin 2023", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Role", fontsize=12)
plt.ylabel("Salary (in $1000)", fontsize=12)

# Annotate the median salary values above each box
for i, role_data in enumerate(salary_data, start=1):
    med_val = np.median(role_data)
    plt.text(i, med_val + 1, f'{med_val:.1f}k', ha='center', va='bottom', fontweight='bold', fontsize=10)

# Add grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent label and title overlap
plt.tight_layout()

# Display the plot
plt.show()