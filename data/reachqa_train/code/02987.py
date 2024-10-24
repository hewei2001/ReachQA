import numpy as np
import matplotlib.pyplot as plt

# Define the years and genres
years = np.arange(2013, 2023)
genres = ['Science Fiction', 'Fantasy', 'Mystery']

# Fictional data representing popularity scores
sci_fi_popularity = [60, 64, 67, 66, 68, 72, 74, 76, 78, 80]
fantasy_popularity = [55, 58, 60, 64, 67, 70, 73, 75, 77, 79]
mystery_popularity = [65, 67, 66, 65, 68, 70, 69, 71, 74, 76]

# Additional data for rate of change (new subplot data)
sci_fi_growth = [sci_fi_popularity[i+1] - sci_fi_popularity[i] for i in range(len(sci_fi_popularity)-1)]
fantasy_growth = [fantasy_popularity[i+1] - fantasy_popularity[i] for i in range(len(fantasy_popularity)-1)]
mystery_growth = [mystery_popularity[i+1] - mystery_popularity[i] for i in range(len(mystery_popularity)-1)]

# Set up the figure with 2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# First subplot: Line Chart of Popularity Scores
ax1.plot(years, sci_fi_popularity, label='Science Fiction', color='#1f77b4', linestyle='-', marker='o', markersize=8, linewidth=2)
ax1.plot(years, fantasy_popularity, label='Fantasy', color='#ff7f0e', linestyle='--', marker='s', markersize=8, linewidth=2)
ax1.plot(years, mystery_popularity, label='Mystery', color='#2ca02c', linestyle=':', marker='D', markersize=8, linewidth=2)
ax1.set_title('Decadal Trends in Book Genre Popularity\n(2013-2022)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Popularity Score', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(title='Book Genres', fontsize=10)

# Annotate peak popularity points
for year, score in zip(years, sci_fi_popularity):
    if score == max(sci_fi_popularity):
        ax1.annotate(f'{score}', xy=(year, score), xytext=(year-0.5, score + 2),
                     textcoords='offset points', arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)

for year, score in zip(years, fantasy_popularity):
    if score == max(fantasy_popularity):
        ax1.annotate(f'{score}', xy=(year, score), xytext=(year-0.5, score + 2),
                     textcoords='offset points', arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)

for year, score in zip(years, mystery_popularity):
    if score == max(mystery_popularity):
        ax1.annotate(f'{score}', xy=(year, score), xytext=(year-0.5, score + 2),
                     textcoords='offset points', arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)

# Second subplot: Bar Chart of Growth Rates
x_indices = np.arange(len(years) - 1)
bar_width = 0.25
ax2.bar(x_indices - bar_width, sci_fi_growth, width=bar_width, label='Science Fiction Growth', color='#1f77b4')
ax2.bar(x_indices, fantasy_growth, width=bar_width, label='Fantasy Growth', color='#ff7f0e')
ax2.bar(x_indices + bar_width, mystery_growth, width=bar_width, label='Mystery Growth', color='#2ca02c')
ax2.set_xticks(x_indices)
ax2.set_xticklabels(years[:-1])
ax2.set_title('Yearly Growth in Popularity Scores', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Growth Rate', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(fontsize=10)

# Adjust layout and display the plots
plt.tight_layout()
plt.show()