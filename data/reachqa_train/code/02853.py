import numpy as np
import matplotlib.pyplot as plt

# Define months and renewable energy sources
months = ['January', 'February', 'March', 'April', 'May']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Biomass']

# Data: Energy output in Gigawatt-hours (GWh) for each source
energy_data = np.array([
    [20, 15, 25, 10],  # January
    [25, 20, 30, 15],  # February
    [30, 25, 35, 20],  # March
    [40, 30, 40, 25],  # April
    [50, 35, 45, 30]   # May
])

# Colors for each energy source
colors = {
    'Solar': '#FFD700',   # Gold
    'Wind': '#1E90FF',    # Dodger Blue
    'Hydro': '#00FA9A',   # Medium Spring Green
    'Biomass': '#8B4513'  # Saddle Brown
}

# Plot configuration
fig, ax = plt.subplots(figsize=(12, 8))

# Create an area chart using stackplot
ax.stackplot(months, energy_data.T, labels=energy_sources, colors=[colors[source] for source in energy_sources], alpha=0.7)

# Chart title and labels
ax.set_title("Renaissance of Renewable Energy Sources in Wonderland\nMonthly Energy Output (GWh), 2023", fontsize=16, weight='bold', loc='center')
ax.set_xlabel("Months", fontsize=12)
ax.set_ylabel("Energy Output (GWh)", fontsize=12)

# Add grid lines for better visualization
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)

# Set x-axis labels with rotation for better readability
plt.xticks(rotation=45)

# Add legend with improved positioning
ax.legend(title='Energy Sources', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title_fontsize='11')

# Adjust layout to prevent overlap and enhance visual appeal
plt.tight_layout()

# Display the plot
plt.show()