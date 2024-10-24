import matplotlib.pyplot as plt
import numpy as np

# Define the time points (years)
years = np.array([2010, 2015, 2020, 2025, 2030])

# Define the number of internet users in millions for each continent
africa_users = np.array([110, 190, 310, 480, 700])
asia_users = np.array([820, 1100, 1500, 2100, 2800])
europe_users = np.array([500, 580, 650, 710, 760])
north_america_users = np.array([270, 300, 320, 340, 350])
south_america_users = np.array([160, 220, 300, 370, 450])
australia_users = np.array([30, 40, 55, 65, 75])

# Colors for each continent
colors = ['#FFD700', '#FF4500', '#8A2BE2', '#00FF00', '#1E90FF', '#FF69B4']

# Create the plot
plt.figure(figsize=(14, 8))

# Plot the stacked area chart
plt.stackplot(years, africa_users, asia_users, europe_users, north_america_users, south_america_users, australia_users, 
              labels=['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Australia'], colors=colors, alpha=0.8)

# Set title and labels
plt.title('Evolution of Internet Users\nby Continent (2010-2030)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Internet Users (Millions)', fontsize=12)

# Add a legend to describe each continent
plt.legend(title='Continent', title_fontsize=12, fontsize=10, loc='upper left')

# Add a grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Rotate x-axis labels to avoid overlap
plt.xticks(years, rotation=45)

# Optimize layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()