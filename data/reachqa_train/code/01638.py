import matplotlib.pyplot as plt

# Data: Authors and number of languages their most famous work has been translated into
authors = [
    "García Márquez\n'One Hundred Years of Solitude'",
    "J.K. Rowling\n'Harry Potter'",
    "Saint-Exupéry\n'The Little Prince'",
    "Cervantes\n'Don Quixote'",
    "Tolstoy\n'War and Peace'"
]
translations = [44, 80, 300, 50, 49]

# New Data: Hypothetical publication years to overlay as a line plot
publication_years = [1967, 1997, 1943, 1605, 1869]

# Create a figure and axis for the bar chart and line plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Create horizontal bar chart
colors = ['#FFDD44', '#77AAFF', '#FF7777', '#33DDDD', '#AA77FF']
bars = ax1.barh(authors, translations, color=colors, height=0.6)

# Set labels for the bar chart
ax1.set_xlabel("Number of Languages", fontsize=12)
ax1.set_ylabel("Authors & Their Famous Works", fontsize=12)
ax1.set_title("Global Reach of Famous Literary Works\nMeasured by Number of Languages Translated",
              fontsize=16, weight='bold', pad=20)
ax1.grid(axis='x', linestyle='--', alpha=0.7)
ax1.tick_params(axis='y', which='major', labelsize=11)
ax1.set_xlim(0, max(translations) + 50)

# Adding value annotations to each bar
for bar in bars:
    ax1.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
             f'{int(bar.get_width())}', va='center', fontsize=10, color='black')

# Create a secondary y-axis for the line plot
ax2 = ax1.twiny()
ax2.plot(publication_years, range(len(authors)), marker='o', color='grey', linestyle='--', linewidth=2, label='Publication Year')
ax2.set_xlim(1600, 2020)
ax2.set_xlabel("Publication Year", fontsize=12)
ax2.invert_yaxis()

# Adding annotations to line plot
for i, (year, author) in enumerate(zip(publication_years, authors)):
    ax2.annotate(f"{year}", (year, i), textcoords="offset points", xytext=(-10, -10), ha='center', fontsize=9)

# Add legend
ax2.legend(loc='upper right', fontsize=10)

# Adjust layout to avoid text clipping and ensure readability
plt.tight_layout()

# Show the plot
plt.show()