import matplotlib.pyplot as plt
import numpy as np

# Years from 2020 to 2030
years = np.arange(2020, 2031)

# Adoption levels (in arbitrary units, increasing over time)
computing = np.array([5, 10, 20, 35, 50, 70, 95, 125, 160, 210, 270])
telecommunications = np.array([3, 8, 15, 25, 40, 60, 80, 110, 150, 190, 240])
cryptography = np.array([2, 5, 12, 20, 35, 55, 75, 105, 135, 175, 220])
healthcare = np.array([1, 3, 7, 15, 25, 40, 60, 80, 105, 135, 180])
defense = np.array([4, 9, 18, 28, 45, 65, 85, 115, 145, 185, 230])

# Prepare data for stacked area chart
data = np.vstack([computing, telecommunications, cryptography, healthcare, defense])

# Create the area plot
plt.figure(figsize=(12, 8))
plt.stackplot(years, data, labels=['Computing', 'Telecommunications', 'Cryptography', 'Healthcare', 'Defense'],
              colors=['#d73027', '#fc8d59', '#fee08b', '#91bfdb', '#4575b4'], alpha=0.8)

# Customize the plot
plt.title("Exploring the Evolution of Quantum Technology\nFrom 2020 to 2030", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Quantum Technology Adoption (Arbitrary Units)", fontsize=12)

# Rotate x-axis labels to avoid overlap
plt.xticks(years, rotation=45)

# Add a legend
plt.legend(loc='upper left', title="Sectors", title_fontsize='13', fontsize='11', frameon=True)

# Add a grid for better readability
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Ensure layout is neat without overlapping
plt.tight_layout()

# Display the plot
plt.show()