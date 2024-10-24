import matplotlib.pyplot as plt
import numpy as np

# Defining age groups
age_groups = ['18-25', '26-35', '36-50', '51+']

# Data: perceived peace levels (on a scale of 1-100)
mindfulness_peace = [67, 72, 78, 85]
transcendental_peace = [60, 75, 73, 80]
zen_peace = [65, 70, 80, 88]
yoga_peace = [55, 68, 77, 83]

# Grouping the data for plotting
meditation_peace_data = [mindfulness_peace, transcendental_peace, zen_peace, yoga_peace]
meditation_types = ['Mindfulness', 'Transcendental', 'Zen', 'Yoga']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the horizontal box chart
box = ax.boxplot(meditation_peace_data, vert=False, patch_artist=True, notch=True,
                 boxprops=dict(facecolor='lightgreen', color='darkgreen'),
                 whiskerprops=dict(color='darkgreen', linestyle='--'),
                 capprops=dict(color='darkgreen'),
                 flierprops=dict(marker='o', color='red', alpha=0.5),
                 medianprops=dict(color='blue'))

# Customizing box colors for clarity
colors = ['#8fbc8f', '#2e8b57', '#3cb371', '#66cdaa']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set titles and labels
ax.set_yticklabels(meditation_types)
ax.set_xlabel('Perceived Peace Level (1-100)', fontsize=12, fontweight='bold')
ax.set_title('Meditative Practices and Peace of Mind\nAn Analytical Journey Across Age Groups', 
             fontsize=14, fontweight='bold', pad=20)
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Adding annotations for additional insight
ax.annotate('Peak Peace in Zen meditation\nfor those 51+ years', xy=(87, 3), xytext=(91, 3.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

ax.annotate('Growth in Peace with Age\nacross Mindfulness', xy=(84, 0), xytext=(90, 0.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Legend
plt.legend([box["boxes"][0]], ["Age Groups: " + ", ".join(age_groups)], loc='lower right', fontsize=10)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Show the plot
plt.show()