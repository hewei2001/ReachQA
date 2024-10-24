import matplotlib.pyplot as plt

# Data for the ring chart: percentage distribution of scientific objectives for each planet
planets = ['Zyron', 'Aelion', 'Nebulis', 'Cyran', 'Thalassa']
objectives = ['Atmosphere Study', 'Geological Analysis', 'Search for Life', 'Resource Utilization']

# Percentage allocation for each scientific objective per planet
data = {
    'Zyron': [30, 25, 35, 10],
    'Aelion': [25, 30, 20, 25],
    'Nebulis': [20, 20, 45, 15],
    'Cyran': [15, 35, 30, 20],
    'Thalassa': [40, 20, 25, 15]
}

# Colors for each objective
colors = ['#4daf4a', '#377eb8', '#ff7f00', '#e41a1c']

# Create a figure with a dynamic layout
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 14))
axes = axes.flatten()

# Loop through each planet to create a ring chart
for i, (planet, percentages) in enumerate(data.items()):
    ax = axes[i]
    wedges, texts, autotexts = ax.pie(
        percentages,
        colors=colors,
        labels=objectives,
        autopct='%1.1f%%',
        startangle=140,
        wedgeprops=dict(width=0.3, edgecolor='w'),
        textprops=dict(color="black")
    )

    # Add a white circle at the center to complete the ring effect
    center_circle = plt.Circle((0, 0), 0.70, color='white', fc='white', linewidth=0)
    ax.add_artist(center_circle)
    
    # Set title with planet name
    ax.set_title(f"Objectives for {planet}", fontsize=14, fontweight='bold')
    
    # Adjust the labels' font size and remove overlaps
    for text in texts + autotexts:
        text.set_fontsize(10)
    
    # Enhance the chart layout
    ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular

# Hide any unused subplots
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

# General settings
plt.suptitle("Galactic Alliance Exploration Missions\nScientific Objective Allocation", fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout(rect=[0, 0, 1, 0.98])

# Display the ring charts
plt.show()