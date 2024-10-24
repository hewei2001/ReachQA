import numpy as np
import matplotlib.pyplot as plt

# Elements and their corresponding usage frequency in the lab
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 
            'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']
usage_frequency = [150, 20, 85, 50, 70, 160, 130, 180, 25, 60]

# Define colors for the histogram bars
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Set the figure size
plt.figure(figsize=(14, 7))

# Plotting the histogram with customized bin edges
plt.bar(elements, usage_frequency, color=colors, edgecolor='black', alpha=0.75)

# Add titles and labels
plt.title('Frequency of Common Laboratory Elements', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Element', fontsize=12, labelpad=10)
plt.ylabel('Usage Frequency', fontsize=12, labelpad=10)

# Add grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Customize the tick labels
plt.xticks(rotation=45, fontsize=11, ha='right')
plt.yticks(fontsize=11)

# Annotate bars with frequency values above the bars
for i, frequency in enumerate(usage_frequency):
    plt.text(i, frequency + 5, str(frequency), ha='center', va='bottom', fontsize=11, fontweight='bold')

# Automatically adjust the layout to prevent text from overlapping
plt.tight_layout()

# Display the histogram
plt.show()