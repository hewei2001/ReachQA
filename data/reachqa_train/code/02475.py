import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2012 to 2022
years = np.arange(2012, 2023)

# Artificial data for each renewable energy source (in Terawatt-hours)
solar_power = np.array([10, 15, 22, 30, 38, 48, 60, 73, 88, 105, 123])
wind_power = np.array([20, 25, 30, 37, 45, 50, 58, 65, 75, 80, 88])
hydropower = np.array([50, 51, 52, 54, 55, 57, 58, 60, 61, 62, 64])

# Stack the data for the area plot
data = np.vstack([solar_power, wind_power, hydropower])

# Define colors for each energy type
colors = ['#FFD700', '#87CEEB', '#32CD32']

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, data, labels=['Solar Power', 'Wind Power', 'Hydropower'], colors=colors, alpha=0.8)

# Customizing the plot
ax.set_title("Renewable Energy Growth in Solaris\n (2012-2022)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Output (TWh)", fontsize=12)
ax.set_xlim(2012, 2022)
ax.set_ylim(0, 250)

# Adding a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Adjusting x-axis labels to avoid overlap
plt.xticks(years, rotation=45)

# Adding a legend outside the plot area
ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1), title="Energy Sources")

# Annotate significant growth in solar energy
ax.annotate('Significant Growth\n in Solar Energy', xy=(2019, 130), xytext=(2015, 180),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, fontweight='bold')

# Use tight layout to prevent clipping of labels
plt.tight_layout()

# Display the plot
plt.show()