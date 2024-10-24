import matplotlib.pyplot as plt
import numpy as np

# Data preparation
disciplines = ['Quantum Physics', 'Genetics', 'Artificial Intelligence', 'Climate Science']
funding_percentages = [25, 20, 35, 20]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting a horizontal bar chart
bars = ax.barh(disciplines, funding_percentages, color=colors, edgecolor='black')

# Adding labels to each bar
ax.bar_label(bars, labels=[f'{p}%' for p in funding_percentages], label_type='edge', padding=3)

# Set labels and title
ax.set_xlabel('Percentage of Total Funding (%)', fontsize=12)
ax.set_title('Research Funding Distribution Across Key Scientific Disciplines\nNIFR Annual Report', 
             fontsize=14, fontweight='bold')

# Customize the x-axis to clearly show 0-100%
ax.set_xlim(0, 50)

# Annotate each discipline with a brief description
descriptions = [
    "Exploring the quantum realm",
    "Decoding the blueprint of life",
    "Innovating intelligent solutions",
    "Combating climate change"
]

for bar, desc in zip(bars, descriptions):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, desc,
            va='center', ha='left', fontsize=10, color='grey')

# Improve the layout
plt.tight_layout()

# Display the plot
plt.show()