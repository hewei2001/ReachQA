import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the fitness attributes
attributes = ['Cardio', 'Strength', 'Flexibility', 'Balance', 'Endurance']
num_attributes = len(attributes)

# Data for user profiles
beginners = [2, 2, 3, 5, 2]
intermediate = [3, 4, 3, 4, 4]
advanced = [5, 5, 4, 4, 5]

# Combined data for plotting
data = [beginners, intermediate, advanced]
profiles = ['Beginners', 'Intermediate', 'Advanced']

# Calculate angle for each attribute
angles = np.linspace(0, 2 * pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

# Initialize radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each user profile
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
for i, profile_data in enumerate(data):
    profile_data += profile_data[:1]  # Closing the loop
    ax.fill(angles, profile_data, color=colors[i], alpha=0.25)
    ax.plot(angles, profile_data, color=colors[i], linewidth=2, label=profiles[i])

# Set the labels for each angle/spoke
ax.set_yticks(range(1, 6))
ax.set_yticklabels(map(str, range(1, 6)), color="grey", size=8)
plt.xticks(angles[:-1], attributes, fontsize=10)

# Add title and layout settings
ax.set_title('Digital Fitness Trends:\nComparison of User Profiles', size=16, color='navy', weight='bold', va='bottom')
ax.set_rlabel_position(30)

# Add a legend
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), title="User Profiles")

# Ensure the layout is tight and non-overlapping
plt.tight_layout()

# Display the plot
plt.show()