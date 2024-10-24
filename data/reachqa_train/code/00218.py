import matplotlib.pyplot as plt
import numpy as np

# Define key decades and popularity index data for various music consumption formats
years = np.array([1980, 1990, 2000, 2010, 2020])
vinyl = np.array([80, 50, 20, 15, 35])
cassette = np.array([60, 70, 30, 5, 0])
cds = np.array([10, 85, 95, 60, 25])
digital_downloads = np.array([0, 0, 40, 85, 55])
streaming = np.array([0, 0, 0, 20, 90])

# Create the plot
plt.figure(figsize=(12, 8))
plt.plot(years, vinyl, marker='o', linestyle='-', linewidth=2, color='darkred', label='Vinyl Records')
plt.plot(years, cassette, marker='s', linestyle='--', linewidth=2, color='goldenrod', label='Cassette Tapes')
plt.plot(years, cds, marker='^', linestyle=':', linewidth=2, color='navy', label='CDs')
plt.plot(years, digital_downloads, marker='d', linestyle='-.', linewidth=2, color='green', label='Digital Downloads')
plt.plot(years, streaming, marker='*', linestyle='-', linewidth=2, color='purple', label='Streaming Services')

# Add title and labels
plt.title("Evolution of Music Consumption:\nFrom Vinyl to Streaming", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=13)
plt.ylabel("Popularity Index", fontsize=13)
plt.xticks(years)
plt.yticks(range(0, 101, 10))

# Add legend to identify the data series
plt.legend(title='Music Formats', loc='upper left', fontsize=10)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust subplot params for better layout
plt.tight_layout()

# Show the plot
plt.show()