import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Define the energy sources and their percentage share in EcoVille for 2023
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Biomass', 'Fossil Fuels']
consumption_2023 = [30, 25, 20, 15, 10]
consumption_2022 = [28, 24, 22, 15, 11]  # Previous year data for comparison

# Define colors and create gradients
colors = ['#FDB813', '#76C7C0', '#8ECF72', '#F39C6B', '#B0BEC5']
gradients = [cm.get_cmap('YlOrRd')(np.linspace(0.2, 0.8, len(energy_sources))),
             cm.get_cmap('GnBu')(np.linspace(0.2, 0.8, len(energy_sources)))]

# Create subplots for 2023 and 2022 data
fig, axs = plt.subplots(1, 2, figsize=(14, 7))
fig.suptitle("EcoVille's Energy Consumption: 2023 vs 2022", fontsize=16, fontweight='bold', y=0.98)

for ax, consumption, year, gradient in zip(axs, [consumption_2023, consumption_2022], [2023, 2022], gradients):
    wedges, texts, autotexts = ax.pie(
        consumption, 
        labels=energy_sources, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=[gradient[i] for i in range(len(energy_sources))],
        wedgeprops=dict(width=0.3, edgecolor='w'),
        pctdistance=0.85
    )
    
    plt.setp(autotexts, size=9, weight="bold", color='white')
    
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)
    
    ax.set_title(f"{year} Energy Distribution", fontsize=12, fontweight='bold', pad=20)

    # Annotate solar energy to highlight growth
    if year == 2023:
        ax.annotate(
            'Increased Solar Investment',
            xy=(0.1, 0.5), xytext=(0.3, 0.7),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, ha='center', color='#FDB813'
        )

# Add a shared legend
fig.legend(wedges, energy_sources, title="Energy Sources", loc="center", bbox_to_anchor=(0.5, 0), ncol=5)

# Ensure layout is adjusted properly to avoid overlap
plt.tight_layout(rect=[0, 0.05, 1, 0.95])

# Display the chart
plt.show()