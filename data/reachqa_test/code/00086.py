import matplotlib.pyplot as plt
import numpy as np

# Data for the donut chart: Popularity of programming languages in 2023
languages = ['Python', 'JavaScript', 'Java', 'C#', 'C++', 'Ruby']
percentages = [29, 24, 17, 13, 11, 6]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Data for the bar chart: Growth rates over the past five years
years = ['2018', '2019', '2020', '2021', '2022']
growth_rates = {
    'Python': [8, 10, 15, 18, 20],
    'JavaScript': [7, 8, 9, 12, 15],
    'Java': [5, 6, 7, 8, 9],
    'C#': [4, 5, 6, 6, 7],
    'C++': [3, 3.5, 4, 5, 6],
    'Ruby': [1, 1.5, 2, 2.5, 3],
}

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Donut chart
wedges, texts, autotexts = ax1.pie(
    percentages,
    labels=languages,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    explode=[0.05] * len(languages),
    shadow=True
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax1.add_artist(centre_circle)
ax1.axis('equal')  
ax1.set_title("Popularity of Programming Languages in 2023", fontsize=14, weight='bold')

for text in autotexts:
    text.set_color('white')
    text.set_weight('bold')
    text.set_size(10)

# Bar chart for growth rates
bar_width = 0.15
x = np.arange(len(years))
for i, language in enumerate(languages):
    ax2.bar(x + i * bar_width, growth_rates[language], width=bar_width, label=language, color=colors[i])

ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.set_title('Growth Rates of Programming Languages (2018-2022)', fontsize=14, weight='bold')
ax2.set_xticks(x + bar_width * (len(languages) - 1) / 2)
ax2.set_xticklabels(years)
ax2.legend(title='Languages', loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()