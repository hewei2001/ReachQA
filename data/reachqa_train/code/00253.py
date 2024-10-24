import matplotlib.pyplot as plt
import numpy as np

# Define the case types and corresponding resolved case counts
case_types = ['Contract Disputes', 'Employment Law', 'Intellectual Property', 'Corporate Compliance', 'Family Law']
cases_resolved = [120, 85, 50, 95, 60]

# Define a color scheme for the bars
colors = ['#6fa3ef', '#f76f8e', '#8ed372', '#ffcc66', '#9d66cc']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Plot the bar chart
bars = ax.bar(case_types, cases_resolved, color=colors, edgecolor='black')

# Annotate the bars with the resolved case counts
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Offset text by 3 points above the bar
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# Title and labels
ax.set_title("Legal Department's Case Resolution by Type: 2022 Snapshot", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Type of Case', fontsize=12)
ax.set_ylabel('Number of Cases Resolved', fontsize=12)

# Improve layout
plt.xticks(rotation=15, ha='right', fontsize=10)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()