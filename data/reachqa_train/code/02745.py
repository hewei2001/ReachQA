import matplotlib.pyplot as plt
import numpy as np

# Centuries (BC and AD) representing the timeline
centuries = np.array([
    -30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30
])

# Global influence percentage for each writing system
cuneiform_influence = np.array([40, 42, 44, 35, 30, 20, 10, 5, 0, 0, 0, 0, 0])
hieroglyphics_influence = np.array([10, 15, 20, 25, 30, 40, 35, 30, 25, 20, 15, 10, 5])
phoenician_alphabet_influence = np.array([0, 0, 0, 0, 5, 20, 35, 45, 55, 60, 65, 70, 75])

# Create the figure and axis
plt.figure(figsize=(12, 8))

# Plot each writing system
plt.plot(centuries, cuneiform_influence, label='Cuneiform', color='brown', marker='o', linestyle='--', linewidth=2)
plt.plot(centuries, hieroglyphics_influence, label='Hieroglyphics', color='darkgreen', marker='s', linestyle='-', linewidth=2)
plt.plot(centuries, phoenician_alphabet_influence, label='Phoenician Alphabet', color='navy', marker='^', linestyle='-.', linewidth=2)

# Title and labels
plt.title("Evolution of Ancient Writing Systems\nOver Centuries (BC to AD)", fontsize=16, fontweight='bold')
plt.xlabel("Century (BC/AD)", fontsize=13)
plt.ylabel("Global Influence (%)", fontsize=13)

# Grid for readability
plt.grid(True, linestyle='--', alpha=0.5)

# Legend
plt.legend(title="Writing Systems", loc='upper left', fontsize=10)

# Annotating key points
plt.annotate('Peak of Cuneiform', xy=(-20, 44), xytext=(-15, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
plt.annotate('Emergence of Phoenician Alphabet', xy=(5, 45), xytext=(10, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Customize tick marks for better spacing
plt.xticks(centuries, rotation=45)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()