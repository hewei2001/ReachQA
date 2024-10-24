import matplotlib.pyplot as plt
import numpy as np

# Define age groups and listening hours (hours/month)
age_groups = ['18-24', '25-34', '35-44', '45-54', '55+']
listening_hours_2015 = [np.array([20, 22, 23, 19, 25, 27, 21, 22, 20, 24, 26, 23]),
                        np.array([15, 14, 16, 18, 17, 15, 16, 18, 17, 16, 18, 15]),
                        np.array([12, 10, 11, 13, 12, 14, 11, 10, 12, 13, 11, 10]),
                        np.array([10, 9, 8, 11, 9, 10, 10, 9, 8, 9, 8, 9]),
                        np.array([5, 6, 7, 6, 5, 6, 7, 5, 6, 7, 5, 6])]

listening_hours_2020 = [np.array([25, 28, 30, 27, 29, 31, 26, 28, 27, 30, 29, 31]),
                        np.array([20, 19, 21, 23, 22, 24, 19, 21, 20, 23, 21, 22]),
                        np.array([18, 17, 16, 18, 19, 17, 15, 18, 17, 16, 18, 16]),
                        np.array([12, 13, 15, 14, 12, 13, 14, 12, 14, 13, 15, 14]),
                        np.array([8, 7, 6, 9, 8, 7, 9, 6, 7, 9, 6, 7])]

listening_hours_2025 = [np.array([28, 31, 33, 32, 30, 32, 29, 33, 31, 34, 32, 31]),
                        np.array([23, 24, 25, 24, 23, 25, 24, 23, 24, 25, 26, 23]),
                        np.array([20, 18, 21, 19, 20, 21, 19, 20, 21, 22, 20, 21]),
                        np.array([15, 14, 16, 15, 14, 16, 15, 14, 16, 17, 15, 16]),
                        np.array([10, 11, 12, 11, 10, 11, 10, 12, 11, 10, 12, 11])]

# Create a dictionary to store data
listening_data = {
    '2015': listening_hours_2015,
    '2020': listening_hours_2020,
    '2025': listening_hours_2025
}

# Calculate average listening hours for the new subplot
avg_listening_hours = {
    year: [np.mean(hours) for hours in data] for year, data in listening_data.items()
}

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [3, 2]})

# Plot the horizontal box chart on ax1
colors = ['#FFC300', '#FF5733', '#C70039']
for i, (year, data) in enumerate(listening_data.items()):
    ax1.boxplot(data, positions=np.arange(len(age_groups)) * 3 + i, vert=False, widths=0.6, patch_artist=True,
                notch=True, boxprops=dict(facecolor=colors[i], alpha=0.7),
                whiskerprops=dict(color=colors[i]), capprops=dict(color=colors[i]),
                medianprops=dict(color='black'))

ax1.set_yticks(np.arange(len(age_groups)) * 3 + 1)
ax1.set_yticklabels(age_groups)
ax1.set_xlabel('Monthly Listening Hours')
ax1.set_title('Trends in Music Streaming Hours Across Age Groups\nfrom 2015 to 2025', fontsize=14, fontweight='bold', pad=20)

# Add a legend for ax1
for i, year in enumerate(listening_data):
    ax1.plot([], [], color=colors[i], label=year, linewidth=7)
ax1.legend(loc='lower right', fontsize=10, title='Year')

ax1.xaxis.grid(True, linestyle='--', alpha=0.7)

# Plot the line chart of average listening hours over the years on ax2
for i, (age_group, color) in enumerate(zip(age_groups, colors)):
    ax2.plot(listening_data.keys(), [avg_listening_hours[year][i] for year in listening_data], marker='o', label=age_group, color=color)

ax2.set_xlabel('Year')
ax2.set_ylabel('Average Monthly Listening Hours')
ax2.set_title('Average Listening Hours by Age Group (2015-2025)', fontsize=12, fontweight='bold', pad=20)
ax2.legend(loc='upper left', fontsize=9, title='Age Group')
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()