import matplotlib.pyplot as plt
import numpy as np

# Data Preparation
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
initial_capacity = 100  # Initial capacity in MW
solar_changes = [20, 50, 20, 10]
wind_changes = [15, 40, 25, 20]
hydro_changes = [5, 10, 60, 20]
biomass_changes = [5, 15, 10, 40]

# Create cumulative changes
changes = [initial_capacity] + solar_changes + wind_changes + hydro_changes + biomass_changes
cumulative_changes = np.cumsum(changes)

# Label names
labels = ['Start'] + [f'{q}-{s}' for q in quarters for s in ['Solar', 'Wind', 'Hydro', 'Biomass']]

# Define colors for each segment
colors = ['#77DD77', '#FFB347', '#03C03C', '#779ECB', '#FFD1DC']  # green for positive, red-like for negative
highlight_color = '#C23B22'

# Create the waterfall chart
fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.bar(labels, cumulative_changes, color=[highlight_color] + [colors[i % 4] for i in range(len(labels) - 1)] + [highlight_color])

# Add lines to connect each bar
for i in range(1, len(bars)):
    ax.plot([bars[i-1].get_x() + bars[i-1].get_width() / 2, bars[i].get_x() + bars[i].get_width() / 2], 
            [cumulative_changes[i-1], cumulative_changes[i]], color='grey', linewidth=1.5)

# Annotating the bars with changes
for i, (bar, change) in enumerate(zip(bars, changes)):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 3, f"{change if i != 0 else ''} MW",
            ha='center', va='bottom', fontsize=9)

# Customizing the plot
ax.set_title("The Rise of Eco-Friendly Energy:\nQuarterly Growth in Renewable Sources (2023)", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Quarters & Energy Types", fontsize=12)
ax.set_ylabel("Cumulative Energy Production (MW)", fontsize=12)
ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=9)

# Add a baseline at the initial capacity
ax.axhline(y=initial_capacity, color='black', linestyle='--', linewidth=1)

# Displaying grid for better visualization
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Optimize layout
plt.tight_layout()

# Show the plot
plt.show()