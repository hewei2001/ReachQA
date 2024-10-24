import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2020 to 2030
years = np.arange(2020, 2031)

# Number of works published in each genre from 2020 to 2030
novels_published = 150 * (1.1 ** np.arange(len(years)))
poetry_published = 100 + 20 * np.log1p(np.arange(len(years)))
short_stories_published = 200 + 30 * np.sqrt(np.arange(len(years)))
essays_published = 50 * np.exp(0.1 * np.arange(len(years)))
plays_published = 60 + 40 * np.sin(np.linspace(0, 2 * np.pi, len(years)))

# Initialize the plot with subplots for additional complexity
fig, axs = plt.subplots(2, 1, figsize=(14, 10))

# Main plot showing publications over time
axs[0].plot(years, novels_published, label='Novels', color='#1f77b4', marker='o', linewidth=2, linestyle='-')
axs[0].plot(years, poetry_published, label='Poetry', color='#ff7f0e', marker='^', linewidth=2, linestyle='--')
axs[0].plot(years, short_stories_published, label='Short Stories', color='#2ca02c', marker='s', linewidth=2, linestyle='-.')
axs[0].plot(years, essays_published, label='Essays', color='#d62728', marker='x', linewidth=2, linestyle=':')
axs[0].plot(years, plays_published, label='Plays', color='#9467bd', marker='d', linewidth=2, linestyle='-')

# Titles and labels
axs[0].set_title('A Decade of Diverse Literary Works (2020-2030)', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Number of Works Published', fontsize=12)

# Legend and grid
axs[0].legend(loc='upper left', title='Genre', fontsize=10, frameon=False)
axs[0].grid(True, linestyle='--', alpha=0.6)

# Customize ticks
axs[0].set_xticks(years)
axs[0].set_xticklabels(years, rotation=45)
axs[0].set_yticks(np.arange(0, 801, 100))

# Highlight a significant trend
axs[0].axvline(x=2030, color='gray', linestyle='--', linewidth=0.8, label='Peak Year')

# Annotate notable events
axs[0].annotate('Poetry Boom', xy=(2025, poetry_published[5]), xytext=(2026, 150),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Secondary plot for relative growth percentages
growth_novels = np.diff(novels_published) / novels_published[:-1] * 100
growth_poetry = np.diff(poetry_published) / poetry_published[:-1] * 100
growth_short_stories = np.diff(short_stories_published) / short_stories_published[:-1] * 100
growth_essays = np.diff(essays_published) / essays_published[:-1] * 100
growth_plays = np.diff(plays_published) / plays_published[:-1] * 100

growth_years = years[1:]

axs[1].plot(growth_years, growth_novels, label='Novels Growth %', color='#1f77b4', linestyle='-')
axs[1].plot(growth_years, growth_poetry, label='Poetry Growth %', color='#ff7f0e', linestyle='--')
axs[1].plot(growth_years, growth_short_stories, label='Short Stories Growth %', color='#2ca02c', linestyle='-.')
axs[1].plot(growth_years, growth_essays, label='Essays Growth %', color='#d62728', linestyle=':')
axs[1].plot(growth_years, growth_plays, label='Plays Growth %', color='#9467bd', linestyle='-')

# Titles and labels for the secondary plot
axs[1].set_title('Year-over-Year Growth Percentage by Genre', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Growth Percentage (%)', fontsize=12)

# Legend and grid for the secondary plot
axs[1].legend(loc='upper left', title='Genre', fontsize=10, frameon=False)
axs[1].grid(True, linestyle='--', alpha=0.6)

# Customize ticks for the secondary plot
axs[1].set_xticks(growth_years)
axs[1].set_xticklabels(growth_years, rotation=45)
axs[1].set_yticks(np.arange(-20, 81, 20))

# Adjust layout for clarity and prevent overlap
plt.tight_layout()

# Show the plots
plt.show()