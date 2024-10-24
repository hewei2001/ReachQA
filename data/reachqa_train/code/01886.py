import matplotlib.pyplot as plt
import numpy as np

# Define years and internet user data for each continent
years = np.arange(2000, 2024)

# Internet users in millions for each continent over the years
asia_users = np.array([100, 120, 150, 180, 210, 250, 300, 350, 420, 500, 580, 670, 780, 900, 1030, 1160, 1290, 1400, 1500, 1590, 1670, 1740, 1800, 1850])
europe_users = np.array([120, 130, 140, 150, 160, 170, 185, 195, 205, 215, 225, 235, 245, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300, 305])
north_america_users = np.array([110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196])
south_america_users = np.array([20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100, 110, 125, 145, 165, 185, 205, 225, 245, 265, 285, 300, 315, 330])
africa_users = np.array([5, 7, 10, 15, 22, 30, 40, 52, 65, 85, 110, 145, 190, 250, 320, 400, 500, 610, 720, 830, 940, 1050, 1160, 1270])
oceania_users = np.array([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])

# Stacked data
data = np.array([asia_users, europe_users, north_america_users, south_america_users, africa_users, oceania_users])

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Stacked area chart using stackplot
ax.stackplot(years, asia_users, europe_users, north_america_users, south_america_users, africa_users, oceania_users,
             labels=['Asia', 'Europe', 'North America', 'South America', 'Africa', 'Oceania'],
             colors=['deepskyblue', 'lightgreen', 'gold', 'orange', 'darkviolet', 'firebrick'], alpha=0.8)

# Plot title and labels
ax.set_title("Digital Planet:\nEvolution of Internet Connectivity Across Continents (2000-2023)", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Internet Users (in millions)", fontsize=12)

# Adding legend outside the plot
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10, title='Continents', title_fontsize='12')

# Annotate significant changes
ax.annotate('Surge in Asia', xy=(2015, 1400), xytext=(2010, 1600),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, ha='center')
ax.annotate('Rapid Growth in Africa', xy=(2020, 1200), xytext=(2018, 1350),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, ha='center')

# Grid for better readability
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Rotate x-axis labels for better visibility
plt.xticks(years[::2], rotation=45)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Show the plot
plt.show()