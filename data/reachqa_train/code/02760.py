import matplotlib.pyplot as plt
import numpy as np

# Years for x-axis
years = np.arange(1010, 1020)

# Data: number of festivals in different cities
atlantis_festivals = np.array([[5, 4, 3, 2], [6, 5, 4, 3], [7, 5, 5, 3], [8, 6, 5, 4], [6, 5, 4, 3], [5, 5, 3, 4], [6, 6, 4, 3], [7, 5, 5, 4], [8, 5, 6, 5], [9, 6, 6, 4]])
el_dorado_festivals = np.array([[6, 3, 4, 1], [7, 4, 5, 2], [8, 4, 6, 2], [9, 5, 6, 3], [7, 4, 5, 2], [6, 4, 4, 3], [7, 5, 5, 2], [8, 4, 6, 3], [9, 4, 7, 4], [10, 5, 7, 3]])
shangri_la_festivals = np.array([[4, 5, 2, 3], [5, 6, 3, 4], [6, 6, 4, 4], [7, 7, 4, 5], [5, 6, 3, 4], [4, 6, 2, 5], [5, 7, 3, 4], [6, 6, 4, 5], [7, 6, 5, 6], [8, 7, 5, 5]])
avalon_festivals = np.array([[7, 6, 5, 4], [8, 7, 6, 5], [9, 7, 7, 5], [10, 8, 7, 6], [8, 7, 6, 5], [7, 7, 5, 6], [8, 8, 6, 5], [9, 7, 7, 6], [10, 7, 8, 7], [11, 8, 8, 6]])

# Colors for the different festival types
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#40E0D0']

# Creating the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot stacked bars for each city and festival type
ax.bar(years, atlantis_festivals[:, 0], label='Music (Atlantis)', color=colors[0])
ax.bar(years, atlantis_festivals[:, 1], bottom=atlantis_festivals[:, 0], label='Arts (Atlantis)', color=colors[1])
ax.bar(years, atlantis_festivals[:, 2], bottom=np.sum(atlantis_festivals[:, :2], axis=1), label='Sports (Atlantis)', color=colors[2])
ax.bar(years, atlantis_festivals[:, 3], bottom=np.sum(atlantis_festivals[:, :3], axis=1), label='Culinary (Atlantis)', color=colors[3])

ax.bar(years, el_dorado_festivals[:, 0], label='Music (El Dorado)', color=colors[0], hatch='//', alpha=0.8)
ax.bar(years, el_dorado_festivals[:, 1], bottom=el_dorado_festivals[:, 0], label='Arts (El Dorado)', color=colors[1], hatch='//', alpha=0.8)
ax.bar(years, el_dorado_festivals[:, 2], bottom=np.sum(el_dorado_festivals[:, :2], axis=1), label='Sports (El Dorado)', color=colors[2], hatch='//', alpha=0.8)
ax.bar(years, el_dorado_festivals[:, 3], bottom=np.sum(el_dorado_festivals[:, :3], axis=1), label='Culinary (El Dorado)', color=colors[3], hatch='//', alpha=0.8)

ax.bar(years, shangri_la_festivals[:, 0], label='Music (Shangri-La)', color=colors[0], alpha=0.6)
ax.bar(years, shangri_la_festivals[:, 1], bottom=shangri_la_festivals[:, 0], label='Arts (Shangri-La)', color=colors[1], alpha=0.6)
ax.bar(years, shangri_la_festivals[:, 2], bottom=np.sum(shangri_la_festivals[:, :2], axis=1), label='Sports (Shangri-La)', color=colors[2], alpha=0.6)
ax.bar(years, shangri_la_festivals[:, 3], bottom=np.sum(shangri_la_festivals[:, :3], axis=1), label='Culinary (Shangri-La)', color=colors[3], alpha=0.6)

ax.bar(years, avalon_festivals[:, 0], label='Music (Avalon)', color=colors[0], edgecolor='black', linewidth=0.5)
ax.bar(years, avalon_festivals[:, 1], bottom=avalon_festivals[:, 0], label='Arts (Avalon)', color=colors[1], edgecolor='black', linewidth=0.5)
ax.bar(years, avalon_festivals[:, 2], bottom=np.sum(avalon_festivals[:, :2], axis=1), label='Sports (Avalon)', color=colors[2], edgecolor='black', linewidth=0.5)
ax.bar(years, avalon_festivals[:, 3], bottom=np.sum(avalon_festivals[:, :3], axis=1), label='Culinary (Avalon)', color=colors[3], edgecolor='black', linewidth=0.5)

# Labels, title, and legend
ax.set_ylabel('Number of Festivals')
ax.set_xlabel('Year')
ax.set_title('Annual Cultural Festival Distribution\nin Ancient Cities (1010-1019)', fontsize=14)
ax.set_xticks(years)
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), title='Festival Type and City', fontsize=9, ncol=2)
ax.set_ylim(0, 50)

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()