import matplotlib.pyplot as plt
import numpy as np

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
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, language_preferences, labels=['Oceania', 'Technotalk', 'Olden', 'Mixtrix', 'Galzonia'],
             colors=['skyblue', 'gray', 'tan', 'purple', 'coral'], alpha=0.85)

# Add titles and labels
ax.set_title("Language Preferences Over Time\nin the Archipelago of Linguaterra (2010-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Percentage of Population (%)", fontsize=12)

# Customize the legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Language', fontsize=10)

# Add gridlines for better readability
ax.grid(alpha=0.3)

# Adjust layout for visibility
plt.tight_layout()

# Show the plot
plt.show()