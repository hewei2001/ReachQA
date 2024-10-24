import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2015 to 2025
years = np.arange(2015, 2026)

# Number of tournaments per year for each genre
moba_tournaments = [60, 65, 70, 75, 80, 100, 110, 115, 120, 130, 135]
fps_tournaments = [40, 45, 50, 60, 70, 80, 85, 90, 95, 100, 105]
battle_royale_tournaments = [5, 10, 20, 30, 50, 70, 90, 110, 130, 150, 170]
rts_tournaments = [50, 48, 45, 43, 40, 38, 36, 34, 32, 30, 28]
fighting_tournaments = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

# Calculate average number of tournaments per year for new subplot
avg_tournaments = np.mean([moba_tournaments, fps_tournaments, battle_royale_tournaments, rts_tournaments, fighting_tournaments], axis=0)

# Initialize the plot with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7), gridspec_kw={'width_ratios': [3, 2]})

# Stacked bar chart plotting in the first subplot
bar_width = 0.6

ax1.bar(years, moba_tournaments, bar_width, label='MOBA', color='#FF5733')
ax1.bar(years, fps_tournaments, bar_width, bottom=moba_tournaments, label='FPS', color='#33FF57')
ax1.bar(years, battle_royale_tournaments, bar_width,
       bottom=np.array(moba_tournaments) + np.array(fps_tournaments),
       label='Battle Royale', color='#3357FF')
ax1.bar(years, rts_tournaments, bar_width,
       bottom=np.array(moba_tournaments) + np.array(fps_tournaments) + np.array(battle_royale_tournaments),
       label='RTS', color='#FF33A3')
ax1.bar(years, fighting_tournaments, bar_width,
       bottom=np.array(moba_tournaments) + np.array(fps_tournaments) +
       np.array(battle_royale_tournaments) + np.array(rts_tournaments),
       label='Fighting', color='#F3FF33')

ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Number of Tournaments', fontsize=12, fontweight='bold')
ax1.set_title('Rise of Gaming Genres in Esports\n2015 to 2025', fontsize=16, fontweight='bold')
ax1.legend(loc='upper left', title='Game Genre', title_fontsize='12', fontsize=10)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, ha='right')

# Display data values on top of the bars
for idx, year in enumerate(years):
    total_height = 0
    for height in [moba_tournaments, fps_tournaments, battle_royale_tournaments, rts_tournaments, fighting_tournaments]:
        bar_height = height[idx]
        ax1.text(year, total_height + bar_height / 2, f'{bar_height}', ha='center', va='center', color='white', fontsize=8, fontweight='bold')
        total_height += bar_height

# Line plot of average tournaments in the second subplot
ax2.plot(years, avg_tournaments, marker='o', linestyle='-', color='purple', linewidth=2, label='Average Tournaments')
ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_ylabel('Average Number of Tournaments', fontsize=12, fontweight='bold')
ax2.set_title('Average Tournaments per Year', fontsize=14, fontweight='bold')
ax2.grid(linestyle='--', alpha=0.7)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45, ha='right')
ax2.legend(loc='upper left', fontsize=10)

# Apply tight layout for optimal viewing
plt.tight_layout()

# Display the chart
plt.show()