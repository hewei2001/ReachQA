import matplotlib.pyplot as plt
import numpy as np

# Years of data collection
years = np.array([2020, 2021, 2022, 2023, 2024])

# Funding allocation in millions of dollars
rover_missions = np.array([100, 120, 150, 130, 140])
habitat_research = np.array([80, 85, 100, 110, 120])
satellite_deployments = np.array([90, 100, 120, 115, 130])
human_training = np.array([60, 70, 85, 90, 100])
technology_development = np.array([70, 75, 95, 110, 125])

# Stack all funding categories
funding_data = np.vstack([
    rover_missions, habitat_research,
    satellite_deployments, human_training,
    technology_development
])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, funding_data, labels=[
    'Rover Missions', 'Habitat Research',
    'Satellite Deployments', 'Human Training',
    'Technology Development'], colors=['#FF6347', '#4682B4', '#FFD700', '#8A2BE2', '#32CD32'], alpha=0.8)

# Add titles and labels
ax.set_title("Mars Exploration Funding Allocation\n(2020-2024)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Funding in Millions ($)", fontsize=12)

# Add a legend
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=10, frameon=False)

# Style the grid and axes
ax.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)
ax.set_axisbelow(True)
ax.set_xlim(min(years), max(years))
ax.set_ylim(0, np.sum(funding_data, axis=0).max() + 50)

# Annotate significant points for emphasis
ax.annotate('Tech. Development Surge', xy=(2024, technology_development[-1] + habitat_research[-1]),
            xytext=(2023.5, 550),
            arrowprops=dict(facecolor='black', shrink=0.05, headwidth=8, width=2),
            fontsize=10, ha='center', fontstyle='italic')

# Adjust layout to prevent clipping of legend and improve spacing
plt.tight_layout()

# Display the chart
plt.show()