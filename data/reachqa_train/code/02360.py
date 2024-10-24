import matplotlib.pyplot as plt
import numpy as np

# Continents and corresponding data for renewable energy sources
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
solar = [32, 41, 36, 44, 27, 52]  # Solar energy percentage
wind = [28, 22, 32, 33, 22, 27]   # Wind energy percentage
hydro = [30, 24, 22, 14, 38, 12]  # Hydro energy percentage
geothermal = [10, 13, 10, 9, 13, 9]  # Geothermal energy percentage

# Stacking the data for the bar plot
ind = np.arange(len(continents))  # x locations for the groups
width = 0.6  # width of the bars

fig, ax = plt.subplots(figsize=(12, 8))

# Plot each energy source
p1 = ax.bar(ind, solar, width, label='Solar', color='#FFD700')
p2 = ax.bar(ind, wind, width, bottom=solar, label='Wind', color='#87CEFA')
p3 = ax.bar(ind, hydro, width, bottom=np.array(solar) + np.array(wind), label='Hydro', color='#32CD32')
p4 = ax.bar(ind, geothermal, width, bottom=np.array(solar) + np.array(wind) + np.array(hydro), label='Geothermal', color='#FF7F50')

# Title and labels
ax.set_title('Renewable Energy Adoption\nAcross Continents (2023)', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Continents', fontsize=14, weight='bold')
ax.set_ylabel('Percentage of Total Energy Generation', fontsize=14, weight='bold')
ax.set_xticks(ind)
ax.set_xticklabels(continents, fontsize=12, weight='bold', rotation=30, ha='right')
ax.set_ylim(0, 120)  # Allowing some space above the bars

# Legend configuration
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10, title='Energy Sources')

# Data labels for each segment of the stacked bar
def add_value_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}%',
                    xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                    xytext=(0, 0),  # Offset
                    textcoords="offset points",
                    ha='center', va='center', fontsize=9, color='black')

# Adding labels
for bars in [p1, p2, p3, p4]:
    add_value_labels(bars)

# Enhancements
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Automatically adjust the subplot to accommodate text and avoid clipping
plt.tight_layout()

# Show the plot
plt.show()