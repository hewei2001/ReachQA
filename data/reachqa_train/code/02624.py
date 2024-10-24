import matplotlib.pyplot as plt
import numpy as np

# Define the cuisines and flavor categories
cuisines = ['Indian', 'Italian', 'Chinese', 'Mexican', 'Thai']
flavor_categories = ['Spicy', 'Sweet', 'Savory', 'Umami', 'Bitter', 'Sour']

# Define the flavor intensity data for each cuisine
flavor_data = np.array([
    [8, 4, 7, 6, 3, 5],  # Indian
    [2, 6, 8, 7, 2, 4],  # Italian
    [4, 5, 7, 8, 3, 6],  # Chinese
    [7, 4, 6, 5, 2, 8],  # Mexican
    [8, 5, 6, 7, 2, 9]   # Thai
])

# Number of variables we're plotting
num_vars = len(flavor_categories)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Set up the figure and polar subplot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Define colors for each cuisine
colors = ['#FF5733', '#33FF57', '#3357FF', '#F3FF33', '#FF33F0']

# Loop through each cuisine and plot it on the radar chart
for i, cuisine_data in enumerate(flavor_data):
    values = cuisine_data.tolist() + [cuisine_data[0]]  # Close the loop correctly by adding the first element to the end
    ax.fill(angles, values, color=colors[i], alpha=0.25, label=cuisines[i])
    ax.plot(angles, values, color=colors[i], linewidth=1.5, linestyle='solid')

# Add the flavor categories to the axis
plt.xticks(angles[:-1], flavor_categories, color='black', size=10)

# Add labels for the intensity (radial) axis
ax.set_rlabel_position(0)
plt.yticks([2, 4, 6, 8], ["2", "4", "6", "8"], color="grey", size=8)
plt.ylim(0, 10)

# Add title and legend
plt.title('Cuisine Flavor Profile Evaluation\nA Comparison Across Five Popular Cuisines', size=14, weight='bold', va='bottom')
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1), fontsize=9)

# Automatically adjust layout
plt.tight_layout()

# Display the radar chart
plt.show()