import matplotlib.pyplot as plt
import numpy as np

# Energy sources and their corresponding usage percentages
energy_sources = ['Solar', 'Fusion', 'Wind', 'Geothermal', 'Hydrogen', 'Fossil Fuels']
energy_usage = np.array([25, 20, 15, 10, 20, 10])

# Colors for each section of the donut pie chart
colors = ['#FFD700', '#FF6347', '#4682B4', '#32CD32', '#9400D3', '#D2691E']

# Explode the first and second slice to highlight important segments
explode = (0.1, 0.1, 0, 0, 0, 0)

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(aspect="equal"))

# Plot the pie chart with a hole in the center to create the donut effect
wedges, texts, autotexts = ax.pie(energy_usage, 
                                  labels=energy_sources, 
                                  autopct='%1.1f%%', 
                                  startangle=140, 
                                  colors=colors, 
                                  explode=explode,
                                  wedgeprops=dict(width=0.3, edgecolor='w'),
                                  shadow=True)

# Customize text size and style
plt.setp(autotexts, size=10, weight="bold", color='black')
plt.setp(texts, size=10)

# Title split into two lines for clarity
plt.title('Galactic Energy Consumption:\nA Stellar Analysis of Energy Resources in 2050', 
          fontsize=14, weight='bold', pad=20)

# Add a legend with detailed descriptions, placed neatly
ax.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Adjust layout to ensure everything fits and looks clean
plt.tight_layout()

# Display the plot
plt.show()