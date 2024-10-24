import matplotlib.pyplot as plt
import numpy as np

# Define the cities and years
cities = ['New York', 'London', 'Tokyo', 'Sydney', 'São Paulo']
years = np.arange(2010, 2020)

# Create UCRI scores for each city over the years
ucri_scores = np.array([
    [68, 70, 72, 75, 77, 80, 83, 85, 86, 88],  # New York
    [65, 67, 69, 72, 74, 76, 78, 80, 82, 84],  # London
    [74, 76, 77, 78, 80, 82, 83, 85, 87, 90],  # Tokyo
    [70, 73, 75, 78, 81, 84, 86, 87, 88, 90],  # Sydney
    [60, 62, 64, 66, 68, 70, 72, 73, 75, 77]   # São Paulo
])

# Plotting the heat map
fig, ax = plt.subplots(figsize=(10, 8))
cax = ax.imshow(ucri_scores, cmap='YlGn', aspect='auto')

# Adding labels and title
ax.set_xticks(np.arange(len(years)))
ax.set_yticks(np.arange(len(cities)))
ax.set_xticklabels(years)
ax.set_yticklabels(cities)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('City', fontsize=12)
ax.set_title('Urban Climate Resilience Index:\nCity Preparedness for Climate Change', fontsize=14, fontweight='bold')

# Rotate the year labels to avoid overlap
plt.xticks(rotation=45)

# Create color bar
cbar = fig.colorbar(cax)
cbar.set_label('UCRI Score', fontsize=12)

# Annotate each cell with the numerical value
for i in range(len(cities)):
    for j in range(len(years)):
        ax.text(j, i, ucri_scores[i, j], va='center', ha='center', color='black', fontsize=10)

# Adjust layout for better visualization
plt.tight_layout()

# Display the plot
plt.show()