import matplotlib.pyplot as plt
import numpy as np

# Original Data
years = np.arange(2010, 2021)
parks = [15, 16, 18, 20, 23, 25, 28, 30, 34, 37, 40]
urban_gardens = [1, 2, 3, 4, 6, 9, 13, 16, 20, 25, 30]
green_rooftops = [2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 22]

# New data for the second subplot - Number of Initiatives
# These numbers reflect initiatives per year related to each green space type
park_initiatives = [2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]
garden_initiatives = [1, 1, 2, 2, 3, 5, 7, 9, 12, 15, 18]
rooftop_initiatives = [1, 1, 1, 2, 2, 3, 5, 6, 8, 11, 14]

# Set up the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), constrained_layout=True)

# First subplot for green space expansion
ax1.plot(years, parks, label='Parks', marker='o', color='#228B22', linewidth=2, linestyle='-')
ax1.plot(years, urban_gardens, label='Urban Gardens', marker='s', color='#32CD32', linewidth=2, linestyle='--')
ax1.plot(years, green_rooftops, label='Green Rooftops', marker='^', color='#66CDAA', linewidth=2, linestyle='-.')

ax1.annotate('Garden Surge', xy=(2018, 20), xytext=(2015, 25),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center')
ax1.annotate('Rooftop Boom', xy=(2020, 22), xytext=(2017, 20),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center')

ax1.set_title("Growth of Green Spaces\nin Greenopolis (2010-2020)", fontsize=14, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Area in Square Kilometers", fontsize=12)
ax1.legend(title="Type of Green Space", loc='upper left')
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.set_xticks(years)
ax1.tick_params(axis='x', rotation=45)

# Second subplot for number of initiatives
width = 0.25  # width of the bars
x_indexes = np.arange(len(years))

ax2.bar(x_indexes - width, park_initiatives, width=width, label='Parks', color='#228B22')
ax2.bar(x_indexes, garden_initiatives, width=width, label='Urban Gardens', color='#32CD32')
ax2.bar(x_indexes + width, rooftop_initiatives, width=width, label='Green Rooftops', color='#66CDAA')

ax2.set_title("Green Space Initiatives\nfrom 2010 to 2020", fontsize=14, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Number of Initiatives", fontsize=12)
ax2.legend(title="Type of Initiative", loc='upper left')
ax2.set_xticks(x_indexes)
ax2.set_xticklabels(years)
ax2.tick_params(axis='x', rotation=45)
ax2.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Display the plot
plt.show()