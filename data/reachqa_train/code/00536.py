import matplotlib.pyplot as plt
import numpy as np

# Years for the x-axis
years = np.arange(2010, 2021)

# Energy production data for each renewable source (in petawatt-hours)
solar = np.array([10, 15, 20, 30, 45, 60, 80, 110, 150, 195, 250])
wind = np.array([40, 55, 70, 90, 110, 130, 160, 200, 250, 310, 380])
hydroelectric = np.array([300, 305, 310, 320, 330, 340, 350, 365, 380, 395, 410])
biomass = np.array([50, 52, 55, 58, 62, 66, 70, 74, 79, 85, 90])

# Set up the plot with a specific size
plt.figure(figsize=(12, 7))

# Create stacked area chart
plt.stackplot(years, solar, wind, hydroelectric, biomass, 
              labels=['Solar', 'Wind', 'Hydroelectric', 'Biomass'],
              colors=['#ffcc00', '#66b3ff', '#99ff99', '#cc99ff'], 
              alpha=0.8)

# Add a comprehensive title and labels for axes
plt.title("Tech Evolution: The Rise of Renewable Energy Sources\nFrom 2010 to 2020", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Energy Production (PWh)", fontsize=12)

# Place the legend outside the plot area to avoid data occlusion
plt.legend(loc='upper left', fontsize=10, title='Energy Sources', bbox_to_anchor=(1, 1))

# Enhance layout to prevent overlap and ensure clear visibility of elements
plt.tight_layout()

# Display the final plot
plt.show()