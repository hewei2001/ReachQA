import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2025
years = np.arange(2000, 2026)

# Hypothetical annual revenues in billions of dollars
revenues = np.array([
    18.5, 19.0, 18.8, 19.1, 19.3, 19.5, 20.1, 21.0, 21.7, 21.3,
    22.0, 22.5, 23.0, 23.5, 23.8, 24.2, 25.0, 25.5, 25.9, 26.3,
    26.7, 27.2, 27.5, 28.0, 28.7, 29.0
])

# Hypothetical error values (uncertainty range) in billions of dollars
errors = np.concatenate([
    np.full(21, 0.2),
    np.array([0.5, 0.6, 0.8, 1.0, 1.2])
])

# Hypothetical number of books published annually in millions
books_published = np.array([
    200, 205, 210, 215, 220, 225, 230, 240, 245, 248,
    250, 255, 260, 265, 270, 275, 280, 290, 300, 310,
    320, 330, 340, 350, 360, 370
])

# Create the figure and axis objects
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the revenue line chart with error bars
ax1.errorbar(
    years, revenues, yerr=errors, fmt='o-', color='tab:blue', ecolor='lightgray',
    elinewidth=3, capsize=4, alpha=0.7, label='Revenue with Uncertainty'
)
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Revenues (Billions USD)", fontsize=14, color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.set_xticks(years[::2])
ax1.set_xticklabels(years[::2], rotation=45)
ax1.set_yticks(np.arange(18, 31, 1))
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Add annotations
ax1.annotate(
    'Digital Revolution', xy=(2008, 21.3), xytext=(2005, 20.0),
    arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
    fontsize=11, fontstyle='italic'
)
ax1.annotate(
    'COVID-19 Impact', xy=(2020, 26.7), xytext=(2017, 28.0),
    arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
    fontsize=11, fontstyle='italic'
)

# Create a secondary y-axis for the number of books published
ax2 = ax1.twinx()
ax2.bar(years, books_published, alpha=0.3, color='tab:orange', width=0.6, label='Books Published')
ax2.set_ylabel("Books Published (Millions)", fontsize=14, color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')
ax2.set_yticks(np.arange(200, 401, 20))

# Title and legend
plt.title(
    "Historical Trends and Forecasts of Book Publishing\nRevenues and Books Published (2000-2025)",
    fontsize=16, fontweight='bold'
)
fig.tight_layout()
fig.legend(loc='upper left', fontsize=12)

# Display the plot
plt.show()