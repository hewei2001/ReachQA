import matplotlib.pyplot as plt
import numpy as np

# Define categories and their respective values for two datasets
categories = ['Creativity', 'Technical Programming', 'Storytelling', 
              'Graphics Design', 'Sound Design', 'Project Management']

values1 = np.array([8, 6, 9, 7, 5, 8])
values2 = np.array([6, 7, 8, 6, 7, 9])

# Close the loop by appending the first value to both datasets
values1 = np.append(values1, values1[0])
values2 = np.append(values2, values2[0])

# Calculate angle for each category
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

# Initialize radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot first dataset
ax.fill(angles, values1, color='skyblue', alpha=0.3, label='Game Designer A')
ax.plot(angles, values1, color='blue', linewidth=2, linestyle='dashed')
ax.scatter(angles, values1, color='blue', s=50, edgecolors='navy')

# Plot second dataset
ax.fill(angles, values2, color='orange', alpha=0.3, label='Game Designer B')
ax.plot(angles, values2, color='red', linewidth=2, linestyle='dashed')
ax.scatter(angles, values2, color='red', s=50, edgecolors='darkred')

# Set category labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, color='darkblue', weight='bold')

# Enhanced grid and radial lines
ax.grid(color='gray', linestyle=':', linewidth=0.5)
ax.set_facecolor('whitesmoke')

# Set radial limits and custom ticks
ax.set_ylim(0, 10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='gray', size=12)

# Add title and legend
plt.title("Comparative Skills Analysis for Game Designers\n2023 Insights", 
          size=16, color='darkblue', weight='bold', pad=30)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2), fontsize=12)

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()