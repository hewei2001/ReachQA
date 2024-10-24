import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Average crop yields (in tons per hectare)
average_yields = np.array([2.5, 2.7, 2.9, 3.0, 3.1, 3.3, 3.5, 3.6, 3.8, 3.9, 4.0])

# Error margins due to climate conditions and other uncertainties
error_margins = np.array([0.2, 0.25, 0.3, 0.3, 0.35, 0.4, 0.35, 0.3, 0.25, 0.2, 0.2])

# Construct a secondary data set for comparative analysis (national averages for example)
national_averages = np.array([2.0, 2.1, 2.2, 2.3, 2.4, 2.6, 2.7, 2.9, 3.0, 3.2, 3.3])

# Create the plot
plt.figure(figsize=(14, 9))

# First plot: Error bar with enhanced visual elements
plt.errorbar(
    years, 
    average_yields, 
    yerr=error_margins, 
    fmt='-o', 
    capsize=5, 
    capthick=2, 
    color='forestgreen', 
    ecolor='orange', 
    elinewidth=2, 
    markerfacecolor='gold', 
    markersize=8,
    alpha=0.8,
    label='Average Yield with Error Margins'
)

# Adding a secondary line plot for national averages
plt.plot(
    years, 
    national_averages, 
    '-s', 
    color='royalblue', 
    markersize=6, 
    markerfacecolor='skyblue', 
    label='National Average Yields'
)

# Highlight significant periods with shaded regions
plt.axvspan(2015, 2016, color='lightgrey', alpha=0.5, label='Policy Changes')
plt.axvspan(2018, 2019, color='lightcoral', alpha=0.2, label='Climate Anomaly')

# Titles and labels with multiline title
plt.title('Decade of Organic Farming:\nYield Trends in Greenfield Valley (2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Crop Yield (tons/ha)', fontsize=12)

# Grid and legend
plt.grid(linestyle='--', alpha=0.6)
plt.legend(loc='upper left', fontsize=10)

# Additional annotations for significant trends
plt.annotate(
    'Yield Improvement Initiatives', 
    xy=(2015, 3.1), 
    xytext=(2011.5, 3.5), 
    arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8), 
    fontsize=11, 
    color='blue'
)
plt.annotate(
    'Sustainable Practice Adoption', 
    xy=(2018, 3.8), 
    xytext=(2016, 4.1), 
    arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8), 
    fontsize=11, 
    color='red'
)

# Use a secondary y-axis for related data (hypothetical additional data)
ax2 = plt.gca().twinx()
rainfall = np.array([300, 320, 290, 310, 330, 350, 370, 360, 380, 390, 400])  # Hypothetical data
ax2.plot(years, rainfall, '--', color='gray', label='Annual Rainfall (mm)')
ax2.set_ylabel('Annual Rainfall (mm)', fontsize=12)
ax2.legend(loc='upper right', fontsize=10)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()