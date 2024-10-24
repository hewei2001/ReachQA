import matplotlib.pyplot as plt
import numpy as np

# Define years and corresponding data
years = np.arange(2010, 2021)
internet_users = [1950, 2135, 2300, 2475, 2730, 3000, 3290, 3615, 4005, 4370, 4700]  # in millions
connection_speeds = [2.0, 2.5, 3.1, 4.0, 5.5, 7.0, 8.9, 10.4, 12.5, 15.2, 18.0]  # in Mbps
time_spent_online = [50, 53, 55, 59, 63, 68, 72, 75, 78, 81, 85]  # hours per week

# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(14, 9))

# Plot the number of internet users
color_users = 'tab:blue'
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Internet Users (Millions)', color=color_users, fontsize=12)
ax1.plot(years, internet_users, marker='o', linestyle='-', color=color_users, linewidth=2.5, label='Internet Users')
ax1.tick_params(axis='y', labelcolor=color_users)

# Plot the average connection speed
ax2 = ax1.twinx()
color_speeds = 'tab:red'
ax2.set_ylabel('Average Connection Speed (Mbps)', color=color_speeds, fontsize=12)
ax2.plot(years, connection_speeds, marker='s', linestyle='--', color=color_speeds, linewidth=2.5, label='Connection Speed')
ax2.tick_params(axis='y', labelcolor=color_speeds)

# Introduce a third plot with a bar chart
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
color_time = 'tab:green'
ax3.set_ylabel('Time Spent Online (Hours/Week)', color=color_time, fontsize=12)
ax3.bar(years, time_spent_online, color=color_time, alpha=0.3, width=0.6, label='Time Spent Online')
ax3.tick_params(axis='y', labelcolor=color_time)

# Add titles and grid
plt.title('A Decade of Digital Expansion:\nInternet Usage, Speed, and Online Time (2010-2020)', fontsize=16, pad=20)
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add legends
fig.legend(loc='upper center', ncol=3, fontsize=10, title='Metrics', bbox_to_anchor=(0.5, 1.05))

# Highlight specific points
important_years = [2015, 2020]
for year in important_years:
    idx = np.where(years == year)[0][0]
    ax1.annotate(f'{internet_users[idx]}M', (years[idx], internet_users[idx]), textcoords="offset points", xytext=(-10,-15), ha='center', fontsize=9, color=color_users)
    ax2.annotate(f'{connection_speeds[idx]} Mbps', (years[idx], connection_speeds[idx]), textcoords="offset points", xytext=(10,10), ha='center', fontsize=9, color=color_speeds)
    ax3.annotate(f'{time_spent_online[idx]} hrs', (years[idx], time_spent_online[idx]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=9, color=color_time)

# Adjust layout to avoid overlapping
fig.tight_layout()

# Show the plot
plt.show()