import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d

# Define the days and apparent magnitude data for each celestial object
days = np.arange(1, 366)  # Observations over a full year, assuming daily data
variable_star_magnitude = np.cos(np.linspace(0, 2*np.pi, 365)) + np.sin(np.linspace(0, 4*np.pi, 365)) * 0.5 + 5.5
comet_magnitude = np.linspace(9.5, 5.5, 365) + np.cos(np.linspace(0, 12*np.pi, 365)) * 0.4
galaxy_magnitude = 10 + np.sin(np.linspace(0, 6*np.pi, 365)) * 0.2
asteroid_magnitude = np.abs(np.sin(np.linspace(0, 8*np.pi, 365)) * 0.3 + 5.8)

# Set up the figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(16, 12))

# Plot data for each celestial object on the main subplot
axs[0, 0].plot(days, variable_star_magnitude, color='gold', linewidth=1.5, label='Variable Star')
axs[0, 0].plot(days, comet_magnitude, color='cyan', linestyle='--', linewidth=1.5, label='Comet')
axs[0, 0].plot(days, galaxy_magnitude, color='magenta', linestyle='-.', linewidth=1.5, label='Galaxy')
axs[0, 0].plot(days, asteroid_magnitude, color='green', linestyle=':', linewidth=1.5, label='Asteroid')

# Add titles and labels
axs[0, 0].set_title("Daily Observations: Luminosity of Celestial Objects", fontsize=14, fontweight='bold')
axs[0, 0].set_xlabel("Day of Observation", fontsize=12)
axs[0, 0].set_ylabel("Apparent Magnitude (lower is brighter)", fontsize=12)
axs[0, 0].grid(True, linestyle='--', alpha=0.5)
axs[0, 0].legend(title='Celestial Objects', fontsize=10, loc='upper right')

# Plot moving averages for trend analysis
window_size = 30  # Monthly average
variable_star_trend = np.convolve(variable_star_magnitude, np.ones(window_size)/window_size, mode='valid')
comet_trend = np.convolve(comet_magnitude, np.ones(window_size)/window_size, mode='valid')

axs[0, 1].plot(days[:len(variable_star_trend)], variable_star_trend, color='gold', linewidth=2, label='Variable Star Trend')
axs[0, 1].plot(days[:len(comet_trend)], comet_trend, color='cyan', linewidth=2, linestyle='--', label='Comet Trend')

# Add titles and labels
axs[0, 1].set_title("Trend Analysis: Moving Average", fontsize=14)
axs[0, 1].set_xlabel("Day of Observation", fontsize=12)
axs[0, 1].set_ylabel("Moving Average Magnitude", fontsize=12)
axs[0, 1].grid(True, linestyle='--', alpha=0.5)
axs[0, 1].legend(fontsize=10, loc='upper right')

# Plot standard deviation bands for variable star
smoothed_star = gaussian_filter1d(variable_star_magnitude, sigma=3)
std_dev = np.std(variable_star_magnitude)
axs[1, 0].plot(days, smoothed_star, color='gold', linewidth=1.5, label='Smoothed Variable Star')
axs[1, 0].fill_between(days, smoothed_star - std_dev, smoothed_star + std_dev, color='gold', alpha=0.3, label='±1 Std Dev')

# Add titles and labels
axs[1, 0].set_title("Variability Analysis: Standard Deviation Bands", fontsize=14)
axs[1, 0].set_xlabel("Day of Observation", fontsize=12)
axs[1, 0].set_ylabel("Smoothed Magnitude", fontsize=12)
axs[1, 0].grid(True, linestyle='--', alpha=0.5)
axs[1, 0].legend(fontsize=10, loc='upper right')

# Additional subplot with Fourier Transform Analysis (e.g., for comet)
freqs = np.fft.fftfreq(len(comet_magnitude))
fft_comet = np.abs(np.fft.fft(comet_magnitude))

axs[1, 1].plot(freqs, fft_comet, color='cyan', linewidth=1.5)
axs[1, 1].set_title("Frequency Domain Analysis: Comet", fontsize=14)
axs[1, 1].set_xlabel("Frequency", fontsize=12)
axs[1, 1].set_ylabel("Magnitude of FFT", fontsize=12)
axs[1, 1].grid(True, linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()