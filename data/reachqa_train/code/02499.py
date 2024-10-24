import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2015 to 2025
years = np.arange(2015, 2026)

# Simulated data: number of patent applications in biotechnology fields
gene_editing = [100, 115, 130, 150, 175, 205, 235, 270, 310, 355, 400]
synthetic_biology = [80, 90, 105, 120, 140, 160, 185, 215, 250, 290, 335]
personalized_medicine = [95, 110, 125, 145, 165, 190, 220, 255, 295, 340, 390]

# Create the plot
plt.figure(figsize=(12, 8))

# Plot each data series with distinct styles
plt.plot(years, gene_editing, label='Gene Editing', color='darkblue', linewidth=2, marker='o')
plt.plot(years, synthetic_biology, label='Synthetic Biology', color='green', linewidth=2, linestyle='--', marker='s')
plt.plot(years, personalized_medicine, label='Personalized Medicine', color='purple', linewidth=2, linestyle='-.', marker='^')

# Set the chart title and axis labels
plt.title("Biotechland: Biotechnology Patent Application Trends\n(2015-2025)", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Number of Patent Applications", fontsize=12)

# Add a grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Add a legend to identify the different biotechnology fields
plt.legend(loc='upper left', fontsize=10)

# Customize x and y ticks
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 450, 50))

# Annotate key data points for clarity
for i, year in enumerate(years):
    plt.annotate(f'{gene_editing[i]}', (year, gene_editing[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8, color='darkblue')
    plt.annotate(f'{synthetic_biology[i]}', (year, synthetic_biology[i]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=8, color='green')
    plt.annotate(f'{personalized_medicine[i]}', (year, personalized_medicine[i]), textcoords="offset points", xytext=(0, -30), ha='center', fontsize=8, color='purple')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()