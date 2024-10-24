import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the genres and their appeal scores
genres = ['Mystery', 'Science Fiction', 'Historical Fiction', 'Fantasy', 'Romance', 'Non-Fiction']
appeal_scores = [80, 70, 65, 85, 75, 60]

# Number of variables
num_vars = len(genres)

# Compute angle for each genre on the plot
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Appeal scores need to loop back to the starting point to close the radar chart
appeal_scores += appeal_scores[:1]

# Plot setup
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one axe per variable and add labels
ax.set_yticklabels([])  # Remove y-tick labels for a cleaner look
ax.set_xticks(angles[:-1])
ax.set_xticklabels(genres, color='grey', fontsize=12)

# Adjust the radial limits
ax.set_ylim(0, 100)

# Plot data
ax.plot(angles, appeal_scores, linewidth=1.5, linestyle='solid', color='blue')

# Fill area
ax.fill(angles, appeal_scores, 'blue', alpha=0.3)

# Add a title
ax.set_title("Literary Genre Appeal\nAvid Readers' Preferences", fontsize=15, fontweight='bold', pad=20)

# Add a grid for better readability
ax.yaxis.grid(True)

# Customize radar chart
ax.spines['polar'].set_visible(False)  # Hide the polar spine
ax.tick_params(axis='x', which='major', pad=15)  # Move the labels outward

# Legend
ax.legend(['Appeal Score'], loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()