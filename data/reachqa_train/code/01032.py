import matplotlib.pyplot as plt
import numpy as np

# Define departments and their corresponding engagement scores
departments = ['Software Development', 'Marketing', 'Customer Support', 'Human Resources', 'Finance']
engagement_scores = [75, 82, 68, 90, 78]

# Calculate positions for the bars
x_pos = np.arange(len(departments))

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting the bar chart
bars = ax.bar(x_pos, engagement_scores, color=['#4a90e2', '#50e3c2', '#b8e986', '#f8e71c', '#7ed321'], width=0.6)

# Adding data labels above bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Adding title and labels
ax.set_title("Annual Employee Engagement Scores\nAcross Departments in 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Departments", fontsize=12)
ax.set_ylabel("Engagement Score (%)", fontsize=12)
ax.set_ylim(0, 100)

# Customizing the layout
plt.xticks(x_pos, departments, rotation=30, ha='right', fontsize=11)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Ensure layout is optimal and readable
plt.tight_layout()

# Display the plot
plt.show()