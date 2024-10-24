import matplotlib.pyplot as plt
import numpy as np

# Define years (quarterly granularity)
years = np.arange(2040, 2051, 0.25)

# Manually crafted energy consumption data for cities (in GWh) - quarterly
solar_energy = np.array([
    np.linspace(150, 250, len(years)),  # Technopolis
    np.linspace(120, 220, len(years)),  # Energetica
    np.linspace(140, 240, len(years)),  # Nova Terra
    np.linspace(100, 200, len(years)),  # Solaria
    np.linspace(160, 260, len(years))   # Zephyra
])

wind_energy = np.array([
    np.linspace(100, 155, len(years)),  # Technopolis
    np.linspace(90, 190, len(years)),   # Energetica
    np.linspace(95, 195, len(years)),   # Nova Terra
    np.linspace(80, 180, len(years)),   # Solaria
    np.linspace(105, 205, len(years))   # Zephyra
])

geothermal_energy = np.array([
    np.linspace(70, 120, len(years)),   # Technopolis
    np.linspace(60, 110, len(years)),   # Energetica
    np.linspace(65, 115, len(years)),   # Nova Terra
    np.linspace(50, 100, len(years)),   # Solaria
    np.linspace(75, 125, len(years))    # Zephyra
])

hydroelectric_energy = np.array([
    np.linspace(30, 80, len(years)),    # Technopolis
    np.linspace(40, 90, len(years)),    # Energetica
    np.linspace(35, 85, len(years)),    # Nova Terra
    np.linspace(45, 95, len(years)),    # Solaria
    np.linspace(55, 105, len(years))    # Zephyra
])

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 10))

# Plotting area chart for each city
for i, city in enumerate(['Technopolis', 'Energetica', 'Nova Terra', 'Solaria', 'Zephyra']):
    ax.stackplot(years,
                 solar_energy[i], wind_energy[i], geothermal_energy[i], hydroelectric_energy[i],
                 alpha=0.75,
                 colors=['#FFD700', '#1E90FF', '#228B22', '#8A2BE2'],
                 edgecolor='w',
                 linewidth=0.5)

# Set legend labels once after plotting
ax.legend(['Solar', 'Wind', 'Geothermal', 'Hydroelectric'], loc='upper left', frameon=False)

# Customizing the plot
ax.set_title('Energy Consumption Trends in Futuristic Smart Cities\nFrom 2040 to 2050 at Quarterly Intervals', fontsize=18, fontweight='bold', pad=15)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Consumption (GWh)', fontsize=14)
ax.set_xticks(np.arange(2040, 2051, 1))

# Add gridlines for readability
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Rotate x-axis labels to prevent overlap
plt.xticks(rotation=45)

# Highlight key data for 'Zephyra' in mid-2048
ax.annotate('Zephyra 2048 Mid: Renewables Peak', 
            xy=(2048.5, 270), xycoords='data',
            xytext=(2049, 350), textcoords='data',
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='gray'),
            fontsize=12, color='gray')

# Adjust layout for neatness
plt.tight_layout()

# Create a subplot for comparative analysis across cities
fig, ax2 = plt.subplots(figsize=(12, 6))
total_energy = solar_energy + wind_energy + geothermal_energy + hydroelectric_energy
average_energy_per_city = np.mean(total_energy, axis=1)

ax2.bar(['Technopolis', 'Energetica', 'Nova Terra', 'Solaria', 'Zephyra'], average_energy_per_city, color=['#FFD700', '#1E90FF', '#228B22', '#8A2BE2', '#FF6347'])
ax2.set_title('Average Energy Consumption by City\nAcross All Energy Sources (2040-2050)', fontsize=16, fontweight='bold')
ax2.set_xlabel('City', fontsize=14)
ax2.set_ylabel('Average Energy Consumption (GWh)', fontsize=14)
ax2.yaxis.grid(True, linestyle='--', alpha=0.6)

# Adjust layout for neatness
plt.tight_layout()

# Display plots
plt.show()