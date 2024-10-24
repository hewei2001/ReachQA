import matplotlib.pyplot as plt
import numpy as np

# Define the data
departments = ['Engineering', 'Design', 'Marketing', 'Sales', 'HR', 'Customer Support']
engagement_scores = [7.8, 6.5, 8.2, 7.1, 9.0, 6.8]

# Calculate the average score for annotation
average_score = np.mean(engagement_scores)

# Create the figure and axis with a larger figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the bar chart
bars = ax.bar(departments, engagement_scores, color=['#3498db', '#e74c3c', '#f1c40f', '#2ecc71', '#9b59b6', '#e67e22'], width=0.6)

# Add data annotation above the bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2.0, yval + 0.1, f'{yval:.1f}', 
            ha='center', va='bottom', fontsize=11, color='black')

# Highlight departments with scores above average in bold
for i, score in enumerate(engagement_scores):
    annotation_color = 'darkgreen' if score > average_score else 'red'
    annotation_text = 'Above Avg' if score > average_score else 'Below Avg'
    ax.text(bars[i].get_x() + bars[i].get_width() / 2.0, score + 0.3, annotation_text, 
            ha='center', va='bottom', fontsize=9, fontweight='bold', color=annotation_color)

# Customize the plot with title and labels
ax.set_title('Employee Engagement Scores\nby Department in 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Department', fontsize=12)
ax.set_ylabel('Engagement Score', fontsize=12)
ax.axhline(y=average_score, color='gray', linestyle='--', linewidth=1, label=f'Company Average: {average_score:.1f}')

# Adjust the y-axis limit
ax.set_ylim(0, 10)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=11)

# Add legend
ax.legend(loc='upper left', fontsize=11)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()