import matplotlib.pyplot as plt
import numpy as np

# Define the international cuisines and their respective popularity scores
cuisines = ["Italian", "Japanese", "Mexican", "Indian", "Chinese", "Thai", "French", "Greek", "Spanish", "Middle Eastern"]
popularity_scores = np.array([85, 75, 70, 65, 60, 55, 50, 45, 40, 35])

# Colors for the bars, using a warm color palette
colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300', '#DAF7A6', '#FFC0CB', '#FF6F61', '#92A8D1', '#B833FF']

# Create the horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the bars
bars = ax.barh(cuisines, popularity_scores, color=colors, edgecolor='black', height=0.6)

# Set the title and labels with appropriate font sizes
ax.set_title('Culinary Adventures:\nPopularity of International Cuisines Among City Residents', fontsize=16, fontweight='bold', ha='center')
ax.set_xlabel('Popularity Score (out of 100)', fontsize=14)
ax.set_ylabel('Cuisines', fontsize=14)

# Add data labels to each bar
for bar in bars:
    ax.text(bar.get_width() - 5, bar.get_y() + bar.get_height() / 2, f'{bar.get_width()}', 
            ha='right', va='center', color='white', fontsize=10, fontweight='bold')

# Invert y-axis to have the highest score on top
ax.invert_yaxis()

# Add vertical grid lines to enhance readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Set x-axis limit to provide appropriate spacing
ax.set_xlim(0, 100)

# Annotate the leading cuisines
ax.annotate('Italian and Japanese lead the way!', xy=(80, 1), xytext=(50, 8), 
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), 
            fontsize=12, bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow', alpha=0.8))

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()