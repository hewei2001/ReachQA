import matplotlib.pyplot as plt
import numpy as np

# Define the time periods (in centuries)
centuries = np.array([-25, -20, -15, -10, -5])  # Representing 2500 BCE to 500 BCE

# Estimated populations in thousands (artificial data)
egyptian_population = [500, 800, 1500, 1800, 1300]
mesopotamian_population = [600, 1100, 1200, 900, 800]
indus_valley_population = [400, 900, 1100, 1000, 300]

# Plotting the data
plt.figure(figsize=(12, 8))

plt.plot(centuries, egyptian_population, marker='o', linestyle='-', linewidth=2, color='gold', label='Egyptian Civilization')
plt.plot(centuries, mesopotamian_population, marker='s', linestyle='-', linewidth=2, color='teal', label='Mesopotamian Civilization')
plt.plot(centuries, indus_valley_population, marker='^', linestyle='-', linewidth=2, color='indigo', label='Indus Valley Civilization')

# Annotating key points
for i, (ce, me, iv) in enumerate(zip(egyptian_population, mesopotamian_population, indus_valley_population)):
    plt.text(centuries[i], ce + 50, f'{ce}k', ha='center', fontsize=9, color='goldenrod', fontweight='bold')
    plt.text(centuries[i], me - 120, f'{me}k', ha='center', fontsize=9, color='darkcyan', fontweight='bold')
    plt.text(centuries[i], iv + 50, f'{iv}k', ha='center', fontsize=9, color='purple', fontweight='bold')

# Adding title and labels
plt.title("Population Growth of Ancient Civilizations\n2500 BCE - 500 BCE", fontsize=16, fontweight='bold')
plt.xlabel("Time (Centuries BCE)", fontsize=14)
plt.ylabel("Population (in thousands)", fontsize=14)

# Adding a legend
plt.legend(title='Civilizations', fontsize=10, loc='upper left')

# Adding grid lines for readability
plt.grid(True, linestyle='--', alpha=0.6)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Reverse the x-axis to represent time from BCE to present
plt.gca().invert_xaxis()

# Show plot
plt.show()