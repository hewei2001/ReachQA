import matplotlib.pyplot as plt
import numpy as np

# Define more granular time points (annual data)
years = np.arange(2010, 2031)

# Define the number of internet users in millions for each continent/sub-region with more complex patterns
africa_north_users = np.array([110, 130, 155, 180, 210, 250, 310, 380, 440, 480, 520, 570, 620, 680, 740, 800, 860, 920, 980, 1040, 1100])
africa_south_users = np.array([30, 40, 60, 90, 120, 160, 200, 250, 310, 380, 450, 510, 580, 650, 720, 790, 860, 930, 1000, 1070, 1150])
asia_users = np.array([820, 860, 900, 950, 1000, 1060, 1130, 1210, 1300, 1400, 1520, 1660, 1810, 1970, 2150, 2350, 2580, 2820, 3080, 3360, 3650])
europe_users = np.array([500, 510, 520, 530, 540, 550, 570, 590, 610, 640, 670, 690, 710, 730, 740, 750, 760, 765, 770, 775, 780])
north_america_users = np.array([270, 275, 280, 285, 290, 295, 300, 310, 315, 320, 325, 330, 335, 338, 340, 345, 348, 350, 352, 353, 355])
south_america_users = np.array([160, 170, 185, 200, 220, 250, 280, 320, 360, 400, 440, 480, 510, 530, 550, 570, 590, 610, 630, 650, 670])
australia_users = np.array([30, 32, 34, 36, 38, 40, 42, 45, 48, 51, 54, 58, 62, 65, 68, 70, 72, 73, 74, 75, 76])

# Aggregate additional regions for Africa
africa_users = africa_north_users + africa_south_users

# Colors for each continent
colors = ['#FFD700', '#FF4500', '#8A2BE2', '#00FF00', '#1E90FF', '#FF69B4']

# Create the plot
plt.figure(figsize=(16, 9))

# Plot the stacked area chart with more sub-regions
plt.stackplot(years, africa_users, asia_users, europe_users, north_america_users, south_america_users, australia_users, 
              labels=['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Australia'], colors=colors, alpha=0.8)

# Set title and labels with multi-line title
plt.title('Evolution of Internet Users by Continent\n(Annual Data from 2010-2030)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Internet Users (Millions)', fontsize=12)

# Add a legend to describe each continent
plt.legend(title='Continent', title_fontsize=12, fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))

# Add a grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Rotate x-axis labels to avoid overlap
plt.xticks(years, rotation=45)

# Annotate key trends
plt.annotate('Rapid Growth in Asia', xy=(2023, 2900), xytext=(2025, 2500), 
             arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10, color='darkred')

# Optimize layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()