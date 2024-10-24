import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2021)

# Artificial data representing the expansion of green spaces in square kilometers
parks = [15, 16, 18, 20, 23, 25, 28, 30, 34, 37, 40]
urban_gardens = [1, 2, 3, 4, 6, 9, 13, 16, 20, 25, 30]
green_rooftops = [2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 22]

# Set up the figure and axis
plt.figure(figsize=(12, 8))

# Plot each type of green space
plt.plot(years, parks, label='Parks', marker='o', color='#228B22', linewidth=2, linestyle='-')
plt.plot(years, urban_gardens, label='Urban Gardens', marker='s', color='#32CD32', linewidth=2, linestyle='--')
plt.plot(years, green_rooftops, label='Green Rooftops', marker='^', color='#66CDAA', linewidth=2, linestyle='-.')

# Annotate significant growth periods or peaks
plt.annotate('Garden Surge', xy=(2018, 20), xytext=(2015, 25),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, color='black', ha='center')
plt.annotate('Rooftop Boom', xy=(2020, 22), xytext=(2017, 20),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, color='black', ha='center')

# Add titles and labels
plt.title("Growth of Green Spaces in Greenopolis\nfrom 2010 to 2020", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=14)
plt.ylabel("Area in Square Kilometers", fontsize=14)

# Add legend
plt.legend(title="Type of Green Space", loc='upper left')

# Enable grid with specific style
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Rotate x-ticks for clarity
plt.xticks(years, rotation=45)

# Adjust layout to improve clarity
plt.tight_layout()

# Display the plot
plt.show()