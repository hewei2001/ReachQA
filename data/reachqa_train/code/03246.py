import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.array([1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000])
medieval = np.array([90, 70, 50, 20, 10, 5, 2, 1, 0])
renaissance = np.array([0, 10, 30, 50, 40, 20, 10, 5, 2])
baroque = np.array([0, 0, 5, 20, 30, 40, 30, 15, 5])
neoclassical = np.array([0, 0, 0, 0, 10, 20, 30, 40, 20])
modern = np.array([0, 0, 0, 0, 10, 15, 28, 39, 73])

# Calculate rate of change for each architectural style
def calculate_rate_of_change(data):
    return np.gradient(data, years)

medieval_roc = calculate_rate_of_change(medieval)
renaissance_roc = calculate_rate_of_change(renaissance)
baroque_roc = calculate_rate_of_change(baroque)
neoclassical_roc = calculate_rate_of_change(neoclassical)
modern_roc = calculate_rate_of_change(modern)

# Setting up the plot with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# First subplot: Stacked Area Chart
ax1.stackplot(years, medieval, renaissance, baroque, neoclassical, modern, 
              labels=["Medieval", "Renaissance", "Baroque", "Neoclassical", "Modern"],
              colors=['#8c564b', '#d62728', '#9467bd', '#2ca02c', '#1f77b4'],
              alpha=0.8)
ax1.set_title("Evolution of Architectural Styles in Archopolis\n(1200-2000)", fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Percentage Coverage", fontsize=12)
ax1.set_xticks(years)
ax1.set_xticklabels([str(year) for year in years], rotation=45, ha='right', fontsize=10)
ax1.legend(title="Architectural Styles", fontsize=10, loc='upper left')
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Second subplot: Line Chart for Rate of Change
ax2.plot(years, medieval_roc, label="Medieval", color='#8c564b', marker='o')
ax2.plot(years, renaissance_roc, label="Renaissance", color='#d62728', marker='o')
ax2.plot(years, baroque_roc, label="Baroque", color='#9467bd', marker='o')
ax2.plot(years, neoclassical_roc, label="Neoclassical", color='#2ca02c', marker='o')
ax2.plot(years, modern_roc, label="Modern", color='#1f77b4', marker='o')
ax2.set_title("Rate of Change of Architectural Styles", fontsize=16, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Rate of Change", fontsize=12)
ax2.set_xticks(years)
ax2.set_xticklabels([str(year) for year in years], rotation=45, ha='right', fontsize=10)
ax2.legend(title="Architectural Styles", fontsize=10, loc='best')
ax2.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()