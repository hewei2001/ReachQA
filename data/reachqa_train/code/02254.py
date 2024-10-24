import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data for FutureTech Social Media Analysis 2025
content_types = ['Video', 'Image', 'Text', 'Audio', 'Interactive']
platforms = ['AlphaNet', 'BetaStream', 'GammaLink', 'DeltaNet']

# Engagement data (Likes, Shares, Comments) in thousands
# Format: [Average Likes, Average Shares, Average Comments]
alpha_net_data = np.array([[50, 30, 20], [35, 25, 15], [20, 15, 10], [25, 10, 5], [60, 40, 30]])
beta_stream_data = np.array([[45, 28, 18], [30, 22, 12], [18, 12, 8], [20, 9, 4], [55, 35, 25]])
gamma_link_data = np.array([[55, 32, 22], [40, 27, 17], [22, 17, 12], [28, 12, 6], [65, 42, 32]])
delta_net_data = np.array([[48, 29, 19], [32, 23, 13], [21, 13, 9], [23, 11, 5], [58, 38, 28]])

# Engagement score (for bubble size)
alpha_engagement = np.sum(alpha_net_data, axis=1)
beta_engagement = np.sum(beta_stream_data, axis=1)
gamma_engagement = np.sum(gamma_link_data, axis=1)
delta_engagement = np.sum(delta_net_data, axis=1)

# Colors for platforms
colors = ['#FF5733', '#33FFCE', '#335BFF', '#FF33B8']

# Setting up the 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting each platform's data
for i, data in enumerate([alpha_net_data, beta_stream_data, gamma_link_data, delta_net_data]):
    ax.scatter(data[:, 0], data[:, 1], data[:, 2], 
               s=[size*10 for size in [alpha_engagement, beta_engagement, gamma_engagement, delta_engagement][i]],
               alpha=0.6, c=colors[i], edgecolors='w', linewidth=0.5, label=platforms[i])

# Adding annotations for content types
for i, data in enumerate(alpha_net_data):
    ax.text(data[0], data[1], data[2], content_types[i], fontsize=9, color='black')

# Labels and title
ax.set_xlabel('Average Likes (thousands)', fontsize=10)
ax.set_ylabel('Average Shares (thousands)', fontsize=10)
ax.set_zlabel('Average Comments (thousands)', fontsize=10)
ax.set_title('FutureTech Social Media Analysis 2025\nEngagement Across Platforms', fontsize=14, fontweight='bold')

# Legend
ax.legend(title="Platforms", fontsize=9, loc='upper left')

# Customize the view angle for better visualization
ax.view_init(elev=30, azim=240)

# Adjust layout to avoid text overlapping
plt.tight_layout()

# Show the plot
plt.show()