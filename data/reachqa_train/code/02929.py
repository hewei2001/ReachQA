import matplotlib.pyplot as plt
import numpy as np

# Define the years for data collection
years = np.arange(2010, 2024)

# Original adoption data
solar_adoption = np.array([10, 15, 23, 34, 48, 62, 80, 100, 124, 153, 190, 233, 280, 330])
wind_adoption = np.array([8, 14, 20, 29, 40, 54, 68, 85, 106, 130, 158, 190, 220, 250])
hydropower_adoption = np.array([30, 32, 35, 38, 42, 47, 52, 58, 65, 73, 80, 85, 90, 92])
geothermal_adoption = np.array([5, 7, 11, 16, 23, 31, 40, 52, 66, 83, 100, 118, 140, 160])

# Create related dataset for cumulative capacity (in arbitrary units)
solar_capacity = solar_adoption.cumsum()
wind_capacity = wind_adoption.cumsum()
hydropower_capacity = hydropower_adoption.cumsum()
geothermal_capacity = geothermal_adoption.cumsum()

# Initialize the figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# First subplot: Adoption levels over the years
axs[0].plot(years, solar_adoption, label='Solar', color='orange', linewidth=2, marker='o', linestyle='-')
axs[0].plot(years, wind_adoption, label='Wind', color='skyblue', linewidth=2, marker='s', linestyle='--')
axs[0].plot(years, hydropower_adoption, label='Hydropower', color='green', linewidth=2, marker='^', linestyle='-.')
axs[0].plot(years, geothermal_adoption, label='Geothermal', color='purple', linewidth=2, marker='d', linestyle=':')
axs[0].set_title('Renewable Energy Technology Adoption\n(2010-2023)', fontsize=16, fontweight='bold', pad=15)
axs[0].set_xlabel('Year', fontsize=14)
axs[0].set_ylabel('Adoption Level\n(Arbitrary Units)', fontsize=14)
axs[0].set_xticks(years)
axs[0].tick_params(axis='x', rotation=45)
axs[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axs[0].legend(title='Technologies', fontsize=12, title_fontsize=13, loc='upper left', frameon=False)

# Annotations for key points
axs[0].annotate('Significant Solar Growth', xy=(2015, 62), xytext=(2012.5, 150),
                arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3,rad=0.3'),
                fontsize=10, color='black')

axs[0].annotate('Stable Hydropower Trend', xy=(2023, 92), xytext=(2016, 110),
                arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3,rad=-0.3'),
                fontsize=10, color='black')

# Second subplot: Cumulative capacity over the years
axs[1].stackplot(years, solar_capacity, wind_capacity, hydropower_capacity, geothermal_capacity,
                 labels=['Solar', 'Wind', 'Hydropower', 'Geothermal'],
                 colors=['orange', 'skyblue', 'green', 'purple'])
axs[1].set_title('Cumulative Capacity of Renewables\n(2010-2023)', fontsize=16, fontweight='bold', pad=15)
axs[1].set_xlabel('Year', fontsize=14)
axs[1].set_ylabel('Cumulative Capacity\n(Arbitrary Units)', fontsize=14)
axs[1].set_xticks(years)
axs[1].tick_params(axis='x', rotation=45)
axs[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axs[1].legend(title='Technologies', fontsize=12, title_fontsize=13, loc='upper left', frameon=False)

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the plots
plt.show()