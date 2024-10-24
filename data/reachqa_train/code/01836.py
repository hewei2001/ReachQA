import matplotlib.pyplot as plt
import numpy as np

# Define planets and qualities
planets = ['Alderaan', 'Tatooine', 'Endor', 'Naboo', 'Coruscant']
qualities = ['Biodiversity', 'Resource Richness', 'Tech Advancement', 'Cultural Development']

# Quality ratings for each planet (out of 10)
biodiversity = [9, 4, 8, 7, 3]
resource_richness = [7, 6, 8, 9, 5]
tech_advancement = [5, 3, 7, 8, 10]
cultural_development = [6, 4, 9, 8, 9]

# Data
data = [biodiversity, resource_richness, tech_advancement, cultural_development]

# Calculate average quality score for each planet
average_quality = np.mean(data, axis=0)

# Plotting the bar chart with data annotation
x = np.arange(len(planets))  # the label locations
width = 0.2  # the width of the bars

# Set up the figure
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each quality
colors = ['#76C7C0', '#FFB6C1', '#FFD700', '#6A5ACD']
rects1 = ax.bar(x - 1.5 * width, biodiversity, width, label='Biodiversity', color=colors[0])
rects2 = ax.bar(x - 0.5 * width, resource_richness, width, label='Resource Richness', color=colors[1])
rects3 = ax.bar(x + 0.5 * width, tech_advancement, width, label='Tech Advancement', color=colors[2])
rects4 = ax.bar(x + 1.5 * width, cultural_development, width, label='Cultural Development', color=colors[3])

# Overlay a line plot for average quality score
line = ax.plot(x, average_quality, marker='o', linestyle='-', color='black', label='Average Quality', linewidth=2)

# Annotate bars and line plot points
def annotate_bars(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, fontweight='bold')

for rects in [rects1, rects2, rects3, rects4]:
    annotate_bars(rects)

def annotate_line_points(x, y_values):
    for i, y in enumerate(y_values):
        ax.annotate(f'{y:.1f}', xy=(x[i], y),
                    xytext=(5, -10), textcoords="offset points", ha='center', va='bottom', fontsize=10, fontweight='bold')

annotate_line_points(x, average_quality)

# Customizing the plot
ax.set_ylabel('Quality Score (1-10)', fontsize=12)
ax.set_xlabel('Planets', fontsize=12)
ax.set_title('Intergalactic Survey of Planetary Qualities\nA Galactic Federation Study', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(planets, fontsize=11)
ax.legend(title="Qualities", fontsize=10)

# Add a grid for better readability
ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()