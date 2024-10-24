import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
from scipy.ndimage import gaussian_filter1d

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Popularity index for each art style
abstract_expressionism = [20, 25, 30, 35, 40, 50, 60, 70, 65, 60, 58]
minimalism = [30, 35, 38, 40, 45, 55, 68, 72, 75, 80, 85]
cyberpunk_art = [10, 15, 20, 25, 35, 45, 50, 60, 65, 70, 80]

# Smoothed data for trendlines
abstract_smooth = gaussian_filter1d(abstract_expressionism, sigma=1)
minimalism_smooth = gaussian_filter1d(minimalism, sigma=1)
cyberpunk_smooth = gaussian_filter1d(cyberpunk_art, sigma=1)

# Plotting the line chart
fig, ax1 = plt.subplots(figsize=(14, 10))

# Background shading for periods
ax1.axvspan(2010, 2012, color='gray', alpha=0.1, label='Initial Period')
ax1.axvspan(2013, 2017, color='orange', alpha=0.05, label='Growth Period')
ax1.axvspan(2018, 2020, color='purple', alpha=0.05, label='Modern Era')

# Main trend lines
ax1.plot(years, abstract_expressionism, marker='o', linestyle='-', color='#FF6F61', linewidth=2, label='Abstract Expressionism')
ax1.plot(years, minimalism, marker='s', linestyle='--', color='#92A8D1', linewidth=2, label='Minimalism')
ax1.plot(years, cyberpunk_art, marker='^', linestyle='-.', color='#76C7C0', linewidth=2, label='Cyberpunk Art')

# Smoothed trend lines
ax1.plot(years, abstract_smooth, color='#FF6F61', linestyle='-', alpha=0.6)
ax1.plot(years, minimalism_smooth, color='#92A8D1', linestyle='--', alpha=0.6)
ax1.plot(years, cyberpunk_smooth, color='#76C7C0', linestyle='-.', alpha=0.6)

# Enhancing annotations with textboxes
ax1.annotate('Rise of Minimalism', xy=(2015, 55), xytext=(2013, 75),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='white', alpha=0.9))
ax1.annotate('Cyberpunk Art Surge', xy=(2019, 70), xytext=(2017, 85),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='white', alpha=0.9))

# Annotating max and min points with different symbols
max_abstract = max(abstract_expressionism)
min_abstract = min(abstract_expressionism)
max_minimalism = max(minimalism)
min_minimalism = min(minimalism)
max_cyberpunk = max(cyberpunk_art)
min_cyberpunk = min(cyberpunk_art)

for i, txt in enumerate(abstract_expressionism):
    ax1.text(years[i], abstract_expressionism[i] + 2, str(txt), fontsize=9, ha='center', color='#FF6F61')
for i, txt in enumerate(minimalism):
    ax1.text(years[i], minimalism[i] + 2, str(txt), fontsize=9, ha='center', color='#92A8D1')
for i, txt in enumerate(cyberpunk_art):
    ax1.text(years[i], cyberpunk_art[i] - 5, str(txt), fontsize=9, ha='center', color='#76C7C0')

# Additional styling
ax1.set_title('Evolution of Art Styles in NeoCanvas District (2010-2020)\nAnalysis of Popularity Indices and Trendlines', fontsize=18, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Popularity Index', fontsize=14)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

# Legend
ax1.legend(title='Art Styles & Periods', loc='upper left', fontsize=10, ncol=2)

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()