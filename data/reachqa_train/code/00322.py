import matplotlib.pyplot as plt
import numpy as np

# Extended timeline and additional research areas
years = np.arange(2010, 2041)
atmosphere_analysis = 15 + 5 * np.sin(np.linspace(0, 2 * np.pi, len(years)))
geological_survey = 25 - 10 * np.sin(np.linspace(0, 2 * np.pi, len(years)))
water_detection = 20 + 5 * np.cos(np.linspace(0, 2 * np.pi, len(years)))
life_search = 10 + 7 * np.sin(np.linspace(0, 3 * np.pi, len(years)))
robotics_exploration = 15 + 3 * np.sin(np.linspace(0, 4 * np.pi, len(years)))
satellite_monitoring = np.clip(100 - (atmosphere_analysis + geological_survey +
                                      water_detection + life_search +
                                      robotics_exploration), 0, 25)

# Stack the data
data = np.vstack([
    atmosphere_analysis, geological_survey, water_detection, 
    life_search, robotics_exploration, satellite_monitoring
])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(
    years, data,
    labels=[
        'Atmosphere Analysis', 'Geological Survey', 'Water Detection', 
        'Life Search', 'Robotics Exploration', 'Satellite Monitoring'
    ],
    colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'], 
    alpha=0.8
)

# Adding labels and title
ax.set_title(
    'Evolving Focus in Planetary Research Activities\n'
    '(2010-2040)', fontsize=16, fontweight='bold'
)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Research Focus (%)', fontsize=12)
ax.legend(loc='upper right', title='Research Areas', fontsize=10, frameon=False)

# Customizing ticks and grid
ax.set_xticks(years[::2])  # Show every other year to reduce clutter
ax.tick_params(axis='x', rotation=45)
ax.grid(True, linestyle='--', alpha=0.5)

# Annotating significant changes
ax.annotate(
    'New Era in Robotics', xy=(2018, 70), xytext=(2012, 80),
    arrowprops=dict(facecolor='black', shrink=0.05),
    fontsize=10, fontweight='bold'
)

# Tight layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()