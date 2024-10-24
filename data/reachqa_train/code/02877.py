import matplotlib.pyplot as plt
import numpy as np

# Define the categories for the radar chart
categories = ['Renewable Energy', 'Green Spaces', 'Public Transport',
              'Waste Management', 'Air Quality', 'Water Conservation']

# Number of variables we're plotting
num_vars = len(categories)

# Data for each city
Copenhagen = [85, 70, 80, 75, 90, 60]
Singapore = [75, 50, 90, 85, 85, 70]
Curitiba = [65, 80, 75, 90, 60, 85]

# Arrange data into a 2D array and repeat the first value to close the loop
data = np.array([Copenhagen, Singapore, Curitiba])
data = np.concatenate((data, data[:, [0]]), axis=1)

# Define angles for the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Create the radar chart
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

# Plot each city
ax.fill(angles, data[0], color='skyblue', alpha=0.25, label='Copenhagen')
ax.fill(angles, data[1], color='yellowgreen', alpha=0.25, label='Singapore')
ax.fill(angles, data[2], color='salmon', alpha=0.25, label='Curitiba')

# Draw the outline of each radar chart
ax.plot(angles, data[0], color='skyblue', linewidth=2)
ax.plot(angles, data[1], color='yellowgreen', linewidth=2)
ax.plot(angles, data[2], color='salmon', linewidth=2)

# Add category labels
ax.set_yticklabels([])  # Hide y-axis labels for cleanliness
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11, fontweight='semibold')

# Add a title
ax.set_title("Sustainability in Urban Development:\nComparative Analysis of Leading Cities",
             fontsize=16, fontweight='bold', pad=20)

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 0.1), fontsize=12, title='City', title_fontsize='13')

# Automatically adjust layout for optimal viewing
plt.tight_layout()

# Show plot
plt.show()