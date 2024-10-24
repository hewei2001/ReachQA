import matplotlib.pyplot as plt
import numpy as np

# Define the metrics and the platforms
labels = ['Likes', 'Comments', 'Shares', 'Reach', 'Saves']
num_vars = len(labels)

# Data for each platform representing engagement metrics
facebook = [75, 60, 45, 80, 50]
instagram = [85, 75, 70, 65, 90]
twitter = [65, 55, 80, 60, 40]
linkedin = [50, 40, 30, 55, 20]

# Extend data to close the radar chart loop
data = np.array([facebook, instagram, twitter, linkedin])
data = np.concatenate((data, data[:, [0]]), axis=1)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the loop

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Function to plot each platform's engagement
def plot_platform(ax, data, angles, label, color):
    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid', label=label)
    ax.fill(angles, data, color=color, alpha=0.25)

# Plot each platform's data with unique colors
plot_platform(ax, data[0], angles, 'Facebook', 'dodgerblue')
plot_platform(ax, data[1], angles, 'Instagram', 'mediumvioletred')
plot_platform(ax, data[2], angles, 'Twitter', 'skyblue')
plot_platform(ax, data[3], angles, 'LinkedIn', 'darkslategray')

# Customize chart features
ax.set_yticklabels([])  # Hide radial labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=12, color='darkblue', ha='center', va='center')
ax.set_title("Social Media Engagement Metrics\nInfluenceScope Analysis", size=16, color='darkred', va='bottom')

# Place legend outside the plot for better readability
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10, frameon=False)

# Ensure layout is neat without overlapping
plt.tight_layout()

# Display the plot
plt.show()