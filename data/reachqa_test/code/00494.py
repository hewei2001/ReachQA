import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Coffee types and regions
coffee_types = ['Espresso', 'Americano', 'Cappuccino', 'Latte', 'Cold Brew']
regions = ['USA', 'Canada', 'Mexico', 'Germany', 'France', 
           'Italy', 'Brazil', 'Argentina', 'Colombia']

# Construct consumption data (cups per person per day)
consumption_data = np.array([
    [2.5, 1.8, 1.5, 2.0, 1.0],  # USA
    [1.5, 1.0, 1.2, 1.8, 0.8],  # Canada
    [1.0, 0.9, 1.1, 1.3, 0.5],  # Mexico
    [3.0, 2.5, 2.0, 1.5, 0.7],  # Germany
    [2.8, 2.0, 1.5, 1.8, 0.6],  # France
    [3.2, 2.0, 1.0, 3.5, 0.3],  # Italy
    [4.0, 1.5, 1.3, 1.0, 1.5],  # Brazil
    [3.5, 2.0, 1.1, 0.8, 0.4],  # Argentina
    [3.2, 1.8, 1.0, 0.7, 1.6]   # Colombia
])

# Create the heat map with improved aesthetics
plt.figure(figsize=(14, 8))
heatmap = sns.heatmap(consumption_data, annot=True, fmt=".1f", cmap='YlGn', 
                       cbar_kws={'label': 'Cups per person per day'},
                       xticklabels=coffee_types, yticklabels=regions, linewidths=0.5, linecolor='black')

# Adjust the font size of the colorbar label
colorbar = heatmap.collections[0].colorbar
colorbar.ax.tick_params(labelsize=12)  # Adjusting the fontsize of the colorbar ticks

# Title with multi-line support
plt.title('Coffee Preference by Region\n(Avg. Cups per Person per Day)', fontsize=18, pad=20)

# Adjust x and y labels
plt.xlabel('Coffee Types', fontsize=14)
plt.ylabel('Regions', fontsize=14)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()