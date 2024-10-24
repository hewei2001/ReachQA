import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Artificial data for programming language usage in percentages
python = np.array([10, 15, 20, 25, 30, 40, 50, 55, 60, 65, 70])
javascript = np.array([30, 35, 40, 50, 55, 60, 60, 62, 65, 68, 70])
java = np.array([50, 45, 40, 35, 30, 25, 20, 20, 18, 17, 15])
csharp = np.array([5, 5, 5, 6, 7, 8, 8, 10, 12, 13, 15])
ruby = np.array([5, 5, 5, 5, 5, 7, 9, 8, 5, 4, 3])

# Calculate bottom positions for stacking
bottom_js = python
bottom_java = bottom_js + javascript
bottom_csharp = bottom_java + java
bottom_ruby = bottom_csharp + csharp

# Create a stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Stack bars with transparency
ax.bar(years, python, label='Python', color='#306998', width=0.6, alpha=0.8)
ax.bar(years, javascript, bottom=bottom_js, label='JavaScript', color='#F7DF1E', width=0.6, alpha=0.8)
ax.bar(years, java, bottom=bottom_java, label='Java', color='#b07219', width=0.6, alpha=0.8)
ax.bar(years, csharp, bottom=bottom_csharp, label='C#', color='#178600', width=0.6, alpha=0.8)
ax.bar(years, ruby, bottom=bottom_ruby, label='Ruby', color='#701516', width=0.6, alpha=0.8)

# Title and labels
ax.set_title('The Rise of Programming Languages in Tech Startups\n(2010-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Usage Percentage', fontsize=12)

# Customizing legend
ax.legend(loc='upper left', title='Programming Languages', fontsize=10, title_fontsize='12')

# Adjust x-axis labels for better readability
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha="right")

# Adding grid lines
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent text cutoff
plt.tight_layout()

# Display the plot
plt.show()