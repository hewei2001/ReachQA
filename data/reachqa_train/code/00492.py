import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(1990, 2021)

# Energy production in terawatt-hours (TWh) for each technology
solar_energy = np.array([0, 1, 3, 7, 15, 25, 50, 90, 140, 200, 280, 350, 440, 550, 680, 820, 970, 1130, 1300, 1480, 1670, 1870, 2080, 2300, 2530, 2770, 3020, 3280, 3550, 3830, 4120])
wind_energy = np.array([0, 1, 4, 9, 20, 35, 60, 100, 160, 230, 320, 420, 530, 650, 780, 920, 1070, 1230, 1400, 1580, 1770, 1970, 2180, 2400, 2630, 2870, 3120, 3380, 3650, 3930, 4220])
hydroelectric_energy = np.array([500, 510, 525, 540, 560, 580, 600, 620, 650, 680, 710, 740, 770, 800, 830, 860, 890, 920, 950, 980, 1010, 1040, 1070, 1100, 1130, 1160, 1190, 1220, 1250, 1280, 1310])
geothermal_energy = np.array([10, 11, 13, 16, 20, 25, 31, 38, 46, 55, 65, 76, 88, 101, 115, 130, 146, 163, 181, 200, 220, 241, 263, 286, 310, 335, 361, 388, 416, 445, 475])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the stacked area chart
ax.stackplot(years, solar_energy, wind_energy, hydroelectric_energy, geothermal_energy,
             labels=['Solar', 'Wind', 'Hydroelectric', 'Geothermal'],
             colors=['#FFA500', '#00BFFF', '#7FFF00', '#8A2BE2'], alpha=0.8)

# Set title and labels
ax.set_title('The Evolution of Green Technologies:\nRenewable Energy Contributions Over the Decades',
             fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Production (TWh)', fontsize=14)

# Add a legend
ax.legend(loc='upper left', fontsize=10, frameon=True)

# Add grid lines for better readability
ax.grid(True, which='major', linestyle='--', alpha=0.5)

# Adjust x-axis ticks for clarity
ax.set_xticks(np.arange(1990, 2021, 5))
ax.set_xticklabels(np.arange(1990, 2021, 5), rotation=45, ha='right')

# Annotate with notable trends or changes
ax.annotate('Start of Global Renewable Initiatives', (2005, 900), 
            textcoords="offset points", xytext=(30, 10), ha='center', fontsize=10,
            arrowprops=dict(arrowstyle='->', color='black'))

ax.annotate('Technological Breakthroughs in Solar', (2010, 1600),
            textcoords="offset points", xytext=(-20, 10), ha='center', fontsize=10,
            arrowprops=dict(arrowstyle='->', color='black'))

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()