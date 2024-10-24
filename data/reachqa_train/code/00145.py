import matplotlib.pyplot as plt
import numpy as np

# Define the categories of the radar chart
categories = ['Funding', 'Innovation', 'Team Skills', 'Market Opportunity', 'Legal Environment']

# Define the data for each city
silicon_valley = [9, 8, 8, 9, 7]
tel_aviv = [7, 9, 8, 8, 6]
berlin = [6, 7, 7, 6, 8]

# Number of variables we're plotting
num_vars = len(categories)

# Compute angle for each axis and close the radar chart loop
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
silicon_valley += silicon_valley[:1]
tel_aviv += tel_aviv[:1]
berlin += berlin[:1]
angles += angles[:1]

# Start the plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each city's data on the radar chart
ax.fill(angles, silicon_valley, color='blue', alpha=0.25, label='Silicon Valley')
ax.fill(angles, tel_aviv, color='green', alpha=0.25, label='Tel Aviv')
ax.fill(angles, berlin, color='red', alpha=0.25, label='Berlin')

# Connect the data points with lines
ax.plot(angles, silicon_valley, color='blue', linewidth=2)
ax.plot(angles, tel_aviv, color='green', linewidth=2)
ax.plot(angles, berlin, color='red', linewidth=2)

# Remove radial labels for a cleaner look
ax.set_yticklabels([])

# Define and style category labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, ha='center')

# Add a descriptive title
plt.title('Comparative Analysis of Start-up Ecosystems\nAcross Major Cities', size=15, y=1.1)

# Add a legend to clarify which color represents which city
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Display the radar chart
plt.show()