import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(1900, 2001, 10)

# Visitor numbers in thousands for each library
nypl_visitors = [80, 120, 150, 170, 200, 220, 210, 180, 140, 130, 150]
british_library_visitors = [60, 70, 90, 110, 150, 160, 140, 120, 110, 100, 120]
bibliotheque_france_visitors = [50, 65, 80, 100, 130, 155, 135, 115, 90, 95, 110]

# Create a new figure
plt.figure(figsize=(14, 8))

# Plotting each line with unique styles and markers
plt.plot(years, nypl_visitors, label='New York Public Library', color='navy', linestyle='-', marker='o', markersize=8, linewidth=2)
plt.plot(years, british_library_visitors, label='British Library', color='crimson', linestyle='--', marker='s', markersize=8, linewidth=2)
plt.plot(years, bibliotheque_france_visitors, label='Bibliothèque Nationale de France', color='darkgreen', linestyle='-.', marker='d', markersize=8, linewidth=2)

# Title and axis labels
plt.title('Rise and Fall of the Great Libraries:\nA Journey Through Time (1900-2000)', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Annual Visitors (thousands)', fontsize=14)

# Adding a legend
plt.legend(title='Library', loc='upper right', fontsize=12, title_fontsize=13)

# Adding grid lines for better visualization
plt.grid(True, linestyle='--', alpha=0.6)

# Set tick parameters for better clarity
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 301, 50))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()