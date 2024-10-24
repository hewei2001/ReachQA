import matplotlib.pyplot as plt
import numpy as np

# Extended years for the x-axis (quarterly data from 2000 to 2023)
years = np.arange(2000, 2023.25, 0.25)

# Creating more detailed data, quarterly
europe = np.linspace(8.0, 12.0, len(years)) + np.sin(np.linspace(0, 10, len(years)))  # Adding some variation
north_america = np.linspace(4.0, 8.0, len(years)) + np.cos(np.linspace(0, 10, len(years)))
asia = np.linspace(0.5, 6.0, len(years)) + 0.5 * np.sin(np.linspace(0, 10, len(years)))
south_america = np.linspace(1.5, 5.5, len(years)) + 0.5 * np.cos(np.linspace(0, 10, len(years)))
africa = np.linspace(0.5, 4.0, len(years)) + 0.3 * np.sin(np.linspace(0, 10, len(years)))
oceania = np.linspace(2.0, 5.0, len(years)) + 0.4 * np.cos(np.linspace(0, 10, len(years)))

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 10))

# Plot each region's data with distinct styles
ax.plot(years, europe, marker='o', linestyle='-', color='brown', linewidth=2, label='Europe')
ax.plot(years, north_america, marker='s', linestyle='--', color='blue', linewidth=2, label='North America')
ax.plot(years, asia, marker='^', linestyle='-', color='red', linewidth=2, label='Asia')
ax.plot(years, south_america, marker='d', linestyle='-.', color='green', linewidth=2, label='South America')
ax.plot(years, africa, marker='x', linestyle=':', color='orange', linewidth=2, label='Africa')
ax.plot(years, oceania, marker='p', linestyle='-', color='purple', linewidth=2, label='Oceania')

# Adding titles and labels
ax.set_title("Extended Global Chocolate Consumption Trends (2000-2023)\nAnalyzing Per Capita Changes Over Time", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year (Quarterly)", fontsize=14)
ax.set_ylabel("Consumption per Capita (kg)", fontsize=14)

# Position the legend and add grid
ax.legend(loc='upper left', fontsize=12, title='Regions', title_fontsize='13')
ax.grid(True, linestyle='--', alpha=0.7)

# Improve x-axis labeling
plt.xticks(np.arange(2000, 2024, 1), rotation=45, fontsize=10)

# Adding a secondary y-axis to depict chocolate price trend
ax2 = ax.twinx()
chocolate_price = np.linspace(2, 10, len(years)) + 0.5 * np.cos(np.linspace(0, 10, len(years)))
ax2.plot(years, chocolate_price, color='gray', linestyle=':', linewidth=2, label='Chocolate Price ($/kg)')
ax2.set_ylabel("Chocolate Price ($/kg)", fontsize=14)
ax2.legend(loc='upper right', fontsize=12, title='Pricing', title_fontsize='13')

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()