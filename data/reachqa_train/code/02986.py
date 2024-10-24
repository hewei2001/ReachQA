import numpy as np
import matplotlib.pyplot as plt

# Define the years and genres
years = np.arange(2013, 2023)
genres = ['Science Fiction', 'Fantasy', 'Mystery']

# Fictional data representing popularity scores
sci_fi_popularity = [60, 64, 67, 66, 68, 72, 74, 76, 78, 80]
fantasy_popularity = [55, 58, 60, 64, 67, 70, 73, 75, 77, 79]
mystery_popularity = [65, 67, 66, 65, 68, 70, 69, 71, 74, 76]

# Create the line chart
plt.figure(figsize=(12, 8))

# Plot each genre with distinct styles
plt.plot(years, sci_fi_popularity, label='Science Fiction', color='#1f77b4', linestyle='-', marker='o', markersize=8, linewidth=2)
plt.plot(years, fantasy_popularity, label='Fantasy', color='#ff7f0e', linestyle='--', marker='s', markersize=8, linewidth=2)
plt.plot(years, mystery_popularity, label='Mystery', color='#2ca02c', linestyle=':', marker='D', markersize=8, linewidth=2)

# Enhance plot with titles and labels
plt.title('Decadal Trends in Book Genre Popularity\n(2013-2022)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Popularity Score', fontsize=12)

# Adding grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Adding legend to differentiate between genres
plt.legend(title='Book Genres', fontsize=10)

# Annotate peak popularity points
for year, score in zip(years, sci_fi_popularity):
    if score == max(sci_fi_popularity):
        plt.annotate(f'{score}', xy=(year, score), xytext=(year-0.5, score + 2),
                     textcoords='offset points', arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)

for year, score in zip(years, fantasy_popularity):
    if score == max(fantasy_popularity):
        plt.annotate(f'{score}', xy=(year, score), xytext=(year-0.5, score + 2),
                     textcoords='offset points', arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)

for year, score in zip(years, mystery_popularity):
    if score == max(mystery_popularity):
        plt.annotate(f'{score}', xy=(year, score), xytext=(year-0.5, score + 2),
                     textcoords='offset points', arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)

# Adjust layout for clarity and show the plot
plt.tight_layout()
plt.show()