import matplotlib.pyplot as plt
import numpy as np

# Data for the chart: Global Usage of Programming Languages in 2023
languages = ['Python', 'JavaScript', 'Java', 'C#', 'Ruby', 'Go', 'Others']
usage_percentages = [28, 23, 16, 12, 8, 5, 8]

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Bar positions
x_pos = np.arange(len(languages))

# Create the bar chart
bars = ax.bar(x_pos, usage_percentages, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2'], width=0.6)

# Customize the plot
ax.set_title("Global Usage of Programming Languages\nin 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Programming Languages", fontsize=12)
ax.set_ylabel("Usage Percentage (%)", fontsize=12)
ax.set_ylim(0, 35)
ax.set_xticks(x_pos)
ax.set_xticklabels(languages, rotation=45, ha='right', fontsize=10)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Annotate percentage values on each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%', 
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Offset to avoid overlap with the bar
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, color='black')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Show the plot
plt.show()