import matplotlib.pyplot as plt
import numpy as np

# Satisfaction scores for each department
technology_scores = [7, 8, 6, 9, 8, 7, 9, 8, 8, 7, 10, 8, 7, 6, 8]
marketing_scores = [5, 6, 7, 5, 6, 6, 7, 6, 6, 5, 5, 7, 6, 8, 5]
sales_scores = [6, 7, 6, 5, 8, 7, 6, 5, 6, 7, 5, 8, 6, 7, 6]
finance_scores = [8, 9, 8, 9, 7, 8, 8, 7, 9, 9, 8, 7, 9, 8, 8]
hr_scores = [9, 10, 9, 8, 9, 10, 8, 9, 8, 9, 10, 9, 9, 8, 9]

# Aggregate the data into a list for plotting
scores = [technology_scores, marketing_scores, sales_scores, finance_scores, hr_scores]
departments = ['Technology', 'Marketing', 'Sales', 'Finance', 'Human Resources']

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the horizontal box plot
box = ax.boxplot(scores, vert=False, patch_artist=True, notch=True, whis=1.5, 
                 boxprops=dict(facecolor="lightblue", color="navy"),
                 whiskerprops=dict(color="navy"),
                 capprops=dict(color="navy"),
                 flierprops=dict(marker="o", color="red", alpha=0.5),
                 medianprops=dict(color="darkorange"))

# Add titles and labels
ax.set_title("Employee Satisfaction Across Different Departments\nA Corporate Firm's Insight", fontsize=16, fontweight='bold')
ax.set_xlabel("Satisfaction Score", fontsize=12)
ax.set_yticklabels(departments, fontsize=12)
ax.set_xlim(0, 11)

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()