import matplotlib.pyplot as plt
import numpy as np

# Define the tech roles and corresponding salary data
roles = ['Software Engineers', 'Data Scientists', 'Product Managers', 'UX Designers', 'Cybersecurity Experts']

# Construct the salary data for each role
salaries = [
    [80000, 85000, 90000, 95000, 105000, 110000, 115000, 125000, 135000, 145000, 150000],
    [90000, 95000, 100000, 110000, 115000, 120000, 125000, 135000, 145000, 155000, 160000],
    [95000, 100000, 110000, 120000, 125000, 135000, 145000, 155000, 165000, 170000, 175000],
    [70000, 75000, 80000, 90000, 95000, 100000, 105000, 115000, 120000, 125000, 130000],
    [85000, 90000, 95000, 100000, 105000, 115000, 125000, 135000, 140000, 145000, 150000]
]

# Calculate mean salaries for the bar chart
mean_salaries = [np.mean(s) for s in salaries]

# Create a figure with two subplots side by side
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Box Plot (Original)
box = axes[0].boxplot(
    salaries, 
    vert=True, 
    patch_artist=True, 
    labels=roles,
    notch=True,
    boxprops=dict(facecolor='lightblue', color='blue', linewidth=1.5),
    medianprops=dict(color='red', linewidth=1.5),
    whiskerprops=dict(color='blue', linewidth=1.2),
    capprops=dict(color='blue', linewidth=1.2)
)

# Apply custom colors to each box to improve distinction
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

axes[0].set_title("Tech Haven: \nSalary Distribution Across Tech Roles in 2023", fontsize=14, fontweight='bold', pad=15)
axes[0].set_ylabel('Salary in USD', fontsize=12)
axes[0].set_xlabel('Tech Roles', fontsize=12)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Bar Chart (New)
bars = axes[1].bar(roles, mean_salaries, color=colors, alpha=0.7)
axes[1].set_title("Average Salary Across Tech Roles", fontsize=14, fontweight='bold', pad=15)
axes[1].set_ylabel('Average Salary in USD', fontsize=12)
axes[1].set_xlabel('Tech Roles', fontsize=12)

# Add value labels on the bar chart
for bar in bars:
    yval = bar.get_height()
    axes[1].text(bar.get_x() + bar.get_width()/2, yval + 500, int(yval), ha='center', va='bottom', fontsize=10, fontweight='bold')

# Adjust layout to ensure no overlap
plt.tight_layout()

# Display the plot
plt.show()