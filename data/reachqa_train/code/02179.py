import matplotlib.pyplot as plt

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

# Create a vertical box plot with custom styling
plt.figure(figsize=(12, 7))
box = plt.boxplot(
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
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Enhance plot details
plt.title("Tech Haven: \nSalary Distribution across Tech Roles in 2023", fontsize=14, fontweight='bold', pad=20)
plt.ylabel('Salary in USD', fontsize=12)
plt.xlabel('Tech Roles', fontsize=12)

# Add grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to ensure no overlap
plt.tight_layout()

# Display the plot
plt.show()