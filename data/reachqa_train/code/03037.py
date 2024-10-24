import matplotlib.pyplot as plt
import numpy as np

# Define decades from 1900s to 2020s
decades = np.arange(1900, 2030, 10)

# Hypothetical interest levels in different art styles over the decades
impressionism_interest = [70, 65, 60, 55, 50, 40, 30, 25, 20, 15, 10, 10, 8]
cubism_interest = [5, 10, 20, 40, 60, 75, 65, 50, 40, 35, 30, 25, 20]
surrealism_interest = [2, 5, 10, 20, 30, 50, 70, 80, 75, 60, 50, 40, 30]
abstract_art_interest = [1, 3, 8, 15, 25, 40, 60, 70, 80, 85, 90, 95, 98]

# Create the line chart
plt.figure(figsize=(12, 8))
plt.plot(decades, impressionism_interest, marker='o', label='Impressionism', color='teal', linestyle='--', linewidth=1.5)
plt.plot(decades, cubism_interest, marker='s', label='Cubism', color='crimson', linestyle='-.', linewidth=1.5)
plt.plot(decades, surrealism_interest, marker='^', label='Surrealism', color='darkorange', linestyle=':', linewidth=1.5)
plt.plot(decades, abstract_art_interest, marker='d', label='Abstract Art', color='royalblue', linestyle='-', linewidth=1.5)

# Set axis labels and title
plt.xlabel('Decade', fontsize=12)
plt.ylabel('Interest Level (%)', fontsize=12)
plt.title('Evolution of Art Styles\nOver the Decades', fontsize=16, fontweight='bold')

# Add grid to the plot
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust tick positions and labels
plt.xticks(decades, rotation=45)
plt.yticks(np.arange(0, 101, 10))

# Add a legend to the plot
plt.legend(title='Art Styles', loc='upper left', fontsize=10)

# Use tight_layout to adjust subplot params for a better fit
plt.tight_layout()

# Display the plot
plt.show()