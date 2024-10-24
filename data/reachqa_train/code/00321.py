import matplotlib.pyplot as plt
import numpy as np

# Years from 2020 to 2030
years = np.arange(2020, 2031)

# Research focus data
atmosphere_analysis = np.array([20, 22, 25, 27, 28, 30, 33, 35, 37, 40, 42])
geological_survey = np.array([30, 28, 25, 23, 23, 22, 21, 20, 19, 18, 17])
water_detection = np.array([35, 35, 35, 30, 28, 25, 20, 20, 19, 18, 15])
life_search = np.array([15, 15, 15, 20, 21, 23, 26, 25, 25, 24, 26])

# Stack the data
data = np.vstack([atmosphere_analysis, geological_survey, water_detection, life_search])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, data, labels=['Atmosphere Analysis', 'Geological Survey', 
                                  'Water Detection', 'Life Search'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], alpha=0.8)

# Adding labels and title
ax.set_title('Evolving Focus in Planetary Research\n(2020-2030)', fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Research Focus (%)', fontsize=12)
ax.legend(loc='upper left', title='Research Areas', fontsize=10, frameon=False)

# Customizing ticks and grid
ax.set_xticks(years)
ax.tick_params(axis='x', rotation=45)
ax.grid(True, linestyle='--', alpha=0.5)

# Tight layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()