import matplotlib.pyplot as plt
import squarify

# Social Media Platforms and their monthly active users (in billions)
platforms = [
    "MetaVerse", "Twittory", "SnapMate", "InstaReel",
    "LinkNet", "PinClick", "TalkSpace", "StreamVision"
]

# Active users in billions
active_users = [3.1, 1.5, 0.6, 2.7, 0.9, 0.5, 2.2, 0.8]

# Define a color palette for the treemap
colors = ["#FF9999", "#66B3FF", "#99FF99", "#FFCC99",
          "#FFD700", "#8A2BE2", "#FF69B4", "#40E0D0"]

# Create the figure and axis
plt.figure(figsize=(12, 8))

# Plot the tree map using squarify
squarify.plot(sizes=active_users, label=[f"{name} ({size}B)" for name, size in zip(platforms, active_users)],
              color=colors, alpha=0.8, text_kwargs={'fontsize': 12, 'weight': 'bold', 'color': 'black'})

# Title for the plot
plt.title("The Digital Land:\nSocial Media Platforms by User Engagement in 2023", fontsize=16, fontweight='bold', pad=20)

# Hide axes for better clarity
plt.axis('off')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()