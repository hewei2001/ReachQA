import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data points for the technological index of language mediums
years = np.array([1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050])
tech_index = np.array([10, 12, 15, 18, 22, 28, 35, 45, 60, 70, 80, 100, 180, 250])

# Generate smooth line using interpolation
years_new = np.linspace(years.min(), years.max(), 300) 
spl = make_interp_spline(years, tech_index, k=3)  # Smoothening
tech_index_smooth = spl(years_new)

# Create the scatter plot and smooth fitting line
fig, ax = plt.subplots(figsize=(12, 8))

# Scatter plot
ax.scatter(years, tech_index, color='darkblue', label='Tech Index Data Points', s=100, alpha=0.6)

# Smooth fitting line
ax.plot(years_new, tech_index_smooth, color='green', linestyle='-', linewidth=2.5, label='Smooth Fit')

# Annotate important transitions
annotations = {
    1400: "Start of Handwritten\nManuscripts Era",
    1700: "Printed Texts Revolution",
    1900: "Digital Texts Onset",
    2000: "Digital Dominance"
}

for year, text in annotations.items():
    ax.annotate(text, xy=(year, tech_index[np.where(years == year)][0]), 
                xytext=(-20, 20), textcoords='offset points', 
                arrowprops=dict(arrowstyle='->', color='gray'),
                ha='right', fontsize=10, color='black', weight='bold')

# Customize plot appearance
ax.set_title("Technological Evolution of Languages:\nTransition from Manuscripts to Digital Texts", 
             fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Technological Index of Language Medium", fontsize=12)
ax.set_xlim(1350, 2100)
ax.set_ylim(0, 300)
ax.grid(True, linestyle='--', alpha=0.7)

# Add legend
ax.legend(loc='upper left', frameon=False)

# Ensure layout fits all elements and text
plt.tight_layout()

# Display the plot
plt.show()