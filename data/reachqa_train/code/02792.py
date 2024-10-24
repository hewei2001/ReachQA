import matplotlib.pyplot as plt
import numpy as np

# Extended Data for the chart with regional preferences
coffee_types = ['Espresso', 'Cappuccino', 'Latte', 'Mocha', 'Americano', 'Cold Brew', 'Macchiato', 'Flat White', 'Ristretto', 'Affogato']
preferences_global = [23.5, 18.2, 16.7, 13.5, 10.8, 9.7, 3.3, 2.8, 0.9, 0.6]
preferences_asia = [15.2, 12.5, 20.0, 16.0, 8.0, 10.0, 5.0, 3.0, 7.5, 3.8]

# Colors for each segment
colors = ['#6F4E37', '#D2B48C', '#FFF8DC', '#8B4513', '#A0522D', '#2E8B57', '#8FBC8F', '#DEB887', '#CD853F', '#DAA520']

# Create the figure and axis for subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))

# Plot the global preference ring chart
ax1.pie(preferences_global, labels=coffee_types, autopct='%1.1f%%', startangle=90, 
        colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w'))
ax1.add_artist(plt.Circle((0, 0), 0.6, fc='white'))
ax1.axis('equal')
ax1.set_title('Global Preferences', fontsize=12, fontweight='bold', pad=15)

# Plot the Asia preference ring chart
ax2.pie(preferences_asia, labels=coffee_types, autopct='%1.1f%%', startangle=90, 
        colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w'))
ax2.add_artist(plt.Circle((0, 0), 0.6, fc='white'))
ax2.axis('equal')
ax2.set_title('Asian Preferences', fontsize=12, fontweight='bold', pad=15)

# Title for the entire figure
plt.suptitle('Gourmet Coffee Preferences Among Enthusiasts\nComparison between Global and Asian Markets in 2023', 
             fontsize=16, fontweight='bold')

# Adding a central label in the global chart
ax1.text(0, 0, 'Global\n2023', horizontalalignment='center', verticalalignment='center', 
         fontsize=14, fontweight='bold', color='navy')

# Adding a central label in the Asia chart
ax2.text(0, 0, 'Asia\n2023', horizontalalignment='center', verticalalignment='center', 
         fontsize=14, fontweight='bold', color='navy')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to make space for suptitle

# Display the plot
plt.show()