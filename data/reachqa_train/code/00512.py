import numpy as np
import matplotlib.pyplot as plt

# Define decades and energy types
decades = ['1980s', '1990s', '2000s', '2010s', '2020s']
energy_types = ['Solar', 'Wind', 'Hydroelectric']

# Data representing the global adoption rates (in percentage) for each energy type by decade
solar_adoption = [1, 2, 8, 15, 30]
wind_adoption = [3, 5, 10, 20, 25]
hydroelectric_adoption = [10, 12, 15, 18, 20]

# Stacked adoption data for the area chart
adoption_data = np.array([solar_adoption, wind_adoption, hydroelectric_adoption])

# Create a stacked area chart
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the stacked area chart
colors = ['#FFD700', '#87CEEB', '#8FBC8F']
ax.stackplot(decades, adoption_data, labels=energy_types, colors=colors, alpha=0.8)

# Set titles and labels
ax.set_title('Global Adoption of Renewable Energy Sources\nOver Recent Decades', fontsize=14, weight='bold', pad=20)
ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('Adoption Rate (%)', fontsize=12)
ax.legend(loc='upper left', fontsize=10)

# Enhance the grid
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add annotations for notable data points
ax.annotate('Early wind investments', xy=('1990s', 5), xytext=('1980s', 10),
            arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=9, color='blue')

ax.annotate('Rise of solar power', xy=('2000s', 8), xytext=('1990s', 15),
            arrowprops=dict(facecolor='orange', shrink=0.05), fontsize=9, color='orange')

ax.annotate('Significant growth', xy=('2010s', 33), xytext=('2020s', 40),
            arrowprops=dict(facecolor='green', shrink=0.05), fontsize=9, color='green')

# Adjust the layout to avoid overlapping
plt.tight_layout()

# Display the chart
plt.show()