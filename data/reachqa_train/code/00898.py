import matplotlib.pyplot as plt
import numpy as np

# Data for the years 2010 to 2020
years = np.arange(2010, 2021)

# Fictional data representing the number of published titles for each fantasy sub-genre
epic_fantasy = [50, 55, 60, 70, 85, 100, 120, 140, 160, 180, 200]
urban_fantasy = [30, 35, 40, 50, 60, 70, 85, 95, 110, 130, 150]
historical_fantasy = [20, 25, 28, 32, 40, 45, 55, 65, 78, 90, 100]
magical_realism = [15, 18, 25, 28, 30, 35, 42, 50, 60, 70, 80]
dark_fantasy = [10, 12, 15, 20, 25, 30, 40, 50, 60, 75, 90]

data = np.array([epic_fantasy, urban_fantasy, historical_fantasy, magical_realism, dark_fantasy])

# Calculate average growth rates over the decade for each sub-genre
avg_growth = np.diff(data).mean(axis=1)

# Projected data for the next five years based on average growth rates
future_years = np.arange(2021, 2026)
epic_future = [epic_fantasy[-1] + avg_growth[0] * i for i in range(1, 6)]
urban_future = [urban_fantasy[-1] + avg_growth[1] * i for i in range(1, 6)]
historical_future = [historical_fantasy[-1] + avg_growth[2] * i for i in range(1, 6)]
magical_future = [magical_realism[-1] + avg_growth[3] * i for i in range(1, 6)]
dark_future = [dark_fantasy[-1] + avg_growth[4] * i for i in range(1, 6)]

# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(16, 8))

# Stacked area plot for 2010-2020
ax[0].stackplot(years, data, labels=['Epic Fantasy', 'Urban Fantasy', 'Historical Fantasy', 'Magical Realism', 'Dark Fantasy'],
                colors=['#4B0082', '#FF6347', '#FFD700', '#ADFF2F', '#2E8B57'], alpha=0.8)
ax[0].set_title("A Decade of Rising Fantasy:\nGenre Popularity in Fiction (2010-2020)", fontsize=14, fontweight='bold')
ax[0].set_xlabel('Year', fontsize=12)
ax[0].set_ylabel('Number of Published Titles', fontsize=12)
ax[0].legend(loc='upper left', title="Fantasy Sub-genres", fontsize=10)
ax[0].annotate('Surge in Epic Fantasy', xy=(2015, 100), xytext=(2013, 250),
               arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, fontweight='bold')
ax[0].annotate('Plateau in Urban Fantasy', xy=(2014, 75), xytext=(2016, 50),
               arrowprops=dict(facecolor='grey', arrowstyle='->'), fontsize=10, fontweight='bold')

# Line plot for projected data (2021-2025)
ax[1].plot(future_years, epic_future, label='Epic Fantasy', color='#4B0082', linestyle='--', marker='o')
ax[1].plot(future_years, urban_future, label='Urban Fantasy', color='#FF6347', linestyle='--', marker='o')
ax[1].plot(future_years, historical_future, label='Historical Fantasy', color='#FFD700', linestyle='--', marker='o')
ax[1].plot(future_years, magical_future, label='Magical Realism', color='#ADFF2F', linestyle='--', marker='o')
ax[1].plot(future_years, dark_future, label='Dark Fantasy', color='#2E8B57', linestyle='--', marker='o')
ax[1].set_title("Projected Genre Growth\n(2021-2025)", fontsize=14, fontweight='bold')
ax[1].set_xlabel('Year', fontsize=12)
ax[1].set_ylabel('Number of Published Titles', fontsize=12)
ax[1].legend(loc='upper left', fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()