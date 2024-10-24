import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
from scipy.stats import linregress

# Define years from 2015 to 2025
years = np.arange(2015, 2026)

# Funding data for each tech sector in millions of USD
funding_ai = np.array([50, 70, 100, 130, 180, 230, 280, 340, 410, 490, 600])
funding_iot = np.array([30, 40, 60, 80, 110, 150, 180, 220, 270, 330, 400])
funding_fintech = np.array([40, 65, 85, 120, 170, 220, 270, 340, 420, 510, 650])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(16, 9))

# Define color palette for each sector
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plot the funding data with markers and fill between the lines
ax.plot(years, funding_ai, label='Artificial Intelligence', color=colors[0], marker='o', linestyle='-', linewidth=2.5)
ax.plot(years, funding_iot, label='Internet of Things', color=colors[1], marker='s', linestyle='-', linewidth=2.5)
ax.plot(years, funding_fintech, label='Fintech', color=colors[2], marker='^', linestyle='-', linewidth=2.5)

# Fill areas between plots for visual effect
ax.fill_between(years, funding_ai, funding_iot, color='lightblue', alpha=0.1)
ax.fill_between(years, funding_iot, funding_fintech, color='orange', alpha=0.1)

# Linear trend lines for each sector
for funding, color in zip([funding_ai, funding_iot, funding_fintech], colors):
    slope, intercept, _, _, _ = linregress(years, funding)
    ax.plot(years, slope * years + intercept, linestyle='--', color=color, linewidth=1.5, alpha=0.7)

# Annotate each data point with the funding amount
for year, ai, iot, fintech in zip(years, funding_ai, funding_iot, funding_fintech):
    ax.annotate(f'${ai}M', (year, ai), textcoords="offset points", xytext=(-10, 10), ha='center', fontsize=9, color=colors[0], backgroundcolor='white')
    ax.annotate(f'${iot}M', (year, iot), textcoords="offset points", xytext=(-10, -15), ha='center', fontsize=9, color=colors[1], backgroundcolor='white')
    ax.annotate(f'${fintech}M', (year, fintech), textcoords="offset points", xytext=(-10, 5), ha='center', fontsize=9, color=colors[2], backgroundcolor='white')

# Multi-line title for clarity
ax.set_title('Innovation Journey:\nStartup Funding Trends in Tech from 2015 to 2025', fontsize=18, fontweight='bold', linespacing=1.5)

# Set the axis labels
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Funding Amount (Millions USD)', fontsize=14)

# Format y-axis labels as currency
formatter = FuncFormatter(lambda x, _: f'${int(x)}M')
ax.yaxis.set_major_formatter(formatter)

# Configure the grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Set limits for better data visualization
ax.set_ylim(0, 700)
ax.set_xlim(2015, 2025)

# Add a legend with a descriptive title
ax.legend(title='Tech Sectors', loc='upper left', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()