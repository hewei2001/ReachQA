import matplotlib.pyplot as plt
import numpy as np

# Define the decades and energy source shares (percentages) for each decade
decades = ['1980', '1990', '2000', '2010', '2020']
coal = [50, 45, 40, 30, 20]
nuclear = [10, 15, 20, 20, 15]
natural_gas = [20, 20, 25, 30, 25]
hydro = [15, 12, 10, 10, 10]
renewables = [5, 8, 5, 10, 30]  # Solar and Wind combined

# Stack data for the area plot
data = np.array([coal, nuclear, natural_gas, hydro, renewables])

# Generate the stacked area chart
plt.figure(figsize=(12, 8))
plt.stackplot(decades, coal, nuclear, natural_gas, hydro, renewables,
              labels=['Coal', 'Nuclear', 'Natural Gas', 'Hydro', 'Renewables'],
              colors=['#8B0000', '#FFD700', '#1E90FF', '#32CD32', '#FF8C00'], 
              alpha=0.8)

# Title and labels
plt.title('Energy Generation Mix Over the Decades:\nA Closer Look at Renewable Evolution',
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Decade', fontsize=12)
plt.ylabel('Percentage Share (%)', fontsize=12)

# Add legend outside the plot to avoid occlusion
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Energy Sources')

# Improve layout to accommodate legend
plt.tight_layout()

# Display the plot
plt.show()