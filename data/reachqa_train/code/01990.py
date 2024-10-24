import matplotlib.pyplot as plt
import numpy as np

# Define companies and specializations
companies = ['TechNova', 'CodeCraft', 'AlgoSphere']
specializations = ['AI Research', 'Cybersecurity', 'Cloud Computing', 'Quantum Computing', 'Blockchain Development']

# Number of positions open for each specialization at each company
positions = np.array([
    [120, 80, 200, 50, 70],   # TechNova
    [150, 110, 170, 65, 90],  # CodeCraft
    [130, 95, 180, 75, 85]    # AlgoSphere
])

# Colors and markers for each company
colors = ['red', 'green', 'blue']
markers = ['o', 's', 'D']

# Create the scatter plot
plt.figure(figsize=(12, 8))

# Plot each company's data
for i, company in enumerate(companies):
    # Extract x and y data for the company
    x_positions = np.arange(len(specializations)) + i * 0.2  # Slight offset for clarity
    y_positions = positions[i]

    # Scatter plot with distinct marker and color
    plt.scatter(x_positions, y_positions, color=colors[i], marker=markers[i],
                s=150, edgecolor='black', alpha=0.75, label=company)

# Add x-ticks for specializations
plt.xticks(ticks=np.arange(len(specializations)), labels=specializations, fontsize=10)

# Title and labels
plt.title('Tech Giants\' Hiring Focus in 2050\nAcross Various Computer Science Specializations', fontsize=16, fontweight='bold')
plt.xlabel('Specializations', fontsize=12)
plt.ylabel('Number of Positions Open', fontsize=12)

# Grid and legend
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper right', title='Companies', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()