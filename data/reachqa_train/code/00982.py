import matplotlib.pyplot as plt
import numpy as np

# Radar Chart Data
labels = ['Renewable Energy', 'Waste Reduction', 'Green Spaces', 'Air Quality', 'Water Conservation', 'Transport Efficiency']
greenfield = [8, 7, 9, 6, 7, 8]
sunnytown = [7, 6, 8, 7, 8, 7]
eco_heights = [9, 8, 7, 9, 9, 8]
bluevale = [6, 5, 6, 8, 6, 7]

# New Overlay Plot Data (e.g., city-wide averages)
average_scores = [7.5, 6.8, 7.5, 7.5, 7.5, 7.5]

# Setup for Radar Chart
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Close the data loop for the radar chart
greenfield += greenfield[:1]
sunnytown += sunnytown[:1]
eco_heights += eco_heights[:1]
bluevale += bluevale[:1]
average_scores += average_scores[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Radar Chart Plot
ax.fill(angles, greenfield, color='lime', alpha=0.3, label='Greenfield')
ax.fill(angles, sunnytown, color='gold', alpha=0.3, label='Sunnytown')
ax.fill(angles, eco_heights, color='skyblue', alpha=0.3, label='Eco Heights')
ax.fill(angles, bluevale, color='orchid', alpha=0.3, label='Bluevale')

ax.plot(angles, greenfield, color='green', linewidth=2)
ax.plot(angles, sunnytown, color='darkorange', linewidth=2)
ax.plot(angles, eco_heights, color='blue', linewidth=2)
ax.plot(angles, bluevale, color='purple', linewidth=2)

# Overlay Plot - Average Line
ax.plot(angles, average_scores, color='red', linewidth=2, linestyle='--', label='City Average')

# Customizing the Radar Chart
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=11, weight='bold')
ax.tick_params(axis='x', labelsize=10)

# Title with Line Break
plt.title('Sustainability Indicators\nAcross Urban Neighborhoods', size=16, y=1.1, weight='bold', wrap=True)

# Add Legend
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2), fontsize=10)

# Annotations for Key Points
for angle, score in zip(angles, average_scores):
    ax.text(angle, score + 0.3, f'{score:.1f}', horizontalalignment='center', size=9, color='red')

# Adjust Layout
plt.tight_layout()

# Display the Chart
plt.show()