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

# Calculate percentage growth for each continent (simplified calculation)
def calculate_growth(data):
    growth = np.zeros_like(data)
    growth[1:] = ((data[1:] - data[:-1]) / data[:-1]) * 100
    return growth

asia_growth = calculate_growth(asia_users)
europe_growth = calculate_growth(europe_users)
north_america_growth = calculate_growth(north_america_users)
south_america_growth = calculate_growth(south_america_users)
africa_growth = calculate_growth(africa_users)
oceania_growth = calculate_growth(oceania_users)

# Create the subplot layout
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Stacked area chart
axes[0].stackplot(years, asia_users, europe_users, north_america_users, south_america_users, africa_users, oceania_users,
                  labels=['Asia', 'Europe', 'North America', 'South America', 'Africa', 'Oceania'],
                  colors=['deepskyblue', 'lightgreen', 'gold', 'orange', 'darkviolet', 'firebrick'], alpha=0.8)
axes[0].set_title("Digital Planet:\nEvolution of Internet Connectivity Across Continents (2000-2023)", fontsize=16, weight='bold', pad=20)
axes[0].set_xlabel("Year", fontsize=12)
axes[0].set_ylabel("Internet Users (in millions)", fontsize=12)
axes[0].legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10, title='Continents', title_fontsize='12')
axes[0].annotate('Surge in Asia', xy=(2015, 1400), xytext=(2010, 1600),
                 arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center')
axes[0].annotate('Rapid Growth in Africa', xy=(2020, 1200), xytext=(2018, 1350),
                 arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center')
axes[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Rotate x-axis labels
axes[0].set_xticks(years[::2])
axes[0].set_xticklabels(years[::2], rotation=45)

# Bar chart for growth rates
width = 0.35
positions = np.arange(len(years) - 1)

axes[1].bar(positions, asia_growth[1:], width, label='Asia', color='deepskyblue')
axes[1].bar(positions + width, africa_growth[1:], width, label='Africa', color='darkviolet')
axes[1].set_title('Annual Growth Rate of Internet Users (2001-2023)', fontsize=14, weight='bold')
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Growth Rate (%)', fontsize=12)
axes[1].set_xticks(positions + width / 2)
axes[1].set_xticklabels(years[1:], rotation=45)
axes[1].legend(loc='best', fontsize=10)
axes[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()