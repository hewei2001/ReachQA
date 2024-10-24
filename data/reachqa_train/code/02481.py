import numpy as np
import matplotlib.pyplot as plt

# Data setup
years = np.arange(2020, 2030)
honey_production = np.array([100, 120, 140, 160, 180, 205, 230, 260, 295, 330])

# Annotation details
annotations = {
    2022: "Community Programs Initiated",
    2025: "Urban Expansion Boost",
    2029: "Record Production"
}

# Initialize the plot
plt.figure(figsize=(12, 7))

# Plotting the line chart
plt.plot(years, honey_production, marker='o', color='gold', linewidth=2.5, linestyle='-', label='Urban Honey Production')

# Add annotations with arrows
for year, note in annotations.items():
    plt.annotate(
        note,
        xy=(year, honey_production[np.where(years == year)][0]),
        xytext=(year - 1, honey_production[np.where(years == year)][0] - 25),
        textcoords='data',
        arrowprops=dict(arrowstyle='->', color='darkgreen', lw=1.5),
        fontsize=10,
        fontweight='bold',
        color='darkgreen',
        ha='center'
    )

# Enhancing plot aesthetics
plt.title("The Rise of Urban Beekeeping: Honey Production Over the Decade", fontsize=14, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Honey Production (tons)", fontsize=12)

# Customizing ticks
plt.xticks(years)
plt.yticks(np.arange(100, 351, 50))

# Add grid
plt.grid(True, linestyle='--', alpha=0.5)

# Add legend
plt.legend(loc='upper left', fontsize=11)

# Ensure no overlap
plt.tight_layout()

# Display the plot
plt.show()