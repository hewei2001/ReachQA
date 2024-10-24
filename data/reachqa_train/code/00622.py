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

# Calculate cumulative adoption for overlay plot
cumulative_adoption = computing + telecommunications + cryptography + healthcare + defense

# Prepare data for stacked area chart
data = np.vstack([computing, telecommunications, cryptography, healthcare, defense])

# Create the area plot
fig, ax1 = plt.subplots(figsize=(12, 8))
ax1.stackplot(years, data, labels=['Computing', 'Telecommunications', 'Cryptography', 'Healthcare', 'Defense'],
              colors=['#d73027', '#fc8d59', '#fee08b', '#91bfdb', '#4575b4'], alpha=0.8)

# Adding a line plot for cumulative adoption
ax2 = ax1.twinx()
ax2.plot(years, cumulative_adoption, label='Cumulative Adoption', color='darkgreen', linestyle='--', linewidth=2)
ax2.set_ylabel("Cumulative Adoption (Units)", fontsize=12)
ax2.legend(loc='upper right', title="Overlay", title_fontsize='13', fontsize='11', frameon=True)

# Customize the plot
ax1.set_title("Exploring the Evolution of Quantum Technology\nFrom 2020 to 2030", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Quantum Technology Adoption (Arbitrary Units)", fontsize=12)

# Rotate x-axis labels to avoid overlap
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Add a legend
ax1.legend(loc='upper left', title="Sectors", title_fontsize='13', fontsize='11', frameon=True)

# Add a grid for better readability
ax1.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Annotate the peak of cumulative adoption
peak_year = years[np.argmax(cumulative_adoption)]
peak_value = np.max(cumulative_adoption)
ax2.annotate(f'Peak: {peak_value}', xy=(peak_year, peak_value), xytext=(peak_year, peak_value + 40),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

# Ensure layout is neat without overlapping
plt.tight_layout()

# Display the plot
plt.show()