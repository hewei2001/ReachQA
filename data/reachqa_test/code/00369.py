import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ['18-24', '25-34', '35-44', '45-54', '55+', '65+']
social_media = ['Facebook', 'Instagram', 'Twitter', 'TikTok', 'Snapchat', 'YouTube', 'LinkedIn', 'Reddit', 'Pinterest', 'WhatsApp']
data = np.array([
    [0.8, 0.6, 0.4, 0.3, 0.2, 0.5, 0.1, 0.7, 0.4, 0.3],  # 18-24
    [0.7, 0.5, 0.6, 0.4, 0.3, 0.6, 0.2, 0.6, 0.5, 0.4],  # 25-34
    [0.6, 0.4, 0.7, 0.5, 0.4, 0.7, 0.3, 0.5, 0.6, 0.5],  # 35-44
    [0.5, 0.3, 0.6, 0.4, 0.3, 0.5, 0.4, 0.4, 0.5, 0.6],  # 45-54
    [0.4, 0.2, 0.5, 0.3, 0.2, 0.4, 0.5, 0.3, 0.4, 0.7],  # 55+
    [0.3, 0.1, 0.4, 0.2, 0.1, 0.3, 0.6, 0.2, 0.3, 0.8]  # 65+
])

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 12))

# Plot heat map
im = ax.imshow(data, cmap='viridis', interpolation='nearest', aspect='auto')

# Set title and labels
ax.set_title("The Digital Age:\nA Heatmap of Social Media Usage Across Various Age Groups\n"
             "Including Online Communities and Forum Participation", fontsize=14, ha='center')
ax.set_xlabel("Social Media Platforms")
ax.set_ylabel("Age Groups")

# Set x-axis and y-axis tick labels
ax.set_xticks(np.arange(len(social_media)))
ax.set_yticks(np.arange(len(age_groups)))
ax.set_xticklabels(social_media, rotation=45, ha='right', fontsize=10)
ax.set_yticklabels(age_groups, fontsize=10)

# Add color bar
fig.colorbar(im, ax=ax, shrink=0.7, pad=0.05)

# Automatically adjust the image layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show plot
plt.show()