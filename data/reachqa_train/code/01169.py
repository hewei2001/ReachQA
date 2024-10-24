import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2020 to 2030
years = np.arange(2020, 2031)

# Number of works published in each genre from 2020 to 2030
novels_published = np.array([150, 165, 180, 195, 210, 230, 250, 275, 300, 325, 350])
poetry_published = np.array([100, 110, 115, 130, 140, 155, 165, 180, 190, 210, 225])
short_stories_published = np.array([200, 220, 240, 260, 280, 300, 320, 340, 365, 390, 415])

# Initialize the plot
plt.figure(figsize=(12, 7))

# Plot lines for each genre with distinct styles
plt.plot(years, novels_published, label='Novels', color='#1f77b4', marker='o', linewidth=2, linestyle='-')
plt.plot(years, poetry_published, label='Poetry', color='#ff7f0e', marker='^', linewidth=2, linestyle='--')
plt.plot(years, short_stories_published, label='Short Stories', color='#2ca02c', marker='s', linewidth=2, linestyle='-.')

# Title and labels
plt.title('The Rise of Prolific Writers:\nA Decade of Literary Excellence (2020-2030)', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Works Published', fontsize=12)

# Legend and grid
plt.legend(loc='upper left', title='Genre', fontsize=10, frameon=False)
plt.grid(True, linestyle='--', alpha=0.6)

# Customize ticks
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 451, 50))

# Highlight a significant trend
plt.axvline(x=2030, color='gray', linestyle='--', linewidth=0.8, label='Peak Year')

# Annotate notable events
plt.annotate('Notable Poetry Boom', xy=(2025, 155), xytext=(2026, 100),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adjust layout for clarity and prevent overlap
plt.tight_layout()

# Show the plot
plt.show()