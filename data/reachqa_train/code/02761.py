import matplotlib.pyplot as plt
import numpy as np

# Years for x-axis
years = np.arange(1010, 1020)

# Data: number of festivals in different cities
atlantis_festivals = np.array([[5, 4, 3, 2], [6, 5, 4, 3], [7, 5, 5, 3], [8, 6, 5, 4], [6, 5, 4, 3], 
                               [5, 5, 3, 4], [6, 6, 4, 3], [7, 5, 5, 4], [8, 5, 6, 5], [9, 6, 6, 4]])
el_dorado_festivals = np.array([[6, 3, 4, 1], [7, 4, 5, 2], [8, 4, 6, 2], [9, 5, 6, 3], [7, 4, 5, 2],
                                [6, 4, 4, 3], [7, 5, 5, 2], [8, 4, 6, 3], [9, 4, 7, 4], [10, 5, 7, 3]])
shangri_la_festivals = np.array([[4, 5, 2, 3], [5, 6, 3, 4], [6, 6, 4, 4], [7, 7, 4, 5], [5, 6, 3, 4],
                                 [4, 6, 2, 5], [5, 7, 3, 4], [6, 6, 4, 5], [7, 6, 5, 6], [8, 7, 5, 5]])
avalon_festivals = np.array([[7, 6, 5, 4], [8, 7, 6, 5], [9, 7, 7, 5], [10, 8, 7, 6], [8, 7, 6, 5],
                             [7, 7, 5, 6], [8, 8, 6, 5], [9, 7, 7, 6], [10, 7, 8, 7], [11, 8, 8, 6]])

# Construct average attendance data
average_attendance = np.mean(atlantis_festivals + el_dorado_festivals + shangri_la_festivals + avalon_festivals, axis=1)

# Colors for the different festival types
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#40E0D0']

# Creating the plot
fig, ax1 = plt.subplots(figsize=(14, 9))

# Plot stacked bars for each city and festival type
for i, (city_festivals, city_name, alpha, hatch, linestyle) in enumerate(
    zip([atlantis_festivals, el_dorado_festivals, shangri_la_festivals, avalon_festivals], 
        ['Atlantis', 'El Dorado', 'Shangri-La', 'Avalon'],
        [1, 0.8, 0.6, 0.5], 
        [None, '//', None, None], 
        ['-', '-', '-', '-'])):
    
    base = np.zeros(len(years))
    for j in range(city_festivals.shape[1]):
        ax1.bar(years, city_festivals[:, j], bottom=base, 
                color=colors[j], alpha=alpha, hatch=hatch, edgecolor='black' if city_name == 'Avalon' else None, linewidth=0.5)
        base += city_festivals[:, j]

# Create a secondary Y-axis for the line plot
ax2 = ax1.twinx()
ax2.plot(years, average_attendance, label='Avg Attendance', color='black', linestyle='--', marker='o')
ax2.set_ylabel('Average Attendance')
ax2.set_ylim(0, 40)

# Adjust layout
ax1.set_title('Annual Cultural Festival Distribution\nin Ancient Cities (1010-1019) with Avg Attendance', fontsize=14)
ax1.set_ylabel('Number of Festivals')
ax1.set_xlabel('Year')
ax1.set_xticks(years)
ax1.set_ylim(0, 50)

# Legends
bar_handles, _ = ax1.get_legend_handles_labels()
line_handles, _ = ax2.get_legend_handles_labels()
ax1.legend(handles=bar_handles[:4], loc='upper left', bbox_to_anchor=(1.02, 1), title='Festival Type (City)', fontsize=9, ncol=2)
ax2.legend(handles=line_handles, loc='upper right', bbox_to_anchor=(1.02, 0.5), fontsize=9)

plt.tight_layout()
plt.show()