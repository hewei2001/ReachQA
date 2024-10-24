import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2012 to 2021
years = np.arange(2012, 2022)

# Hypothetical average qubits processed per second (qps) over the years
qubit_speeds = np.array([100, 120, 140, 180, 230, 290, 370, 460, 580, 750])

# Hypothetical standard deviation in qubit processing speed
speed_errors = np.array([10, 15, 18, 25, 30, 35, 40, 45, 50, 55])

# Hypothetical number of quantum algorithms developed per year
quantum_algorithms = np.array([5, 6, 9, 12, 15, 20, 30, 45, 70, 100])

# Create the figure and primary axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the line chart with error bars
ax1.errorbar(
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
    ax1.annotate(
        text,
        (year, qubit_speeds[year - 2012]),
        xytext=(0, -50),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', color='gray'),
        ha='center', fontsize=10, color='maroon'
    )

# Titles and labels for the primary axis
ax1.set_title(
    "Decadal Rise of Quantum Computing Speed (2012-2021)\n"
    "and Algorithm Development",
    fontsize=16, fontweight='bold', pad=20
)
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Qubit Processing Speed (qps)", fontsize=14, color='navy')
ax1.tick_params(axis='y', labelcolor='navy')

# Customize the grid
ax1.grid(True, linestyle='--', alpha=0.7)

# Ensure all years are marked on the x-axis
ax1.set_xticks(years)

# Create a secondary y-axis for the bar chart
ax2 = ax1.twinx()
ax2.bar(
    years, quantum_algorithms, alpha=0.6, color='darkorange',
    label='Quantum Algorithms Developed'
)

# Label for the secondary y-axis
ax2.set_ylabel("Quantum Algorithms", fontsize=14, color='darkorange')
ax2.tick_params(axis='y', labelcolor='darkorange')

# Show legends for both plots
fig.legend(loc='upper left', fontsize=12, bbox_to_anchor=(0.1, 0.85))

# Adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()