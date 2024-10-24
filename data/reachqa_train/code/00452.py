import matplotlib.pyplot as plt
import numpy as np

# Define industry sectors and corresponding AI adoption levels for 2030
sectors = ['Healthcare', 'Finance', 'Manufacturing', 'Retail', 'Education', 'Transportation']
adoption_levels_2030 = [85, 75, 65, 55, 45, 35]  # AI Adoption levels in 2030

# Define initial AI adoption levels in 2020 for line plot overlay
adoption_levels_2020 = [40, 50, 30, 25, 20, 15]  # AI Adoption levels in 2020

# Create the combined bar and line chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Define colors for the bars
bar_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Plot bar chart for 2030 data
bars = ax1.bar(sectors, adoption_levels_2030, color=bar_colors, alpha=0.8, width=0.6, label='2030 AI Adoption')

# Add data annotations on top of each bar
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 3),
                 textcoords="offset points", ha='center', va='bottom', fontsize=10, color='black')

# Create a secondary y-axis for the line plot
ax2 = ax1.twinx()

# Define line plot style
line_color = '#17becf'
line_style = '--'

# Plot line chart for 2020 data
ax2.plot(sectors, adoption_levels_2020, color=line_color, linestyle=line_style, marker='o', linewidth=2,
         label='2020 AI Adoption')

# Annotate line chart points
for i, txt in enumerate(adoption_levels_2020):
    ax2.annotate(f'{txt}%', (sectors[i], adoption_levels_2020[i]), textcoords="offset points", xytext=(0, 10),
                 ha='center', fontsize=10, color=line_color)

# Customize axes labels and title
ax1.set_xlabel('Industry Sectors', fontsize=12)
ax1.set_ylabel('2030 AI Adoption Level (%)', fontsize=12, color=bar_colors[0])
ax2.set_ylabel('2020 AI Adoption Level (%)', fontsize=12, color=line_color)
ax1.set_title('Comparative AI Adoption in Various Industry Sectors\n2020 vs 2030', fontsize=16, fontweight='bold', pad=20)

# Rotate x-axis labels to avoid overlap
plt.xticks(rotation=30, ha='right')

# Add gridlines to the primary y-axis
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Add a legend that combines both plots
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=12)

# Adjust layout to accommodate annotations and labels
plt.tight_layout()

# Display the plot
plt.show()