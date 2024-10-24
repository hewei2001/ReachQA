import matplotlib.pyplot as plt
import numpy as np

# Initial carbon emissions
initial_emissions = 10000

# Expanded changes in emissions due to various factors, including some nonlinear impacts
emissions_changes = np.array([
    -1500,  # Wind energy
    -1200,  # Solar energy
    -800,   # Hydroelectric power
    -400,   # Geothermal energy
    -700,   # Biomass energy
    -500,   # Energy-efficient policies
    200,    # Industrial growth
    300,    # Population growth
    400 * np.log1p(2),  # Technological adoption (nonlinear)
    -100 * (2 ** 0.5),  # Carbon tax policy (nonlinear)
])

# Calculate positions for each stage
emissions_positions = np.zeros(len(emissions_changes) + 1)
emissions_positions[0] = initial_emissions
for i in range(1, len(emissions_positions)):
    emissions_positions[i] = emissions_positions[i-1] + emissions_changes[i-1]

# Labels for each stage
stages = [
    'Initial\nEmissions',
    'Wind\nEnergy',
    'Solar\nEnergy',
    'Hydroelectric\nPower',
    'Geothermal\nEnergy',
    'Biomass\nEnergy',
    'Energy\nPolicies',
    'Industrial\nGrowth',
    'Population\nGrowth',
    'Tech\nAdoption',
    'Carbon\nTax'
]

# Color differentiation for changes
colors = ['#4CAF50' if x < 0 else '#FF5733' for x in emissions_changes]
colors = ['#808080'] + colors  # Adding gray color for the initial bar

# Create the waterfall chart
fig, ax = plt.subplots(figsize=(16, 10))
bars = ax.bar(stages, emissions_positions, color=colors, edgecolor='black')

# Plot lines connecting each step
for i in range(1, len(emissions_positions)):
    ax.plot([i-1, i], [emissions_positions[i-1], emissions_positions[i-1]], "k--", linewidth=0.5)

# Annotate data labels
for bar, pos in zip(bars, emissions_positions):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, f"{pos:,.0f}", ha='center', va='bottom' if yval >= 0 else 'top', fontsize=10)

# Title and labels
ax.set_title("Expanded Analysis of Energy Transition Impacts on Urban Sustainability:\nIncorporating Diverse Renewable Sources and Policy Factors", fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Carbon Emissions (Metric Tons)', fontsize=12)
ax.set_xlabel('Transition Stages', fontsize=12)

# Rotate x-tick labels for clarity
plt.xticks(rotation=45, ha='right')

# Adjust the layout to ensure all elements fit neatly
plt.tight_layout()

# Show the plot
plt.show()