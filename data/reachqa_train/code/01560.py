import matplotlib.pyplot as plt
import numpy as np

# Years of observation
years = np.arange(2010, 2021)

# Artificial data for oscillation metrics
# Frequency of space-time oscillations (in arbitrary units)
frequency = [10, 11, 13, 15, 16, 18, 20, 21, 23, 24, 25]

# Amplitude of space-time oscillations (in arbitrary units)
amplitude = [5, 6, 7, 7, 9, 8, 10, 9, 11, 12, 11]

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the line chart
ax.plot(years, frequency, color='blue', linestyle='-', linewidth=2, marker='o', label='Frequency')
ax.plot(years, amplitude, color='green', linestyle='--', linewidth=2, marker='s', label='Amplitude')

# Add title and labels
ax.set_title('Decadal Observations of Space-Time Oscillations\nInsights from Quantum Fabric Theory', fontsize=16, weight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Oscillation Metric (Arbitrary Units)', fontsize=14)

# Customize grid
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add legend
ax.legend(loc='upper left', fontsize=12)

# Add annotations for notable changes
ax.annotate('Noticeable Frequency Increase', xy=(2016, frequency[6]), xytext=(2014, 22),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12, ha='center')

# Highlight a specific event/year
highlight_year = 2019
ax.axvline(x=highlight_year, color='red', linestyle='--', linewidth=1, alpha=0.8)
ax.text(highlight_year + 0.1, 21, 'Breakthrough Year', color='red', fontsize=12, rotation=90)

# Ensure layout fits well
plt.tight_layout()

# Display the plot
plt.show()