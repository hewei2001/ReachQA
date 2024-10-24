import matplotlib.pyplot as plt
import numpy as np

# Define the industries and years
industries = ['Finance', 'Pharma', 'Logistics', 'Cybersecurity', 'Manufacturing', 'Healthcare', 'Energy', 'Retail']
years = np.arange(2020, 2041)

# Artificial percentage data for each industry with exponential growth patterns
adoption_data = np.array([
    [5, 8, 12, 18, 25, 35, 45, 55, 65, 75, 85, 90, 92, 94, 95, 96, 97, 98, 99, 100, 100],  # Finance
    [3, 5, 10, 15, 22, 30, 40, 50, 60, 70, 80, 82, 84, 86, 88, 90, 91, 92, 93, 94, 95],  # Pharmaceuticals
    [2, 4, 7, 12, 18, 25, 33, 42, 52, 62, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92],   # Logistics
    [6, 10, 15, 23, 33, 45, 58, 68, 78, 85, 90, 92, 93, 94, 95, 96, 97, 98, 99, 100, 100], # Cybersecurity
    [1, 3, 5, 9, 15, 22, 30, 38, 48, 58, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88],     # Manufacturing
    [2, 4, 9, 14, 20, 29, 39, 50, 61, 73, 84, 86, 88, 90, 92, 94, 95, 96, 97, 98, 99],     # Healthcare
    [3, 6, 11, 16, 22, 32, 43, 55, 67, 78, 88, 90, 92, 93, 94, 95, 96, 97, 98, 99, 100],   # Energy
    [4, 8, 13, 18, 24, 34, 45, 58, 70, 82, 91, 93, 94, 95, 96, 97, 98, 99, 100, 100, 100]  # Retail
])

# Define colors for each industry
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFA833', '#33FFA5', '#FF8333', '#A833FF']

# Create the 3D bar chart
fig = plt.figure(figsize=(18, 10))
ax = fig.add_subplot(111, projection='3d')

# Define the positions for the bars
x_pos = np.arange(len(years))
y_pos = np.arange(len(industries))
x_pos, y_pos = np.meshgrid(x_pos, y_pos)
x_pos = x_pos.flatten()
y_pos = y_pos.flatten()
z_pos = np.zeros_like(x_pos)

# Define the bar dimensions
dx = dy = 0.5
dz = adoption_data.flatten()

# Plotting the bars
ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color=[colors[i // len(years)] for i in range(len(z_pos))], zsort='average')

# Set the axes labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Industry')
ax.set_zlabel('Adoption Rate (%)')
ax.set_title('Rise of Quantum Algorithms:\nA 3D Analysis of Industry Adoption (2020-2040)', pad=20)

# Set the ticks for the axes
ax.set_xticks(np.arange(len(years)) + dx / 2)
ax.set_yticks(np.arange(len(industries)) + dy / 2)
ax.set_xticklabels(years, rotation=45, ha='right')
ax.set_yticklabels(industries)

# Normalize the Z-axis to a 0-100 scale
ax.set_zlim(0, 100)

# Add a legend
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=industry, markersize=10, markerfacecolor=color) for industry, color in zip(industries, colors)]
ax.legend(handles=legend_elements, title='Industry', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()