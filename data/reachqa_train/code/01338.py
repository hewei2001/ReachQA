import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Fictional countries and their characteristics
countries = ['Utopiana', 'Novelon', 'Scriptoria', 'Epistemia', 'Infotron', 'Gnostia', 'Techlantis']

# Literacy rates (%)
literacy_rates = np.array([95, 85, 90, 88, 78, 92, 96])

# Internet usage (% of population)
internet_usage = np.array([85, 60, 75, 70, 50, 80, 90])

# GDP per capita (thousands of USD)
gdp_per_capita = np.array([45, 30, 40, 32, 20, 42, 50])

# Population sizes (millions, for bubble sizes)
population_sizes = np.array([10, 25, 15, 22, 30, 18, 5])

# Setup the 3D scatter plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the data
bubble_size_factor = 100  # Scale factor for bubble sizes
scatter = ax.scatter(
    literacy_rates, internet_usage, gdp_per_capita,
    s=population_sizes * bubble_size_factor,
    c=population_sizes, cmap='viridis', alpha=0.8, edgecolors='w'
)

# Title and labels
ax.set_title('Literacy, Internet Usage & GDP in Eutopian Nations', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Literacy Rate (%)', fontsize=12)
ax.set_ylabel('Internet Usage (%)', fontsize=12)
ax.set_zlabel('GDP per Capita (thousands USD)', fontsize=12)

# Annotate each bubble with the country name
for i, country in enumerate(countries):
    ax.text(literacy_rates[i], internet_usage[i], gdp_per_capita[i], country, fontsize=9, weight='bold')

# Colorbar for population sizes
cbar = fig.colorbar(scatter, pad=0.1, aspect=10)
cbar.set_label('Population Size (millions)', fontsize=12)

# Adjust the viewing angle for better clarity
ax.view_init(elev=30, azim=120)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()