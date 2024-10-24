import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Define the renewable energy types
energy_types = ["Solar", "Wind", "Hydroelectric", "Biomass"]

# Define percentage preferences for each country
preferences = {
    "Country A": [40, 30, 20, 10],
    "Country B": [25, 35, 30, 10],
    "Country C": [45, 20, 25, 10],
    "Country D": [30, 40, 15, 15],
    "Country E": [35, 25, 20, 20]
}

# Colors and hatch patterns for each renewable energy type
colors = ['#FFD700', '#32CD32', '#1E90FF', '#FF6347']
hatches = ['/', '\\', '|', '-']

# Plot the percentage bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Positions for each group of bars (countries)
bar_positions = np.arange(len(preferences))
bar_width = 0.6

# Accumulated bottom positions for stacking bars
bottom_positions = np.zeros(len(preferences))

# Creating stacked bars with hatching
for i, energy in enumerate(energy_types):
    values = [country_pref[i] for country_pref in preferences.values()]
    bars = ax.bar(bar_positions, values, bar_width, 
                  label=energy, bottom=bottom_positions, 
                  color=colors[i], hatch=hatches[i], edgecolor='black')
    bottom_positions += values

# Set x-ticks as country names
ax.set_xticks(bar_positions)
ax.set_xticklabels(preferences.keys(), rotation=45, ha='right', fontsize=10)

# Adding data labels to each segment
for i, (country, prefs) in enumerate(preferences.items()):
    bottom = 0
    for value, color in zip(prefs, colors):
        ax.text(i, bottom + value / 2, f'{value}%', ha='center', va='center', 
                color='black', fontsize=9, weight='bold')
        bottom += value

# Label axes and title
ax.set_ylabel('Percentage of Preference (%)', fontsize=12, weight='bold')
ax.set_xlabel('Countries', fontsize=12, weight='bold')
ax.set_title('Renewable Preferences 2040:\nPublic Perceptions Across Countries', 
             fontsize=14, weight='bold', pad=20)

# Add legend with a shadow effect
legend_patches = [mpatches.Patch(facecolor=colors[i], hatch=hatches[i], edgecolor='black', label=energy_types[i]) for i in range(len(energy_types))]
ax.legend(handles=legend_patches, title='Energy Types', loc='upper left', bbox_to_anchor=(1, 1), shadow=True, fontsize=10)

# Set the y-axis range from 0 to 100%
ax.set_ylim(0, 100)

# Enable grid lines for the y-axis
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()