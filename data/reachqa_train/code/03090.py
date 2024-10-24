import matplotlib.pyplot as plt
import numpy as np

# Define the fictional universities and disciplines
universities = ['Nova University', 'Athena College', 'Legacy Institute', 'Wisdom Academy', "Scholars' Corner"]
disciplines = ['History', 'Philosophy', 'Literature', 'Linguistics', 'Archaeology', 'Art History']

# Academic intensity scores for each discipline at each university
data = np.array([
    [85, 70, 95, 60, 50, 65],  # Nova University
    [70, 90, 80, 75, 65, 60],  # Athena College
    [60, 85, 60, 90, 75, 70],  # Legacy Institute
    [80, 60, 70, 85, 90, 50],  # Wisdom Academy
    [75, 75, 85, 80, 55, 95]   # Scholars' Corner
])

# Create the plot
plt.figure(figsize=(12, 8))
heatmap = plt.imshow(data, cmap='YlGnBu', interpolation='nearest', aspect='auto')

# Add a color bar with label
cbar = plt.colorbar(heatmap)
cbar.set_label('Academic Intensity Score', fontsize=12)

# Set x and y ticks with labels
plt.xticks(ticks=np.arange(len(disciplines)), labels=disciplines, rotation=45, ha='right', fontsize=11)
plt.yticks(ticks=np.arange(len(universities)), labels=universities, fontsize=11)

# Set title with a line break for better readability
plt.title('Academic Landscape of Humanities Studies\nAcross Global Universities', fontsize=16, fontweight='bold')

# Annotate each cell with the corresponding score
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        plt.text(j, i, f'{data[i, j]}', ha='center', va='center', color='black', fontsize=11)

# Automatic layout adjustment
plt.tight_layout()

# Display the plot
plt.show()