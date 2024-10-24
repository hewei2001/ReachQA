import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
technologies = [
    'Hyperloop Pods',
    'Electric Air Taxis',
    'Automated Bicycles',
    'Electric Scooters',
    'Solar-Powered Buses',
    'Maglev Trains'
]
adoption_percentages = [35, 25, 15, 10, 10, 5]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Define colors for the bars
colors = ['royalblue', 'mediumslateblue', 'cornflowerblue', 'lightsteelblue', 'lightskyblue', 'powderblue']

# Create the bar chart
bars = ax.barh(np.arange(len(technologies)), adoption_percentages, color=colors, edgecolor='darkgray')

# Add data annotations
for bar in bars:
    ax.annotate(f'{bar.get_width()}%', 
                 xy=(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2),
                 va='center', ha='left', color='black', fontsize=10, fontweight='bold')

# Set the title and labels
ax.set_title('Adoption of Futuristic Transportation Technologies\nin Neon Heights by 2040', fontsize=16, fontweight='bold', color='midnightblue')
ax.set_xlabel('Adoption Percentage (%)', fontsize=12)
ax.set_yticks(np.arange(len(technologies)))
ax.set_yticklabels(technologies, fontsize=12)

# Adding a grid for clarity
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Invert y-axis for a more visually appealing horizontal bar chart
ax.invert_yaxis()

# Adjust the layout to avoid clipping of labels
plt.tight_layout()

# Display the plot
plt.show()