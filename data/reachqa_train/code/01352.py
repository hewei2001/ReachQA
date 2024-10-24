import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Extended years to include more historical data and potential future projections
years = np.array(list(range(2010, 2025)))

# Quantum volume values with hypothetical future projections for different companies
ibm_quantum_volume = np.array([4, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768])
google_quantum_volume = np.array([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768])
rigetti_quantum_volume = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384])
ionq_quantum_volume = np.array([0.5, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192])

# Function to model exponential growth
def exponential_growth(x, a, b):
    return a * np.exp(b * x)

# Fit the model to IBM data for demonstration
params, _ = curve_fit(exponential_growth, years, ibm_quantum_volume, p0=[1, 0.1])

# Plotting setup
fig, ax = plt.subplots(figsize=(16, 10))

# Plot lines for each company
ax.plot(years, ibm_quantum_volume, marker='o', linestyle='-', label='IBM', color='#1f77b4', linewidth=2)
ax.plot(years, google_quantum_volume, marker='s', linestyle='--', label='Google', color='#ff7f0e', linewidth=2)
ax.plot(years, rigetti_quantum_volume, marker='^', linestyle=':', label='Rigetti', color='#2ca02c', linewidth=2)
ax.plot(years, ionq_quantum_volume, marker='d', linestyle='-.', label='IonQ', color='#d62728', linewidth=2)

# Plot the exponential fit line
ax.plot(years, exponential_growth(years, *params), color='grey', linewidth=1.5, linestyle='-', label='IBM Exponential Fit')

# Annotating key milestones with adjustments to avoid overlap
ax.annotate('IBM Quantum Supremacy', xy=(2021, 512), xytext=(2018, 7000),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, fontweight='bold')

ax.annotate('Google Breakthrough', xy=(2023, 4096), xytext=(2016, 10000),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, fontweight='bold')

# Label data points selectively to avoid clutter
for i, year in enumerate(years):
    if i % 3 == 0:  # Reduce the frequency of text labels
        ax.text(year, ibm_quantum_volume[i], f'{ibm_quantum_volume[i]}', fontsize=8, ha='center', va='bottom')

# Customizing the plot with multiline title
plt.title('The Evolution of Quantum Computing Power\nOver Time and Company Projections', 
          fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Quantum Volume (Log Scale)', fontsize=12)
ax.set_yscale('log')
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.legend(title='Quantum Computing Companies', loc='upper left', fontsize=10, frameon=False)
plt.xticks(years, rotation=45)  # Rotate x-ticks for better spacing
plt.tight_layout()

# Show the plot
plt.show()