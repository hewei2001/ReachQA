import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.cm as cm

# Fictional data: Average sentence length (words) from classic literature
years = np.array([1800, 1820, 1840, 1860, 1880, 1900, 1920, 1940, 1960, 1980, 2000])
sentence_length = np.array([45, 50, 54, 48, 47, 44, 38, 34, 32, 28, 25])

# Create figure and axis objects with a larger size
fig, ax = plt.subplots(figsize=(14, 8))

# Scatter plot with color variation
colors = cm.viridis(np.linspace(0, 1, len(years)))
ax.scatter(years, sentence_length, s=120, c=colors, edgecolor='w', linewidth=1.5, alpha=0.8, zorder=3)

# Spline for smooth curve
years_smooth = np.linspace(years.min(), years.max(), 300)
spl = make_interp_spline(years, sentence_length, k=3)
sentence_length_smooth = spl(years_smooth)

# Color gradient effect for the smooth curve
norm = plt.Normalize(years_smooth.min(), years_smooth.max())
sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
sm.set_array([])

# Plot smooth curve with gradient
ax.plot(years_smooth, sentence_length_smooth, color='teal', linewidth=3, linestyle='-', label='Smooth Trend Line', zorder=2)

# Mean line
mean_value = np.mean(sentence_length)
ax.axhline(mean_value, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_value:.2f}', zorder=1)

# Annotations
highlight_years = [1860, 1920]
for highlight_year in highlight_years:
    hl_sentence_length = sentence_length[np.where(years == highlight_year)]
    ax.annotate(f'{highlight_year}\nNoticeable Change',
                xy=(highlight_year, hl_sentence_length),
                xytext=(highlight_year + 5, hl_sentence_length + 5),
                arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontsize=10, ha='center', va='bottom')

# Titles and labels
ax.set_title('Evolution of Writing Styles\nSentence Length in Classic Literature', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Average Sentence Length (words)', fontsize=14)

# Grid and legend
ax.grid(True, linestyle='--', alpha=0.4)
ax.legend(loc='upper right', fontsize=12)

# Color bar for gradient effect
cbar = plt.colorbar(sm, ax=ax, orientation='vertical')
cbar.set_label('Year', fontsize=12)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()