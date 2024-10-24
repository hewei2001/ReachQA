import matplotlib.pyplot as plt

# Satisfaction scores for different departments
engineering_scores = [7, 8, 9, 6, 7, 8, 7, 9, 8, 8, 6, 7, 8, 9, 7]
hr_scores = [5, 6, 5, 6, 5, 7, 5, 6, 6, 5, 6, 7, 6, 5, 6]
sales_scores = [6, 5, 6, 7, 8, 7, 6, 5, 7, 8, 7, 6, 5, 7, 6]
support_scores = [4, 5, 4, 5, 6, 4, 5, 4, 5, 6, 5, 4, 5, 4, 5]
marketing_scores = [7, 8, 7, 9, 8, 9, 8, 7, 8, 9, 8, 9, 7, 8, 8]

# Grouping the data together
department_scores = [engineering_scores, hr_scores, sales_scores, support_scores, marketing_scores]
departments = ['Engineering', 'HR', 'Sales', 'Customer Support', 'Marketing']

# Creating the horizontal box plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting
boxes = ax.boxplot(department_scores, vert=False, patch_artist=True, notch=True,
                   boxprops=dict(facecolor='lightblue', color='darkblue'),
                   whiskerprops=dict(color='darkblue', linestyle='-'),
                   capprops=dict(color='darkblue'),
                   flierprops=dict(marker='o', color='red', alpha=0.5),
                   medianprops=dict(color='darkred'))

# Customizing box colors for differentiation
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

# Customizing the plot
ax.set_yticklabels(departments)
ax.set_xlabel('Satisfaction Scores', fontsize=12, fontweight='bold')
ax.set_title('Employee Satisfaction Survey\nAcross Departments', fontsize=16, fontweight='bold', pad=20)

# Adding grid for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Adding annotations for special insights
ax.annotate('High satisfaction in Marketing', xy=(8.5, 5), xytext=(9, 4.8),
            arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10)

ax.annotate('Room for improvement in Support', xy=(5.5, 4), xytext=(6.5, 3.5),
            arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10)

# Adjust layout to fit the elements and avoid overlapping
plt.tight_layout()

# Show the plot
plt.show()