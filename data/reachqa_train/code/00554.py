import matplotlib.pyplot as plt
import numpy as np

# Define the data for the bar chart
departments = ['Engineering', 'Design', 'Marketing', 'Sales', 'HR', 'Customer Support']
engagement_scores = [7.8, 6.5, 8.2, 7.1, 9.0, 6.8]
average_score = np.mean(engagement_scores)

# Define related data for the line plot (e.g., quarterly trend of engagement scores)
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
trend_data = {
    'Engineering': [7.5, 7.6, 8.0, 7.8],
    'Design': [6.3, 6.4, 6.5, 6.5],
    'Marketing': [8.0, 8.1, 8.3, 8.2],
    'Sales': [6.9, 7.0, 7.2, 7.1],
    'HR': [8.9, 8.9, 9.1, 9.0],
    'Customer Support': [6.5, 6.7, 6.9, 6.8]
}

# Create the figure and 1x2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Plotting the bar chart
bars = ax1.bar(departments, engagement_scores, color=['#3498db', '#e74c3c', '#f1c40f', '#2ecc71', '#9b59b6', '#e67e22'], width=0.6)
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2.0, yval + 0.1, f'{yval:.1f}', ha='center', va='bottom', fontsize=11, color='black')
    annotation_color = 'darkgreen' if yval > average_score else 'red'
    annotation_text = 'Above Avg' if yval > average_score else 'Below Avg'
    ax1.text(bar.get_x() + bar.get_width() / 2.0, yval + 0.3, annotation_text, ha='center', va='bottom', fontsize=9, fontweight='bold', color=annotation_color)

ax1.set_title('Employee Engagement Scores\nby Department in 2023', fontsize=14, fontweight='bold')
ax1.set_xlabel('Department', fontsize=12)
ax1.set_ylabel('Engagement Score', fontsize=12)
ax1.axhline(y=average_score, color='gray', linestyle='--', linewidth=1, label=f'Company Average: {average_score:.1f}')
ax1.set_ylim(0, 10)
ax1.legend(loc='upper left', fontsize=11)
plt.sca(ax1)
plt.xticks(rotation=45, ha='right', fontsize=11)

# Plotting the line chart
for dept, scores in trend_data.items():
    ax2.plot(quarters, scores, marker='o', label=dept)

ax2.set_title('Quarterly Engagement Score Trends by Department', fontsize=14, fontweight='bold')
ax2.set_xlabel('Quarter', fontsize=12)
ax2.set_ylabel('Engagement Score', fontsize=12)
ax2.set_ylim(0, 10)
ax2.legend(loc='lower left', fontsize=10)
plt.sca(ax2)
plt.xticks(fontsize=11)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()