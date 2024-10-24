import matplotlib.pyplot as plt
import numpy as np

# Define the years and quantum processor speeds in Qubits
years = np.arange(2015, 2026)
qubit_speeds = np.array([5, 7, 10, 14, 20, 28, 50, 85, 140, 220, 300])

# Estimated operations per second corresponding to qubit speeds (for illustration purposes)
operations_per_second = qubit_speeds * np.array([10**6, 2*10**6, 3*10**6, 4*10**6, 5*10**6, 7*10**6,
                                                9*10**6, 11*10**6, 15*10**6, 20*10**6, 25*10**6])

# Key milestone annotations
annotations = {
    2018: "10 Qubits",
    2020: "20 Qubit Breakthrough",
    2023: "100+ Qubits",
    2025: "300 Qubits"
}

# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(16, 7))

# First subplot: Line chart of quantum processor speeds
ax[0].plot(years, qubit_speeds, marker='o', linestyle='-', color='b', linewidth=2, label='Quantum Processor Speed')

# Annotate significant milestones
for year, label in annotations.items():
    ax[0].annotate(label,
                   (year, qubit_speeds[years == year]),
                   textcoords="offset points",
                   xytext=(0, 10),
                   ha='center',
                   fontsize=9,
                   arrowprops=dict(arrowstyle='->', color='gray'))

# Configure the first subplot
ax[0].set_title("Advancements in Quantum Technologies:\nProcessor Speeds (Qubits)", fontsize=13, fontweight='bold')
ax[0].set_xlabel("Year", fontsize=12)
ax[0].set_ylabel("Processor Speed (Qubits)", fontsize=12)
ax[0].grid(True, linestyle='--', alpha=0.6)
ax[0].axvline(2020, color='r', linestyle='--', linewidth=1, label='2020 Breakthrough')
ax[0].axvline(2025, color='g', linestyle='--', linewidth=1, label='Future Projection')
ax[0].legend(loc='upper left')
ax[0].set_xticks(years)
ax[0].set_yticks(range(0, 350, 50))

# Second subplot: Bar chart of operations per second
ax[1].bar(years, operations_per_second / 10**6, color='cyan', edgecolor='black', label='Operations per Second')

# Configure the second subplot
ax[1].set_title("Corresponding Computational Power\n(Operations per Second)", fontsize=13, fontweight='bold')
ax[1].set_xlabel("Year", fontsize=12)
ax[1].set_ylabel("Operations (Millions)", fontsize=12)
ax[1].grid(True, linestyle='--', alpha=0.6)
ax[1].legend(loc='upper left')
ax[1].set_xticks(years)

# Ensure no overlapping elements and adjust layout
plt.tight_layout()

# Display the chart
plt.show()