import matplotlib.pyplot as plt
import numpy as np

# Data for the original ring chart
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']
energy_values = [150, 200, 100, 50, 30]
colors = ['#ffcc00', '#33ccff', '#99cc00', '#ff9966', '#669999']

# Data for the radar chart
growth_rates = [5, 8, 3, 2, 4]  # Hypothetical annual growth rates in percentage
labels_for_radar = energy_sources

# Normalize growth rates for radar plot
growth_rates_normalized = np.array(growth_rates)

# Create a subplot for the chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(aspect="equal"))

# Ring Chart (Donut)
wedges, texts, autotexts = ax.pie(
    energy_values,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    textprops=dict(color="black", fontsize=11)
)

# Title and central annotation
ax.set_title("Renewable Energy Sources Contribution in Greenville\n(Annual Breakdown)", fontsize=15, pad=40)
ax.annotate('Total Energy: {} MWh'.format(sum(energy_values)),
            xy=(0, 0), xytext=(0, 0),
            fontsize=13, ha='center', va='center', fontweight='bold')

# Create Radar Chart
# Initialize the radar chart in polar coordinates
num_vars = len(labels_for_radar)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
growth_data = growth_rates_normalized.tolist()
angles += angles[:1]
growth_data += growth_data[:1]

# Subplot for the radar chart
radar_ax = fig.add_subplot(1, 1, 1, polar=True, frame_on=False)
radar_ax.set_theta_offset(np.pi / 2)
radar_ax.set_theta_direction(-1)

# Draw one axe per variable and add labels
radar_ax.set_xticks(angles[:-1])
radar_ax.set_xticklabels(labels_for_radar)

# Draw ylabels
radar_ax.set_rgrids([2, 4, 6, 8, 10])
radar_ax.plot(angles, growth_data, color='cyan', linewidth=2, linestyle='solid', label='Growth Rate (%)')
radar_ax.fill(angles, growth_data, color='cyan', alpha=0.3)

# Add a legend
ax.legend(wedges + [plt.Line2D([0], [0], color='cyan', linewidth=2)],
          energy_sources + ["Growth Rate (%)"],
          title="Data Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()