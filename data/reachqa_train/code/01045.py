import matplotlib.pyplot as plt
import numpy as np

# Constructing sample satisfaction data for each department (on a scale of 0 to 10)
engineering_scores = np.array([8, 7, 9, 6, 7, 9, 8, 8, 6, 7, 7, 8, 9, 5, 9])
marketing_scores = np.array([7, 6, 5, 8, 6, 7, 7, 5, 6, 8, 9, 6, 5, 7, 6])
sales_scores = np.array([6, 5, 5, 7, 6, 4, 5, 6, 4, 5, 5, 7, 8, 5, 5])
hr_scores = np.array([9, 8, 9, 9, 8, 9, 10, 8, 9, 8, 10, 9, 9, 8, 10])
it_support_scores = np.array([5, 6, 5, 6, 5, 5, 5, 6, 6, 5, 6, 6, 5, 5, 4])

# Combine data into a list
data = [engineering_scores, marketing_scores, sales_scores, hr_scores, it_support_scores]

# Labels for each department
labels = ['Engineering', 'Marketing', 'Sales', 'HR', 'IT Support']

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Create the box plot
box = ax.boxplot(data, patch_artist=True, labels=labels, notch=True, vert=True)

# Customizing the box plot
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set properties for whiskers, caps, and medians
plt.setp(box['whiskers'], color='black', linestyle='--')
plt.setp(box['caps'], color='black')
plt.setp(box['medians'], color='red', linewidth=2)

# Adding title and labels
ax.set_title('Employee Satisfaction by Department\nInnovatech Solutions Annual Survey', fontsize=16, fontweight='bold')
ax.set_ylabel('Satisfaction Score (0-10)', fontsize=12)

# Customizing the grid
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.5)
ax.set_xticklabels(labels, rotation=45, fontsize=10)

# Annotate HR satisfaction
ax.annotate('Notably High\nSatisfaction in HR', xy=(4, 10), xytext=(3.5, 9.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='right', va='bottom')

# Tight layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()