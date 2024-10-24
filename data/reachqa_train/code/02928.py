import matplotlib.pyplot as plt
import numpy as np

# Define the years for data collection
years = np.arange(2010, 2024)

# Adoption data for each technology over the years (in arbitrary units)
solar_adoption = np.array([10, 15, 23, 34, 48, 62, 80, 100, 124, 153, 190, 233, 280, 330])
wind_adoption = np.array([8, 14, 20, 29, 40, 54, 68, 85, 106, 130, 158, 190, 220, 250])
hydropower_adoption = np.array([30, 32, 35, 38, 42, 47, 52, 58, 65, 73, 80, 85, 90, 92])
geothermal_adoption = np.array([5, 7, 11, 16, 23, 31, 40, 52, 66, 83, 100, 118, 140, 160])

# Initialize the plot
plt.figure(figsize=(12, 8))

# Plotting the data for each renewable energy technology
plt.plot(years, solar_adoption, label='Solar', color='orange', linewidth=2, marker='o', linestyle='-')
plt.plot(years, wind_adoption, label='Wind', color='skyblue', linewidth=2, marker='s', linestyle='--')
plt.plot(years, hydropower_adoption, label='Hydropower', color='green', linewidth=2, marker='^', linestyle='-.')
plt.plot(years, geothermal_adoption, label='Geothermal', color='purple', linewidth=2, marker='d', linestyle=':')

# Titles and labels
plt.title('Renewable Energy Technology Adoption (2010-2023)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Adoption Level\n(Arbitrary Units)', fontsize=14)

# Formatting and ticks
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 351, 50))
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adding a legend
plt.legend(title='Technologies', fontsize=12, title_fontsize=13, loc='upper left', frameon=False)

# Highlighting key points with annotations
plt.annotate('Significant Solar Growth', xy=(2015, 62), xytext=(2012.5, 150),
             arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3,rad=0.3'),
             fontsize=10, color='black')

plt.annotate('Stable Hydropower Trend', xy=(2023, 92), xytext=(2016, 110),
             arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3,rad=-0.3'),
             fontsize=10, color='black')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Show the plot
plt.show()