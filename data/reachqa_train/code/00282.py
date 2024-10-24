import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.cm as cm

# Data for number of patents filed and their average citations
years = np.array(range(2010, 2024))
patents = np.array([50, 80, 120, 160, 210, 260, 310, 360, 420, 480, 540, 600, 660, 730])
citations = np.array([6, 10, 9, 12, 18, 21, 25, 28, 35, 33, 40, 44, 47, 55])

# Quadratic function for fitting
def smooth_trend(x, a, b, c):
    return a * np.power(x, 2) + b * x + c

# Fit the quadratic curve
params, _ = curve_fit(smooth_trend, patents, citations)

# Generate smooth line data for fitting curve
smooth_patents = np.linspace(patents.min(), patents.max(), 500)
smooth_citations = smooth_trend(smooth_patents, *params)

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 8))

# Scatter plot for the raw data points with color map
colors = cm.viridis(np.linspace(0, 1, len(years)))
scatter = ax1.scatter(patents, citations, c=colors, edgecolor='black', s=120, cmap='viridis', label='Patents Data')

# Add a colorbar for the years
cbar = plt.colorbar(scatter, ax=ax1)
cbar.set_label('Years', fontsize=12)

# Smooth trend line
ax1.plot(smooth_patents, smooth_citations, color='darkorange', linewidth=3, linestyle='--', label='Quadratic Trend Line')

# Annotate key data points
for i, txt in enumerate(years):
    if i in [0, len(years) - 1, len(years)//2]:  # annotate first, last, and middle points
        ax1.annotate(txt, (patents[i], citations[i]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=10, fontweight='bold')

# Titles and axis labels
ax1.set_title("Mapping the Path of Innovation:\nPatent Citations and Their Influence", fontsize=18, fontweight='bold')
ax1.set_xlabel("Number of Patents Filed", fontsize=14)
ax1.set_ylabel("Average Citations Per Patent", fontsize=14)

# Additional trend line for comparison
def exp_trend(x, a, b):
    return a * np.exp(b * x)

# Fit the exponential curve
exp_params, _ = curve_fit(exp_trend, patents, citations, p0=(1, 0.0001))
smooth_exp_citations = exp_trend(smooth_patents, *exp_params)
ax1.plot(smooth_patents, smooth_exp_citations, color='purple', linewidth=2, linestyle='-', label='Exponential Trend Line')

# Legend and grid
ax1.legend(loc='upper left', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()