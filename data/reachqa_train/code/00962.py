import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Country labels
countries = ['France', 'Germany', 'Spain', 'Italy', 'Sweden', 'Poland']

# Renewable energy percentages by country (in percentage)
# Format: [Wind, Solar, Hydro, Biomass]
france = [30, 25, 20, 25]
germany = [40, 30, 10, 20]
spain = [50, 30, 15, 5]
italy = [20, 35, 30, 15]
sweden = [10, 20, 55, 15]
poland = [25, 20, 10, 45]

# Non-renewable energy percentages
france_nonrenewable = 100 - sum(france)
germany_nonrenewable = 100 - sum(germany)
spain_nonrenewable = 100 - sum(spain)
italy_nonrenewable = 100 - sum(italy)
sweden_nonrenewable = 100 - sum(sweden)
poland_nonrenewable = 100 - sum(poland)

# Compile all data into a list for ease of plotting
data = np.array([france, germany, spain, italy, sweden, poland])
nonrenewable_data = np.array([france_nonrenewable, germany_nonrenewable, spain_nonrenewable, 
                              italy_nonrenewable, sweden_nonrenewable, poland_nonrenewable])

# Bar colors for each renewable type
colors = ['skyblue', 'gold', 'lightgreen', 'saddlebrown']

# Create the percentage bar chart
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the stacked bar chart
bar_width = 0.5
bar_positions = np.arange(len(countries))

# Plot each component of the renewable energy sources
bottoms = np.zeros(len(countries))
for i in range(data.shape[1]):
    ax.bar(bar_positions, data[:, i], width=bar_width, label=['Wind', 'Solar', 'Hydro', 'Biomass'][i], 
           color=colors[i], bottom=bottoms, hatch=['/', '\\', '|', '-'][i])
    bottoms += data[:, i]

# Add non-renewable energy bars
ax.bar(bar_positions, nonrenewable_data, width=bar_width, label='Non-Renewable', color='gray', bottom=bottoms, alpha=0.6)

# Add percentage labels to each segment of the bars
for i, (country_data, country) in enumerate(zip(data, countries)):
    cumulative = 0
    for j, percentage in enumerate(country_data):
        ax.text(i, cumulative + percentage / 2, f'{percentage}%', ha='center', va='center', fontsize=9, color='black')
        cumulative += percentage
    ax.text(i, cumulative + nonrenewable_data[i] / 2, f'{nonrenewable_data[i]}%', ha='center', va='center', fontsize=9, color='black')

# Add titles and labels
ax.set_title('2023 Renewable Energy Mix:\nA European Perspective on Energy Distribution', fontsize=16, fontweight='bold')
ax.set_xlabel('Countries', fontsize=12)
ax.set_ylabel('Percentage (%)', fontsize=12)
ax.set_xticks(bar_positions)
ax.set_xticklabels(countries, fontsize=10)
ax.set_ylim(0, 100)

# Add a legend with dynamic positioning
legend_patches = [mpatches.Patch(color=color, label=label, hatch=hatch) 
                  for color, label, hatch in zip(colors + ['gray'], ['Wind', 'Solar', 'Hydro', 'Biomass', 'Non-Renewable'], ['/', '\\', '|', '-', ''])]
ax.legend(handles=legend_patches, loc='upper left', bbox_to_anchor=(1, 1), title="Energy Source", fontsize=10)

# Adjust layout to prevent overlapping text and graphics
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Display the chart
plt.show()