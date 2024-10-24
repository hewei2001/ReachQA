import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Average internet speeds in Mbps for each region over the decade
north_america_speeds = [5, 10, 12, 15, 18, 20, 25, 30, 32, 35, 40]
europe_speeds = [4, 8, 10, 13, 15, 18, 22, 25, 28, 31, 35]
asia_speeds = [3, 6, 9, 11, 13, 17, 21, 24, 27, 30, 34]
africa_speeds = [1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 18]
south_america_speeds = [2, 4, 5, 7, 9, 11, 14, 17, 20, 23, 27]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Define colors for each line
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot each region's internet speeds
ax.plot(years, north_america_speeds, marker='o', color=colors[0], label='North America', linewidth=2)
ax.plot(years, europe_speeds, marker='s', color=colors[1], label='Europe', linewidth=2)
ax.plot(years, asia_speeds, marker='^', color=colors[2], label='Asia', linewidth=2)
ax.plot(years, africa_speeds, marker='D', color=colors[3], label='Africa', linewidth=2)
ax.plot(years, south_america_speeds, marker='v', color=colors[4], label='South America', linewidth=2)

# Annotate specific milestones
for i in range(0, len(years), 2):  # Annotate every two years for clarity
    ax.annotate(f'{north_america_speeds[i]}', (years[i], north_america_speeds[i]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=9)
    ax.annotate(f'{europe_speeds[i]}', (years[i], europe_speeds[i]), textcoords="offset points", xytext=(-10,-15), ha='center', fontsize=9)
    ax.annotate(f'{asia_speeds[i]}', (years[i], asia_speeds[i]), textcoords="offset points", xytext=(10,10), ha='center', fontsize=9)
    ax.annotate(f'{africa_speeds[i]}', (years[i], africa_speeds[i]), textcoords="offset points", xytext=(10,-15), ha='center', fontsize=9)
    ax.annotate(f'{south_america_speeds[i]}', (years[i], south_america_speeds[i]), textcoords="offset points", xytext=(-10,-10), ha='center', fontsize=9)

# Set title and labels
ax.set_title('The Decade of Connectivity:\nEvolution of Internet Speeds Across Regions', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Internet Speed (Mbps)', fontsize=12)

# Add grid for better readability
ax.grid(visible=True, linestyle='--', alpha=0.5)

# Show legend
ax.legend(loc='upper left', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()