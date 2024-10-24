import matplotlib.pyplot as plt
import numpy as np

# Fictional data representing expedition durations (in years) for different mission types
sei_durations = [2.5, 3.0, 3.2, 3.5, 3.8, 4.0, 4.1, 4.5, 5.0, 5.2]  # Stellar Exploration Initiative
gra_durations = [1.5, 2.0, 2.1, 2.5, 2.8, 3.0, 3.5, 4.0]            # Galactic Research Alliance
cpc_durations = [4.0, 4.2, 4.5, 5.0, 5.5, 6.0, 6.2, 6.5, 7.0, 7.5]  # Cosmic Pioneers Corporation
afc_durations = [3.0, 3.3, 3.5, 3.7, 4.0, 4.2, 4.5, 4.7, 5.0]       # Astronomical Frontiers Council

# Compile the data into a list for plotting
data = [sei_durations, gra_durations, cpc_durations, afc_durations]

# Agency names
agencies = ['SEI', 'GRA', 'CPC', 'AFC']

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))

# Create a horizontal boxplot with customization
box = ax.boxplot(data, vert=False, patch_artist=True, notch=True, labels=agencies, whis=1.5)

# Define colors for each agency
colors = ['#add8e6', '#90ee90', '#ffcccb', '#d3d3d3']

# Apply customizations to the boxplot
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)  # Set transparency

# Titles and labels
plt.title('The Ethereal Voyage: \nInsight into Interstellar Expedition Durations', fontsize=14, fontweight='bold')
plt.xlabel('Duration (Years)', fontsize=12)
plt.ylabel('Space Agencies', fontsize=12)

# Add annotations to highlight findings
ax.annotate('Longest Average Duration', xy=(6.5, 3), xytext=(7, 2.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')
ax.annotate('Shortest Range', xy=(2.3, 1), xytext=(3, 0.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

# Ensure no elements are occluded
plt.grid(linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()