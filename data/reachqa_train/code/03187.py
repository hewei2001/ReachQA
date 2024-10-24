import matplotlib.pyplot as plt
import numpy as np

# Character names and attributes
characters = ['Elara the Wise', 'Thorin Ironfist', 'Lyria Swift', 'Drogon the Mystic']
categories = ['Strength', 'Intelligence', 'Dexterity', 'Charisma', 'Wisdom', 'Luck']
num_categories = len(categories)

# Attribute values for each character
elara_attributes = [4, 9, 6, 7, 8, 5]
thorin_attributes = [9, 5, 7, 6, 5, 4]
lyria_attributes = [6, 7, 9, 8, 6, 7]
drogon_attributes = [5, 8, 5, 5, 9, 6]

# Arrange data and close the loop
data = [elara_attributes, thorin_attributes, lyria_attributes, drogon_attributes]
data_with_closure = [d + [d[0]] for d in data]

# Calculate angles for the radar chart
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
angles += angles[:1]  # Close the loop for angles

# Initialize the radar plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Plot each character's attributes
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']
for i, attribute_values in enumerate(data_with_closure):
    ax.fill(angles, attribute_values, color=colors[i], alpha=0.25, label=characters[i])
    ax.plot(angles, attribute_values, color=colors[i], linewidth=2)

# Set category labels
plt.xticks(angles[:-1], categories, color='grey', size=12)

# Add a descriptive title
plt.title('Character Attribute Comparison in Fantasia:\nA Radar Chart of Fictional Heroes', size=14, color='navy', pad=20)

# Add a legend outside the plot
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10, title='Characters')

# Ensure the layout is optimized
plt.tight_layout()

# Display the plot
plt.show()