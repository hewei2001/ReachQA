import matplotlib.pyplot as plt
import numpy as np

# Create a figure
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Define the years and industries
years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
industries = ['Healthcare', 'Manufacturing', 'Finance']

# Define the adoption rates for each technology in each industry for each year
ai_adoption = np.array([
    [30, 35, 40, 45, 55, 60],
    [20, 25, 30, 35, 40, 50],
    [50, 55, 60, 65, 70, 75]
])

iot_adoption = np.array([
    [25, 30, 35, 40, 45, 55],
    [30, 35, 40, 45, 50, 60],
    [20, 25, 30, 35, 40, 50]
])

blockchain_adoption = np.array([
    [10, 15, 20, 25, 30, 40],
    [15, 20, 25, 30, 35, 45],
    [40, 45, 50, 55, 60, 70]
])

# Calculate average adoption rates across technologies for each industry by year
average_adoption = (ai_adoption + iot_adoption + blockchain_adoption) / 3

# X, Y positions for each bar
xpos, ypos = np.meshgrid(years, np.arange(len(industries)), indexing='ij')
xpos = xpos.flatten()
ypos = ypos.flatten()

# Bar dimensions
dx = dy = 0.5

# Colors and labels for each technology
colors = ['#FF9999', '#66B3FF', '#99FF99']
labels = ['AI', 'IoT', 'Blockchain']

# Plot each technology layer
for i, (adoption, color, label) in enumerate(zip([ai_adoption, iot_adoption, blockchain_adoption], colors, labels)):
    zpos = np.sum([ai_adoption, iot_adoption, blockchain_adoption][:i], axis=0).flatten()
    dz = adoption.flatten()
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=color, label=label, alpha=0.8, zsort='average')

# Overlay the average adoption line plot for each industry
for i, industry in enumerate(industries):
    ax.plot(years, np.full_like(years, i), average_adoption[i], 
            label=f'Avg. Adoption in {industry}', linewidth=2, linestyle='--', marker='o')

# Labeling
ax.set_xlabel('Year')
ax.set_ylabel('Industry')
ax.set_zlabel('Adoption Rate (%)')
ax.set_yticks(np.arange(len(industries)))
ax.set_yticklabels(industries)
ax.set_xticks(years)

# Title and legend
ax.set_title('Technological Adoption in Industries\n(2020-2025)\nWith Average Adoption Trends', pad=20)
ax.legend(loc='upper left', title='Technology and Trends')

# Adjust the view angle for better visualization
ax.view_init(elev=20, azim=135)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show plot
plt.show()