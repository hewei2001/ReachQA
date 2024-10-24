import matplotlib.pyplot as plt
import numpy as np

# Define years from 2015 to 2025
years = np.arange(2015, 2026)

# Funding data for each tech sector in millions of USD
funding_ai = np.array([50, 70, 100, 130, 180, 230, 280, 340, 410, 490, 600])
funding_iot = np.array([30, 40, 60, 80, 110, 150, 180, 220, 270, 330, 400])
funding_fintech = np.array([40, 65, 85, 120, 170, 220, 270, 340, 420, 510, 650])

# Create the figure and axis
plt.figure(figsize=(14, 8))

# Define color palette for each sector
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plot the funding data with markers
plt.plot(years, funding_ai, label='Artificial Intelligence', color=colors[0], marker='o', linestyle='-', linewidth=2.5)
plt.plot(years, funding_iot, label='Internet of Things', color=colors[1], marker='s', linestyle='-', linewidth=2.5)
plt.plot(years, funding_fintech, label='Fintech', color=colors[2], marker='^', linestyle='-', linewidth=2.5)

# Annotate each data point with the funding amount
for year, ai, iot, fintech in zip(years, funding_ai, funding_iot, funding_fintech):
    plt.annotate(f'${ai}M', (year, ai), textcoords="offset points", xytext=(-10, 10), ha='center', fontsize=9, color=colors[0], backgroundcolor='white')
    plt.annotate(f'${iot}M', (year, iot), textcoords="offset points", xytext=(-10, -15), ha='center', fontsize=9, color=colors[1], backgroundcolor='white')
    plt.annotate(f'${fintech}M', (year, fintech), textcoords="offset points", xytext=(-10, 5), ha='center', fontsize=9, color=colors[2], backgroundcolor='white')

# Add a multi-line title for clarity
plt.title('Innovation Journey:\nStartup Funding Trends in Tech from 2015 to 2025', fontsize=16, fontweight='bold', linespacing=1.5)

# Set the axis labels
plt.xlabel('Year', fontsize=14)
plt.ylabel('Funding Amount (Millions USD)', fontsize=14)

# Configure the grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Ensure the y-axis is scaled appropriately to display the data
plt.ylim(0, 700)

# Add a legend with a descriptive title
plt.legend(title='Tech Sectors', loc='upper left', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()