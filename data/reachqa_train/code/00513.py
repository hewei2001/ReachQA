import matplotlib.pyplot as plt
import numpy as np

# Define the years and quantum processor speeds in Qubits
years = np.arange(2015, 2026)
qubit_speeds = np.array([5, 7, 10, 14, 20, 28, 50, 85, 140, 220, 300])

# Key milestone annotations
annotations = {
    2018: "10 Qubits",
    2020: "20 Qubit Breakthrough",
    2023: "100+ Qubits",
    2025: "300 Qubits"
}

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))
ax.plot(years, qubit_speeds, marker='o', linestyle='-', color='b', linewidth=2, label='Quantum Processor Speed')

# Annotate significant milestones
for year, label in annotations.items():
    ax.annotate(label,
                (year, qubit_speeds[years == year]),
                textcoords="offset points", 
                xytext=(0, 10), 
                ha='center',
                fontsize=9,
                arrowprops=dict(arrowstyle='->', color='gray'))

# Setting up the labels and title
ax.set_title("Advancements in Quantum Technologies:\nQuantum Processor Speeds from 2015 to 2025", fontsize=14, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Quantum Processor Speed (Qubits)", fontsize=12)

# Customizing the grid and legends
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='upper left')

# Highlight critical projection years
ax.axvline(2020, color='r', linestyle='--', linewidth=1, label='2020 Breakthrough')
ax.axvline(2025, color='g', linestyle='--', linewidth=1, label='Future Projection')

# Avoid label overlap
plt.xticks(years)
plt.yticks(range(0, 350, 50))

# Adjust layout to fit text
plt.tight_layout()

# Display the chart
plt.show()