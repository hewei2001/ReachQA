import matplotlib.pyplot as plt
import numpy as np

# Define decades and art movement influence data
decades = np.arange(1950, 2030, 10)
modernism = [80, 60, 40, 20, 10, 5, 3, 2]
postmodernism = [10, 20, 40, 60, 70, 65, 60, 55]
digital_art = [0, 0, 0, 10, 20, 35, 40, 45]
contemporary_art = [5, 10, 15, 20, 25, 30, 35, 40]

# Setup the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Create the stacked area plot
ax.stackplot(decades, modernism, postmodernism, digital_art, contemporary_art, 
             labels=['Modernism', 'Postmodernism', 'Digital Art', 'Contemporary Art'], 
             colors=['#B0C4DE', '#FFB6C1', '#9370DB', '#98FB98'], alpha=0.85)

# Title and labels
ax.set_title('The Evolution of Art Movements: 1950s to 2020s', fontsize=16, weight='bold')
ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('Influence (Arbitrary Units)', fontsize=12)

# Legend
ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1))

# Grid and layout
ax.grid(True, linestyle='--', alpha=0.5)
plt.xlim([1950, 2020])
plt.xticks(decades, rotation=45)
plt.tight_layout()

# Annotations for significant periods
ax.annotate('Rise of Postmodernism', xy=(1970, 45), xytext=(1980, 65),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='black')
ax.annotate('Digital Era Emerges', xy=(1990, 10), xytext=(2000, 30),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='black')

# Show the plot
plt.show()