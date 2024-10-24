import matplotlib.pyplot as plt
import numpy as np

# Years of observation
years = np.arange(2010, 2021)

# Artificial data for oscillation metrics
frequency = [10, 11, 13, 15, 16, 18, 20, 21, 23, 24, 25]
amplitude = [5, 6, 7, 7, 9, 8, 10, 9, 11, 12, 11]

# New metric: Oscillation Intensity
intensity = [2, 3, 3, 4, 5, 4, 5, 5, 6, 7, 8]

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(14, 9))

# Plot frequency and amplitude on the primary y-axis
ax1.plot(years, frequency, color='blue', linestyle='-', linewidth=2, marker='o', label='Frequency')
ax1.plot(years, amplitude, color='green', linestyle='--', linewidth=2, marker='s', label='Amplitude')

# Customize grid and layout
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add a secondary y-axis for intensity
ax2 = ax1.twinx()
ax2.bar(years, intensity, color='orange', alpha=0.5, label='Intensity', width=0.4)

# Set titles and labels
ax1.set_title('Decadal Observations of Space-Time Oscillations\nInsights from Quantum Fabric Theory', fontsize=16, weight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Frequency / Amplitude (Arbitrary Units)', fontsize=14, color='black')
ax2.set_ylabel('Intensity (Arbitrary Units)', fontsize=14, color='black')

# Add trend lines
z_frequency = np.polyfit(years, frequency, 1)
p_frequency = np.poly1d(z_frequency)
ax1.plot(years, p_frequency(years), color='blue', linestyle='-', alpha=0.3, linewidth=1)

z_amplitude = np.polyfit(years, amplitude, 1)
p_amplitude = np.poly1d(z_amplitude)
ax1.plot(years, p_amplitude(years), color='green', linestyle='--', alpha=0.3, linewidth=1)

# Annotations and highlights
ax1.annotate('Noticeable Frequency Increase', xy=(2016, frequency[6]), xytext=(2013, 22),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, ha='center')

highlight_year = 2019
ax1.axvline(x=highlight_year, color='red', linestyle='--', linewidth=1, alpha=0.8)
ax1.text(highlight_year + 0.1, 21, 'Breakthrough Year', color='red', fontsize=12, rotation=90)

# Legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=12)

# Adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()