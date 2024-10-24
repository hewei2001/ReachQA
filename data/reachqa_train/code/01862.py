import matplotlib.pyplot as plt

# Data setup
regions = ['Sunlandia', 'Windtopia', 'Hydroria', 'Biomassburg']
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Biomass']
colors = ['#FFD700', '#87CEEB', '#90EE90', '#D2B48C']

# Define preference percentages for each region
preferences = [
    [60, 10, 20, 10],  # Sunlandia
    [15, 55, 20, 10],  # Windtopia
    [10, 15, 65, 10],  # Hydroria
    [10, 10, 20, 60]   # Biomassburg
]

# Create the plot
fig, axes = plt.subplots(2, 2, figsize=(12, 12), subplot_kw=dict(aspect="equal"))
fig.suptitle('Power Source Preferences Across the Regions:\nA Renewable Focus', fontsize=16, fontweight='bold', y=0.95)

# Plot each region's donut pie chart
for i, ax in enumerate(axes.flat):
    wedges, texts, autotexts = ax.pie(
        preferences[i], labels=energy_sources, autopct='%1.1f%%',
        startangle=140, colors=colors, pctdistance=0.85,
        wedgeprops=dict(width=0.3), explode=(0.1, 0.1, 0.1, 0.1),
        shadow=True
    )
    
    ax.set_title(regions[i], fontsize=14, pad=10)
    
    # Draw the circle for the donut shape
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)

    # Formatting autotexts
    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_fontsize(10)
    
# Add a central legend
handles = [plt.Line2D([0], [0], color=colors[i], lw=4) for i in range(len(energy_sources))]
fig.legend(handles, energy_sources, loc='upper center', ncol=4, frameon=False, fontsize=12, title='Energy Sources', title_fontsize=12)

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.93])

# Display the plot
plt.show()