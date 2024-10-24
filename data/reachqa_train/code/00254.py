import matplotlib.pyplot as plt
import numpy as np

# Define the case types and corresponding resolved case counts
case_types = ['Contract Disputes', 'Employment Law', 'Intellectual Property', 'Corporate Compliance', 'Family Law']
cases_resolved = [120, 85, 50, 95, 60]
colors = ['#6fa3ef', '#f76f8e', '#8ed372', '#ffcc66', '#9d66cc']

# Imagine additional data for average resolution time in days
resolution_time = [30, 45, 60, 50, 40]

# Create a figure with two subplots (1 row, 2 columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# First subplot: Bar Chart for Resolved Cases
bars = ax1.bar(case_types, cases_resolved, color=colors, edgecolor='black')
ax1.set_title("Legal Department's Case Resolution by Type\n2022 Snapshot", fontsize=14, fontweight='bold')
ax1.set_xlabel('Type of Case', fontsize=12)
ax1.set_ylabel('Number of Cases Resolved', fontsize=12)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Annotate bars with the resolved case counts
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points",
                 ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

plt.xticks(rotation=15, ha='right', fontsize=10)

# Second subplot: Pie Chart for Distribution of Resolved Cases
ax2.pie(cases_resolved, labels=case_types, autopct='%1.1f%%', colors=colors, startangle=140)
ax2.set_title("Distribution of Cases Resolved\nby Type as Percentage", fontsize=14, fontweight='bold')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()