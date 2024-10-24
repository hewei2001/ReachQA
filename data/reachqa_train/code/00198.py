import numpy as np
import matplotlib.pyplot as plt

# Define the time range for decades
decades = np.arange(1970, 2030, 10)

# Fictional data on music genre popularity (in percentage)
rock = [40, 35, 25, 15, 10, 5]
disco = [20, 25, 10, 5, 0, 0]
pop = [10, 15, 25, 30, 35, 40]
hip_hop = [0, 0, 10, 20, 25, 30]
electronic = [5, 10, 15, 20, 20, 15]
indie = [0, 0, 5, 10, 10, 10]

# Stack the data to plot
stacked_data = np.vstack([rock, disco, pop, hip_hop, electronic, indie])

# Initialize the plot
plt.figure(figsize=(14, 8))

# Create the stacked area chart
plt.stackplot(decades, stacked_data, labels=['Rock', 'Disco', 'Pop', 'Hip Hop', 'Electronic', 'Indie'],
              colors=['#d62728', '#ff7f0e', '#1f77b4', '#9467bd', '#2ca02c', '#8c564b'], alpha=0.7)

# Add title, labels, and a legend
plt.title("Shifting Melodies: Music Genre Popularity\nfrom the 1970s to 2020s", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Decade", fontsize=14)
plt.ylabel("Popularity (%)", fontsize=14)
plt.legend(loc='upper left', fontsize=12, title='Music Genres', bbox_to_anchor=(1.05, 1))

# Add grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Rotate x-axis labels to avoid overlap
plt.xticks(decades)

# Annotate a notable transition
plt.annotate('Rise of Hip Hop', xy=(2000, 20), xytext=(1980, 60),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()