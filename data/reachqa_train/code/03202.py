import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2012 to 2021
years = np.arange(2012, 2022)

# Hypothetical average qubits processed per second (qps) over the years
qubit_speeds = np.array([100, 120, 140, 180, 230, 290, 370, 460, 580, 750])

# Hypothetical standard deviation in qubit processing speed
speed_errors = np.array([10, 15, 18, 25, 30, 35, 40, 45, 50, 55])

# Create the line chart with error bars
plt.figure(figsize=(14, 8))

# Plot the data with error bars
plt.errorbar(
    years, qubit_speeds, yerr=speed_errors, fmt='o-', color='navy',
    ecolor='lightblue', elinewidth=2, capsize=5, capthick=2,
    linewidth=2, markersize=8, label='Average Qubit Speed (qps)'
)

# Annotate significant years with breakthroughs
annotations = {
    2014: 'Algorithm\nAdvancement',
    2017: 'Superconducting\nMaterials',
    2020: 'Qubit\nStabilization'
}

for year, text in annotations.items():
    plt.annotate(
        text,
        (year, qubit_speeds[year - 2012]),
        xytext=(0, -50),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', color='gray'),
        ha='center', fontsize=10, color='maroon'
    )

# Titles and labels
plt.title(
    "Decadal Rise of Quantum Computing Speed\n(2012-2021)", 
    fontsize=16, fontweight='bold', pad=20
)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Qubit Processing Speed (qps)", fontsize=14)

# Customize the grid
plt.grid(True, linestyle='--', alpha=0.7)

# Ensure all years are marked on the x-axis
plt.xticks(years)

# Show the legend
plt.legend(loc='upper left', fontsize=12)

# Adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()