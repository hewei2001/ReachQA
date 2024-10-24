import matplotlib.pyplot as plt
import numpy as np

# Publishers
publishers = ['Poetry House', 'Verse City', 'Stanza Street', 'Rhyme Realm']

# Years
years = np.array([2015, 2016, 2017, 2018, 2019, 2020])

# Average number of poetry books published per year per publisher
avg_publications = {
    'Poetry House': [120, 135, 150, 170, 180, 190],
    'Verse City': [90, 105, 120, 130, 140, 155],
    'Stanza Street': [60, 75, 95, 110, 125, 140],
    'Rhyme Realm': [50, 55, 65, 75, 85, 100]
}

# Margin of error for each publisher
error_margin = {
    'Poetry House': [5, 7, 8, 10, 10, 12],
    'Verse City': [6, 7, 8, 9, 11, 13],
    'Stanza Street': [4, 5, 6, 7, 8, 9],
    'Rhyme Realm': [3, 4, 4, 5, 6, 7]
}

# Calculate the total publications each year
total_publications_per_year = [sum(year_data) for year_data in zip(*avg_publications.values())]

# Calculate percentage contribution of each publisher per year
percentage_contributions = {}
for publisher, counts in avg_publications.items():
    percentage_contributions[publisher] = [(count / total) * 100 for count, total in zip(counts, total_publications_per_year)]

# Create the subplots
fig, ax = plt.subplots(1, 2, figsize=(14, 7))

# Colors and styles
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']
line_styles = ['-', '--', '-.', ':']

# Plot the original line chart with error bars
for idx, publisher in enumerate(publishers):
    ax[0].errorbar(
        years, 
        avg_publications[publisher], 
        yerr=error_margin[publisher], 
        label=publisher, 
        fmt=line_styles[idx] + 'o', 
        color=colors[idx], 
        ecolor='gray', 
        elinewidth=2,
        capsize=5, 
        capthick=1.5, 
        alpha=0.9
    )

ax[0].set_title("Annual Growth in Poetry Publications\nfrom Major Literary Publishers (2015-2020)", fontsize=14, fontweight='bold')
ax[0].set_xlabel("Year", fontsize=12)
ax[0].set_ylabel("Number of Books Published", fontsize=12)
ax[0].legend(title="Publisher", fontsize=10, loc='upper left')
ax[0].grid(True, linestyle='--', alpha=0.6)
ax[0].set_ylim(40, 200)

# Plot the new stacked bar chart
bar_width = 0.2
r = np.arange(len(years))

for idx, publisher in enumerate(publishers):
    ax[1].bar(
        r + idx * bar_width,
        percentage_contributions[publisher],
        width=bar_width,
        color=colors[idx],
        label=publisher,
        alpha=0.8
    )

ax[1].set_title("Percentage Contribution by Publishers\n(2015-2020)", fontsize=14, fontweight='bold')
ax[1].set_xlabel("Year", fontsize=12)
ax[1].set_ylabel("Percentage (%)", fontsize=12)
ax[1].set_xticks(r + bar_width * (len(publishers) / 2 - 0.5))
ax[1].set_xticklabels(years)
ax[1].legend(title="Publisher", fontsize=10, loc='upper left')
ax[1].grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()