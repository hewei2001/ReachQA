import matplotlib.pyplot as plt
import numpy as np

# Data preparation
disciplines = ['Quantum Physics', 'Genetics', 'Artificial Intelligence', 'Climate Science']
funding_percentages = [25, 20, 35, 20]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Historical or Projected Data for the Line Plot
# Assume past 3-year funding increase as percentages
growth_percentages = [
    [5, 10, 15],  # Quantum Physics
    [7, 8, 9],    # Genetics
    [10, 15, 20], # Artificial Intelligence
    [3, 5, 7]     # Climate Science
]
years = ['2019', '2020', '2021']

# Create the plot with an additional y-axis for the line plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting a horizontal bar chart
bars = ax1.barh(disciplines, funding_percentages, color=colors, edgecolor='black')
ax1.bar_label(bars, labels=[f'{p}%' for p in funding_percentages], label_type='edge', padding=3)
ax1.set_xlabel('Percentage of Total Funding (%)', fontsize=12)
ax1.set_xlim(0, 50)

# Annotate each discipline with a brief description
descriptions = [
    "Exploring the quantum realm",
    "Decoding the blueprint of life",
    "Innovating intelligent solutions",
    "Combating climate change"
]
for bar, desc in zip(bars, descriptions):
    ax1.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, desc,
             va='center', ha='left', fontsize=10, color='grey')

# Create a secondary y-axis for the line plot
ax2 = ax1.twinx()
for i, discipline_growth in enumerate(growth_percentages):
    ax2.plot(years, discipline_growth, marker='o', label=disciplines[i], color=colors[i])
ax2.set_ylabel('Annual Funding Increase (%)', fontsize=12)

# Add a legend to the plot
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2)

# Set the title and subtitle
ax1.set_title('Research Funding Distribution and Annual Growth\nNIFR Annual Report',
              fontsize=14, fontweight='bold', loc='center')
ax2.set_title('Historical Funding Growth (2019-2021)', fontsize=12, loc='right')

# Adjust layout to prevent overlap
fig.tight_layout()

# Display the plot
plt.show()