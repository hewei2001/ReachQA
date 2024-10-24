import matplotlib.pyplot as plt
import numpy as np

# Data for electric vehicle projections (in millions)
years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
ev_projections = np.array([4, 8, 15, 25, 35, 50])  # in millions
error_margin = np.array([0.5, 1, 1.5, 2, 2.5, 3])  # error margins in millions

# Plot setup
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the line chart with error bars
ax.errorbar(years, ev_projections, yerr=error_margin, fmt='-o', color='green', 
            ecolor='lightgray', elinewidth=2, capsize=5, alpha=0.8,
            label='EV Adoption Projections')

# Titles and labels
ax.set_title('Projected Growth of Electric Vehicle\nAdoption Worldwide (2020-2025)',
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Electric Vehicles (Millions)', fontsize=12)

# Customize x-ticks and y-ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 60, 10))

# Add grid for readability
ax.grid(True, linestyle='--', alpha=0.5)

# Add legend
ax.legend(loc='upper left', fontsize=10, frameon=False)

# Annotate significant data points
for i, (year, projection, error) in enumerate(zip(years, ev_projections, error_margin)):
    ax.annotate(f'{projection}M±{error}M', 
                (year, projection + error + 2), 
                ha='center', fontsize=9, color='darkgreen', 
                bbox=dict(facecolor='lightgreen', alpha=0.5, boxstyle='round,pad=0.3'))

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()