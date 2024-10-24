import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.gridspec import GridSpec

# Define the years and transportation methods
years = np.arange(2010, 2021)
methods = ['Cars', 'Trains', 'Ships', 'Airplanes']

# Percentage CO2 emissions data for each year by transportation method
data = np.array([
    [60, 10, 15, 15],  # 2010
    [58, 10, 16, 16],  # 2011
    [56, 10, 17, 17],  # 2012
    [54, 10, 18, 18],  # 2013
    [52, 11, 18, 19],  # 2014
    [50, 11, 19, 20],  # 2015
    [47, 11, 20, 22],  # 2016
    [45, 12, 20, 23],  # 2017
    [42, 12, 21, 25],  # 2018
    [40, 13, 21, 26],  # 2019
    [38, 13, 22, 27],  # 2020
])

# Calculate total CO2 emissions per method (hypothetical data in metric tons)
total_emissions = np.array([600, 800, 750, 900])  # for Cars, Trains, Ships, Airplanes respectively
emissions_data = (data / 100).T * total_emissions[:, np.newaxis]

# Set up figure and subplots
fig = plt.figure(figsize=(16, 10))
gs = GridSpec(1, 2, width_ratios=[3, 2], wspace=0.3)

# 3D Bar Chart
ax1 = fig.add_subplot(gs[0], projection='3d')

# Plot parameters
width = 0.15
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']

for idx, (method_data, color, method) in enumerate(zip(data.T, colors, methods)):
    xpos = np.arange(len(years))
    ypos = np.full_like(xpos, idx)
    zpos = np.zeros_like(xpos)
    ax1.bar3d(xpos, ypos, zpos, width, width, method_data, color=color, alpha=0.7, label=method)

# Customize plot
ax1.set_xlabel('Year', labelpad=10)
ax1.set_ylabel('Transport Method', labelpad=10)
ax1.set_zlabel('CO2 Emissions (%)', labelpad=10)
ax1.set_title('Percentage CO2 Emissions by Transport Method\n2010-2020', pad=20)
ax1.set_xticks(np.arange(len(years)))
ax1.set_xticklabels(years, rotation=45, ha='right')
ax1.set_yticks(np.arange(len(methods)))
ax1.set_yticklabels(methods)
ax1.set_zlim(0, 100)
ax1.legend(loc='upper left', bbox_to_anchor=(0.1, 1.1))
ax1.view_init(elev=20, azim=130)

# Stacked Area Chart
ax2 = fig.add_subplot(gs[1])

# Prepare data for the stacked area chart
emission_sums = emissions_data.sum(axis=0)
labels = [f'{year}' for year in years]

ax2.stackplot(years, emissions_data, labels=methods, colors=colors, alpha=0.7)
ax2.set_title('Total CO2 Emissions by Year and Method', fontsize=12)
ax2.set_xlabel('Year', fontsize=10)
ax2.set_ylabel('Emissions (Metric Tons)', fontsize=10)
ax2.legend(loc='upper left')
ax2.set_xticks(years)
ax2.set_xticklabels(labels, rotation=45, ha='right')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()