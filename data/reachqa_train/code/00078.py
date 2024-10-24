import matplotlib.pyplot as plt

# Data
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']
energy_values = [150, 200, 100, 50, 30]
colors = ['#ffcc00', '#33ccff', '#99cc00', '#ff9966', '#669999']

# Create the ring chart
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(
    energy_values,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    textprops=dict(color="black", fontsize=11)
)

# Set autotext properties for better readability
plt.setp(autotexts, size=12, weight="bold")

# Title and central annotation
ax.set_title("Renewable Energy Sources Contribution in Greenville\n(Annual Breakdown)", fontsize=15, pad=40)
ax.annotate('Total Energy: {} MWh'.format(sum(energy_values)),
             xy=(0, 0), xytext=(0, 0),
             fontsize=13, ha='center', va='center', fontweight='bold')

# Legend customization
ax.legend(wedges, energy_sources, title="Energy Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()