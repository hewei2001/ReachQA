import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ['18-24', '25-34', '35-44', '45-54', '55+']
platforms = ['Coursera', 'Udemy', 'edX', 'Pluralsight', 'LinkedIn Learning']
data = np.array([
    [30, 25, 20, 15, 10],
    [25, 30, 20, 15, 10],
    [20, 25, 25, 15, 15],
    [15, 20, 30, 20, 15],
    [10, 15, 25, 25, 25]
])

# Additional data for the secondary plot
demographic_data = np.array([
    [40, 30, 20, 10, 0],
    [30, 40, 20, 10, 0],
    [20, 30, 40, 10, 0],
    [10, 20, 30, 40, 0],
    [0, 10, 20, 30, 40]
])

# Create a figure and axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8), gridspec_kw={'width_ratios': [3, 1]})

# Bar chart for market share
bar_width = 0.15
x_positions = np.arange(len(age_groups))

for i, platform in enumerate(platforms):
    ax1.bar(x_positions + i * bar_width, data[i], width=bar_width, label=platform, color=plt.cm.tab20(i / len(platforms)))

ax1.set_xlabel('Age Group')
ax1.set_ylabel('Market Share (%)')
ax1.set_title("Education in the Digital Age:\nOnline Learning Platforms' Market Share by Age Group", fontsize=16, fontweight='bold')

ax1.set_xticks(x_positions + bar_width * 2)
ax1.set_xticklabels(age_groups, rotation=45, ha='right', fontsize=10)

ax1.legend(loc='upper right', fontsize=12, bbox_to_anchor=(1.05, 1), ncol=1)

ax1.grid(axis='y', linestyle='--', alpha=0.5)

# Pie chart for demographic distribution
ax2.pie(demographic_data.sum(axis=0), labels=age_groups, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20(np.arange(len(age_groups)) / len(age_groups)))
ax2.set_title("Age Group Demographics", fontsize=14, fontweight='bold')

fig.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()