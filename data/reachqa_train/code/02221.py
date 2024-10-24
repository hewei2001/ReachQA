import matplotlib.pyplot as plt
import squarify

# Data for Eco Metropolis 2050 energy distribution
sectors = ['Residential Areas', 'Commercial Districts', 'Industrial Zones', 'Public Facilities', 'Transportation']
energy_sources = ['Solar', 'Wind', 'Bioenergy', 'Hydro']

# Energy source distribution in each sector
data = {
    'Residential Areas': [50, 20, 20, 10],
    'Commercial Districts': [40, 30, 10, 20],
    'Industrial Zones': [15, 50, 10, 25],
    'Public Facilities': [30, 10, 40, 20],
    'Transportation': [30, 20, 10, 40]
}

# Flatten the data for plotting
labels = []
sizes = []

for sector in sectors:
    for energy, percent in zip(energy_sources, data[sector]):
        labels.append(f'{sector}\n{energy}: {percent}%')
        sizes.append(percent)

# Define a color palette
colors = ['#FFD700', '#1E90FF', '#3CB371', '#8B4513']

# Create the tree map
plt.figure(figsize=(14, 8))
squarify.plot(sizes=sizes, label=labels, color=colors * len(sectors), alpha=0.7, edgecolor="grey", linewidth=1.5)

# Set title and remove axes for a cleaner look
plt.title("Eco Metropolis 2050:\nEnergy Source Distribution Across City Sectors", fontsize=18, fontweight='bold')
plt.axis('off')

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()