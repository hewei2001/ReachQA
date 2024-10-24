import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2000 to 2020
years = np.arange(2000, 2021, 4)

# Hypothetical popularity index data for programming languages
python_popularity = [20, 35, 50, 65, 80, 95]
java_popularity = [80, 85, 75, 70, 60, 55]
javascript_popularity = [40, 50, 65, 80, 90, 95]
csharp_popularity = [30, 45, 60, 75, 70, 65]
ruby_popularity = [25, 35, 45, 60, 65, 60]

# Calculate average popularity index for each language
languages = ['Python', 'Java', 'JavaScript', 'C#', 'Ruby']
average_popularity = [
    np.mean(python_popularity),
    np.mean(java_popularity),
    np.mean(javascript_popularity),
    np.mean(csharp_popularity),
    np.mean(ruby_popularity)
]

# Set up the plot with subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 8), gridspec_kw={'width_ratios': [3, 2]})

# First subplot: Line chart of popularity trends
ax1.plot(years, python_popularity, marker='o', linestyle='-', color='#3776AB', linewidth=2, label='Python')
ax1.plot(years, java_popularity, marker='s', linestyle='--', color='#B07219', linewidth=2, label='Java')
ax1.plot(years, javascript_popularity, marker='^', linestyle='-.', color='#F0DB4F', linewidth=2, label='JavaScript')
ax1.plot(years, csharp_popularity, marker='D', linestyle=':', color='#178600', linewidth=2, label='C#')
ax1.plot(years, ruby_popularity, marker='*', linestyle='-', color='#701516', linewidth=2, label='Ruby')

ax1.set_title('Programming Languages Popularity Trends\n(2000-2020)', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Popularity Index', fontsize=14)
ax1.set_xticks(years)
ax1.grid(True, linestyle='--', which='both', color='gray', alpha=0.5)
ax1.legend(title='Languages', loc='upper left', fontsize=12)

ax1.annotate('Python Surges', xy=(2016, 80), xytext=(2008, 85),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='#3776AB')
ax1.annotate('Ruby Peaks', xy=(2012, 60), xytext=(2010, 70),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='#701516')

# Second subplot: Bar chart of average popularity
bar_colors = ['#3776AB', '#B07219', '#F0DB4F', '#178600', '#701516']
ax2.bar(languages, average_popularity, color=bar_colors, alpha=0.7)
ax2.set_title('Average Popularity Index\n(2000-2020)', fontsize=14, weight='bold')
ax2.set_ylabel('Average Index', fontsize=14)

for index, value in enumerate(average_popularity):
    ax2.text(index, value + 1, f'{value:.1f}', ha='center', va='bottom', fontsize=10)

# Layout adjustment
plt.tight_layout()
plt.show()