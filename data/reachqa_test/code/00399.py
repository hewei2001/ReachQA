import matplotlib.pyplot as plt
import numpy as np

# Define the data for the bar chart
companies = ["Apple", "Samsung", "IBM", "Microsoft", "Google", "Intel", "Qualcomm"]
patents_filed = [74, 85, 78, 52, 58, 60, 55]  # Patents filed in thousands
patent_positions = np.arange(len(companies))

# Generate a distinct color palette
colors = plt.cm.tab10(np.linspace(0, 1, len(companies)))

# Create a figure and a single subplot with increased width for longer labels
fig, ax = plt.subplots(figsize=(16, 9))

# Plot the bar chart
bars = ax.bar(patent_positions, patents_filed, color=colors, edgecolor='black', linewidth=1.2)

# Function to add labels on top of the bars with automatic adjustment for readability
def add_labels(bars, alignment='center', va='bottom'):
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 2, yval, ha=alignment, va=va, rotation=0,
                fontweight='bold', fontsize=12)

add_labels(bars)

# Set the x-axis tick labels and adjust rotation to avoid overlapping
ax.set_xticks(patent_positions)
ax.set_xticklabels(companies, rotation=45, ha='right')

# Add a baseline
ax.axhline(y=np.mean(patents_filed), color='r', linestyle='--', label='Average Patents')

# Set the title and labels for the axes
plt.title("Patent Powerhouses: \nThe 2023 Patent Filing Landscape \nAmong Global Tech Giants")
plt.xlabel("Technology Companies")
plt.ylabel("Patents Filed (in thousands)")

# Add grid for the y-axis to improve readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add a legend for the baseline
ax.legend()

# Automatically adjust the layout for better visibility
plt.tight_layout()

# Show the plot
plt.show()