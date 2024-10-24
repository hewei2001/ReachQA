import numpy as np
import matplotlib.pyplot as plt

# Tea types and their corresponding fictional satisfaction scores across different continents
tea_types = ['Green Tea', 'Black Tea', 'Herbal Tea', 'Oolong Tea', 'White Tea']

# Satisfaction scores for each tea type by continent
asia = [7, 8, 9, 7, 8]
europe = [6, 7, 6, 7, 6]
africa = [5, 4, 5, 4, 5]
north_america = [9, 8, 9, 8, 9]
south_america = [4, 5, 4, 5, 4]
australia = [7, 8, 7, 8, 7]

# Organizing the data into a list of lists for each tea type
continent_data = [asia, europe, africa, north_america, south_america, australia]

# Calculate average satisfaction scores for each tea type
average_scores = [np.mean([continent[i] for continent in continent_data]) for i in range(len(tea_types))]

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Box plot colors for each tea type
colors = ['#98FB98', '#FFD700', '#FF69B4', '#8A2BE2', '#00CED1']
for i, tea in enumerate(tea_types):
    tea_data = [continent[i] for continent in continent_data]
    ax.boxplot([tea_data], positions=[i], widths=0.6, vert=False, patch_artist=True,
               boxprops=dict(facecolor=colors[i], color='black'),
               whiskerprops=dict(color='black', linestyle='--'),
               capprops=dict(color='black'),
               flierprops=dict(marker='o', color='red', alpha=0.5),
               medianprops=dict(color='black'),
               notch=True)

# Overlay line plot for average satisfaction scores
ax.plot(average_scores, np.arange(len(tea_types)), 'o-', color='darkorange',
        label='Average Satisfaction', linewidth=2, markersize=8)

# Customizing axes and labels
ax.set_yticks(range(len(tea_types)))
ax.set_yticklabels(tea_types, fontsize=12, fontweight='bold')
ax.set_xlabel("Satisfaction Score", fontsize=12, fontweight='bold')
ax.set_title("Global Tea Preferences\nContinental Perspective and Average Scores", 
             fontsize=16, fontweight='bold', pad=20)
ax.grid(axis='x', linestyle='--', alpha=0.5)

# Legend
legend_labels = ['Green Tea', 'Black Tea', 'Herbal Tea', 'Oolong Tea', 'White Tea']
handles = [plt.Line2D([0], [0], color=colors[i], lw=4) for i in range(len(legend_labels))]
handles.append(plt.Line2D([0], [0], color='darkorange', lw=2))
ax.legend(handles, legend_labels + ['Average Satisfaction'], title='Tea Types', loc='upper right', 
          bbox_to_anchor=(1.3, 1), fontsize=12)

plt.tight_layout()
plt.show()