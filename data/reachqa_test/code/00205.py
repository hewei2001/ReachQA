import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Increased data for each instrument with non-linear patterns
loudness_sax = np.array([85, 90, 95, 100, 105, 110])
tonal_quality_sax = np.array([6, 7, 7.5, 8, 8.5, 9]) + np.sin(np.linspace(0, 3, 6))

loudness_trumpet = np.array([90, 95, 100, 105, 110, 115])
tonal_quality_trumpet = np.array([5, 6, 7, 7.5, 8, 8.5]) + 0.1 * (loudness_trumpet - 100)**2

loudness_piano = np.array([70, 75, 80, 85, 90, 95])
tonal_quality_piano = np.array([7, 7.5, 8, 8.5, 9, 9.5]) + 0.3 * np.cos(np.linspace(0, 3, 6))

loudness_bass = np.array([65, 70, 75, 80, 85, 90])
tonal_quality_bass = np.array([8, 8.5, 9, 9.5, 10, 10]) + 0.2 * np.log(np.linspace(1, 2, 6))

# Adding a new instrument
loudness_flute = np.array([75, 80, 85, 90, 95, 100])
tonal_quality_flute = np.array([6, 6.5, 7, 7.5, 8, 8.5]) + 0.5 * (np.array([75, 80, 85, 90, 95, 100]) / 100)**2

# Function to create smooth lines
def smooth_curve(x, y):
    x_new = np.linspace(x.min(), x.max(), 300)
    spl = make_interp_spline(x, y, k=3)
    y_smooth = spl(x_new)
    return x_new, y_smooth

# Initialize the plot with subplots for clarity
fig, ax = plt.subplots(figsize=(14, 8))
instruments = [
    (loudness_sax, tonal_quality_sax, 'Saxophone', 'skyblue'),
    (loudness_trumpet, tonal_quality_trumpet, 'Trumpet', 'orange'),
    (loudness_piano, tonal_quality_piano, 'Piano', 'green'),
    (loudness_bass, tonal_quality_bass, 'Double Bass', 'purple'),
    (loudness_flute, tonal_quality_flute, 'Flute', 'pink')
]

for loudness, tonal_quality, label, color in instruments:
    ax.scatter(loudness, tonal_quality, label=f'{label} (Data)', color=color, alpha=0.6, edgecolors='w', s=100)
    x_smooth, y_smooth = smooth_curve(loudness, tonal_quality)
    ax.plot(x_smooth, y_smooth, color=color, label=f'{label} (Fit)', linestyle='--')

# Customization
ax.set_title('Instrument Loudness vs. Tonal Quality in a Jazz Band\nExploring Harmonic Balance Through Complexity',
             fontsize=14, weight='bold')
ax.set_xlabel('Loudness (dB)', fontsize=12)
ax.set_ylabel('Tonal Quality', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_xlim(60, 120)
ax.set_ylim(4.5, 11)
ax.axhline(np.mean([tonal_quality_sax.mean(), tonal_quality_trumpet.mean(), tonal_quality_piano.mean(),
                    tonal_quality_bass.mean(), tonal_quality_flute.mean()]), color='red', linestyle=':', 
           label='Average Tonal Quality')

# Legend and layout adjustments
ax.legend(loc='upper left', fontsize=10)
plt.tight_layout()

# Show the plot
plt.show()