import matplotlib.pyplot as plt
import numpy as np

# Leagues
leagues = ['NFL', 'MLB', 'NBA', 'EPL', 'La Liga', 'Bundesliga']

# Revenue in billions USD for each year (2020, 2021, 2022)
revenue_2020 = np.array([12.2, 10.7, 8.3, 5.3, 4.5, 4.2])
revenue_2021 = np.array([12.6, 10.9, 8.5, 5.6, 4.7, 4.4])
revenue_2022 = np.array([13.0, 11.2, 9.0, 6.0, 5.0, 4.7])

# Set up the bar chart
x = np.arange(len(leagues))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots(figsize=(12, 8))

# Plotting bars for each year
rects1 = ax.bar(x - width, revenue_2020, width, label='2020', color='#1f77b4', edgecolor='black')
rects2 = ax.bar(x, revenue_2021, width, label='2021', color='#ff7f0e', edgecolor='black')
rects3 = ax.bar(x + width, revenue_2022, width, label='2022', color='#2ca02c', edgecolor='black')

# Adding labels and title
ax.set_xlabel('Sports Leagues', fontsize=14)
ax.set_ylabel('Revenue (Billion USD)', fontsize=14)
ax.set_title('Annual Revenue from Top Global Sports Leagues\n(2020-2022)', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(leagues, rotation=45, ha='right')
ax.legend()

# Add y-axis grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Annotate bars with their value
def annotate_bars(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.1f}', 
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, color='black')

annotate_bars(rects1)
annotate_bars(rects2)
annotate_bars(rects3)

# Automatically adjust layout to fit everything neatly
plt.tight_layout()

# Display the bar chart
plt.show()