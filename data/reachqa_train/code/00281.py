import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Artificial data for number of patents filed and their average citations
years = np.array(range(2010, 2024))
patents = np.array([50, 80, 120, 160, 210, 260, 310, 360, 420, 480, 540, 600, 660, 730])
citations = np.array([6, 10, 9, 12, 18, 21, 25, 28, 35, 33, 40, 44, 47, 55])

# Define a quadratic function for fitting
def smooth_trend(x, a, b, c):
    return a * np.power(x, 2) + b * x + c

# Fit the quadratic curve
params, _ = curve_fit(smooth_trend, patents, citations)

# Generate smooth line data for fitting curve
smooth_patents = np.linspace(patents.min(), patents.max(), 500)
smooth_citations = smooth_trend(smooth_patents, *params)

# Plotting
plt.figure(figsize=(12, 7))

# Scatter plot for the raw data points
plt.scatter(patents, citations, color='deepskyblue', label='Patents Data', edgecolor='k', s=100)

# Smooth trend line
plt.plot(smooth_patents, smooth_citations, color='darkorange', linewidth=2.5, linestyle='--', label='Trend Line')

# Title and axis labels
plt.title("Mapping the Path of Innovation:\nPatent Citations and Their Influence", fontsize=16, fontweight='bold')
plt.xlabel("Number of Patents Filed", fontsize=14)
plt.ylabel("Average Citations Per Patent", fontsize=14)

# Legend and grid
plt.legend(loc='upper left', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()