import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2000 to 2025
years = np.array(range(2000, 2026))

# Data for Internet users in millions for each continent
north_america_users = np.array([95, 110, 135, 160, 185, 200, 220, 235, 260, 280, 310, 340, 370, 395, 420, 440, 460, 480, 500, 520, 530, 540, 555, 570, 585, 600])
europe_users = np.array([110, 125, 145, 175, 200, 220, 240, 260, 290, 320, 350, 380, 410, 440, 470, 490, 510, 530, 550, 570, 590, 610, 625, 640, 660, 680])
asia_users = np.array([140, 180, 230, 280, 340, 400, 470, 550, 640, 740, 850, 960, 1080, 1200, 1330, 1470, 1610, 1760, 1920, 2080, 2250, 2430, 2600, 2780, 2970, 3150])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the data
ax.plot(years, north_america_users, marker='o', linestyle='-', color='blue', linewidth=2, label='North America')
ax.plot(years, europe_users, marker='^', linestyle='--', color='green', linewidth=2, label='Europe')
ax.plot(years, asia_users, marker='s', linestyle='-.', color='orange', linewidth=2, label='Asia')

# Set the title and labels
ax.set_title('Growth of Internet Users Across Continents\n(2000-2025)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Internet Users (Millions)', fontsize=14)

# Annotations for significant growth milestones
milestone_years = [2005, 2010, 2015, 2020]
for year in milestone_years:
    idx = np.where(years == year)[0][0]
    ax.annotate(f'{north_america_users[idx]}M', (year, north_america_users[idx]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=9, color='blue')
    ax.annotate(f'{europe_users[idx]}M', (year, europe_users[idx]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=9, color='green')
    ax.annotate(f'{asia_users[idx]}M', (year, asia_users[idx]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=9, color='orange')

# Set x and y ticks
ax.set_xticks(years[::2])
ax.set_yticks(range(0, 3500, 250))

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Add legend to distinguish between continents
ax.legend(title='Continent', fontsize=12)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()