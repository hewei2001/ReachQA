import matplotlib.pyplot as plt
import numpy as np

# Define app categories and their corresponding user ratings
categories = ['Social Networking', 'Productivity', 'Gaming', 'Health & Fitness', 'Education']

# Explicitly created user ratings data for each category
ratings_data = [
    [3.8, 4.2, 3.9, 4.1, 4.3, 4.0, 3.8, 3.9, 4.4, 4.2, 4.1, 3.7, 3.9, 4.0, 4.2],
    [3.6, 3.9, 3.7, 4.0, 4.1, 3.9, 3.8, 3.9, 4.3, 4.0, 4.2, 3.8, 3.7, 4.1, 4.0],
    [4.5, 4.6, 4.4, 4.3, 4.7, 4.6, 4.5, 4.8, 4.7, 4.2, 4.3, 4.6, 4.4, 4.5, 4.7],
    [4.0, 4.1, 4.2, 4.4, 4.3, 4.5, 4.1, 4.2, 4.4, 4.1, 4.0, 4.3, 4.2, 4.3, 4.4],
    [4.3, 4.4, 4.2, 4.5, 4.4, 4.6, 4.2, 4.1, 4.5, 4.4, 4.3, 4.6, 4.5, 4.4, 4.3]
]

# Create the plot
plt.figure(figsize=(14, 8))

# Create a vertical box plot
box = plt.boxplot(ratings_data, vert=True, patch_artist=True, labels=categories, notch=True)

# Customize the appearance of the box plot
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightyellow']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Customize the whiskers, caps, medians, and fliers
plt.setp(box['whiskers'], color='grey', linestyle='--')
plt.setp(box['caps'], color='grey')
plt.setp(box['medians'], color='purple', linewidth=2)
plt.setp(box['fliers'], marker='o', color='red', alpha=0.5)

# Add titles and labels
plt.title("Mobile App Ratings Across Different Categories\nA Comprehensive Look at User Feedback", fontsize=16, fontweight='bold')
plt.xlabel("App Categories", fontsize=12)
plt.ylabel("User Ratings", fontsize=12)

# Add grid lines
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()