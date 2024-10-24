import matplotlib.pyplot as plt
import numpy as np

# Data for the years 2010 to 2020
years = np.arange(2010, 2021)

# Fictional data representing the number of published titles for each fantasy sub-genre
epic_fantasy = [50, 55, 60, 70, 85, 100, 120, 140, 160, 180, 200]
urban_fantasy = [30, 35, 40, 50, 60, 70, 85, 95, 110, 130, 150]
historical_fantasy = [20, 25, 28, 32, 40, 45, 55, 65, 78, 90, 100]
magical_realism = [15, 18, 25, 28, 30, 35, 42, 50, 60, 70, 80]
dark_fantasy = [10, 12, 15, 20, 25, 30, 40, 50, 60, 75, 90]

# Stacking the data for plotting
data = np.array([epic_fantasy, urban_fantasy, historical_fantasy, magical_realism, dark_fantasy])

# Create a figure for the stacked area chart
plt.figure(figsize=(12, 8))
plt.stackplot(years, data, labels=['Epic Fantasy', 'Urban Fantasy', 'Historical Fantasy', 'Magical Realism', 'Dark Fantasy'], 
              colors=['#4B0082', '#FF6347', '#FFD700', '#ADFF2F', '#2E8B57'], alpha=0.8)

# Adding the title and axis labels
plt.title("A Decade of Rising Fantasy:\nGenre Popularity in Fiction (2010-2020)", fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Published Titles', fontsize=12)

# Add a legend to identify the different sub-genres
plt.legend(loc='upper left', title="Fantasy Sub-genres", fontsize=10, bbox_to_anchor=(1.05, 1))

# Annotate significant changes in trends
plt.annotate('Surge in Epic Fantasy', xy=(2015, 100), xytext=(2013, 250), 
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, fontweight='bold')

plt.annotate('Plateau in Urban Fantasy', xy=(2014, 75), xytext=(2016, 50), 
             arrowprops=dict(facecolor='grey', arrowstyle='->'), fontsize=10, fontweight='bold')

# Improve layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()