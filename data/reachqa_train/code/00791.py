import numpy as np
import matplotlib.pyplot as plt

# Tea types and the corresponding satisfaction scores from different continents
tea_types = ['Green Tea', 'Black Tea', 'Herbal Tea', 'Oolong Tea', 'White Tea']

# Constructed fictional satisfaction scores for each tea type by continent
asia = [7, 8, 9, 7, 8]
europe = [6, 7, 6, 7, 7]
africa = [5, 4, 5, 4, 5]
north_america = [9, 8, 9, 8, 9]
south_america = [4, 5, 4, 5, 4]
australia = [7, 8, 7, 8, 7]

# Organizing the data into a list of lists for each continent
data = [
    asia,          # Asia
    europe,        # Europe
    africa,        # Africa
    north_america, # North America
    south_america, # South America
    australia      # Australia
]

# Plotting the horizontal box plot
fig, ax = plt.subplots(figsize=(14, 8))

# Create horizontal boxplots for each tea type across continents
colors = ['#98FB98', '#FFD700', '#FF69B4', '#8A2BE2', '#00CED1']
for i, tea in enumerate(tea_types):
    tea_data = [continent[i] for continent in data]
    bp = ax.boxplot(tea_data, positions=[i], widths=0.6, vert=False, patch_artist=True, 
                    boxprops=dict(facecolor=colors[i], color='black'),
                    whiskerprops=dict(color='black', linestyle='--'),
                    capprops=dict(color='black'),
                    flierprops=dict(marker='o', color='red', alpha=0.5),
                    medianprops=dict(color='black'),
                    notch=True)

# Customize y-axis and labels
ax.set_yticks(range(len(tea_types)))
ax.set_yticklabels(tea_types, fontsize=12, fontweight='bold')
ax.set_xlabel("Satisfaction Score", fontsize=12, fontweight='bold')
ax.set_title("Global Tea Preferences: A Continental Perspective", fontsize=16, fontweight='bold', pad=20)
ax.grid(axis='x', linestyle='--', alpha=0.5)

# Adding a legend for continents
legend_labels = ['Asia', 'Europe', 'Africa', 'North America', 'South America', 'Australia']
handles = [plt.Line2D([0], [0], color=colors[i], lw=4) for i in range(len(tea_types))]
ax.legend(handles, legend_labels, title='Tea Types', loc='upper right', bbox_to_anchor=(1.25, 1), fontsize=12)

# Adjust layout for better fit and prevent overlap
plt.tight_layout()

# Show the plot
plt.show()