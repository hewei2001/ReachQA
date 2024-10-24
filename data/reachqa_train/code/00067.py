import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Artificial data for language preferences in percentage for each year
oceania = [30, 28, 27, 25, 23, 20, 18, 17, 15, 14, 12]
technotalk = [5, 8, 12, 15, 18, 22, 25, 28, 30, 33, 35]
olden = [40, 37, 34, 30, 26, 22, 18, 15, 12, 10, 8]
mixtrix = [10, 12, 15, 18, 20, 22, 24, 25, 26, 27, 28]
galzonia = [15, 15, 12, 12, 13, 14, 15, 15, 17, 16, 17]

# Combine datasets for stackplot
language_preferences = np.array([oceania, technotalk, olden, mixtrix, galzonia])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(14, 10))

# Using a Seaborn color palette for better distinction
palette = sns.color_palette("husl", 5)

# Create the stackplot
ax.stackplot(years, language_preferences, labels=['Oceania', 'Technotalk', 'Olden', 'Mixtrix', 'Galzonia'],
             colors=palette, alpha=0.85)

# Add titles and labels with multi-line
ax.set_title("Language Preferences Over Time\nin the Archipelago of Linguaterra (2010-2020)", fontsize=18, fontweight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Percentage of Population (%)", fontsize=14)

# Customize the legend
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Language', fontsize=12)

# Enhance gridlines
ax.grid(alpha=0.4, linestyle='--')

# Add trend lines for each language
for i, language in enumerate(language_preferences):
    ax.plot(years, language, label=f"{i}_trend", color=palette[i], linewidth=1.5, linestyle='dashed')

# Annotate the most dominant language in 2010 and 2020
dominant_2010 = np.argmax(language_preferences[:, 0])
dominant_2020 = np.argmax(language_preferences[:, -1])

ax.text(2010, language_preferences[dominant_2010, 0] + 2,
        f"Dominant: {['Oceania', 'Technotalk', 'Olden', 'Mixtrix', 'Galzonia'][dominant_2010]}",
        fontsize=10, fontweight='bold', color=palette[dominant_2010])

ax.text(2020, language_preferences[dominant_2020, -1] + 2,
        f"Dominant: {['Oceania', 'Technotalk', 'Olden', 'Mixtrix', 'Galzonia'][dominant_2020]}",
        fontsize=10, fontweight='bold', color=palette[dominant_2020])

# Make layout tight and show the plot
plt.tight_layout()
plt.show()