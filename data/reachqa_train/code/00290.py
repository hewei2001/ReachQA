import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Artificial data for internet usage growth (% of population using internet)
africa_internet = [10, 13, 17, 22, 28, 33, 39, 45, 52, 59, 65]
asia_internet = [20, 25, 30, 37, 44, 50, 58, 65, 72, 78, 84]
europe_internet = [60, 63, 66, 69, 72, 76, 79, 83, 86, 88, 91]
north_america_internet = [70, 73, 75, 78, 80, 82, 84, 86, 88, 89, 90]
south_america_internet = [40, 44, 48, 53, 59, 64, 68, 73, 78, 82, 86]

# Combine the datasets into a single 2D array for the stackplot function
internet_usage = np.array([
    africa_internet, 
    asia_internet, 
    europe_internet, 
    north_america_internet, 
    south_america_internet
])

# Create a new figure and axis with a specific size
fig, ax = plt.subplots(figsize=(12, 8))

# Use the stackplot function to create the stacked area chart
ax.stackplot(years, internet_usage, labels=['Africa', 'Asia', 'Europe', 'North America', 'South America'], 
             colors=['gold', 'lightcoral', 'lightblue', 'lightgreen', 'thistle'], alpha=0.8)

# Set chart title with a line break for clarity
ax.set_title("Decade of Digital Growth:\nInternet Adoption Across Continents (2010-2020)", fontsize=16, fontweight='bold')

# Label the x and y axes
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Internet Users (% of Population)", fontsize=12)

# Add a legend to describe the data clearly
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Continents')

# Add grid lines for better readability
ax.grid(alpha=0.3)

# Rotate x-axis labels to prevent overlap
plt.xticks(rotation=45)

# Adjust layout to avoid clipping of text and ensure no elements overlap
plt.tight_layout()

# Display the final plot
plt.show()