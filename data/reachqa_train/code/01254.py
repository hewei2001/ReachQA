import matplotlib.pyplot as plt
import numpy as np

# Years and corresponding communication tool usage (in millions)
years = np.array([1900, 1920, 1940, 1960, 1980, 2000, 2020])
postal_mail = np.array([80, 120, 150, 160, 140, 100, 40])
telephone = np.array([0, 5, 50, 200, 600, 1200, 1500])
radio = np.array([0, 0, 30, 150, 300, 250, 50])
television = np.array([0, 0, 0, 20, 500, 1100, 1200])
internet = np.array([0, 0, 0, 0, 50, 800, 4000])

# Related but distinct data: World population (in billions)
world_population = np.array([1.65, 1.86, 2.3, 3.0, 4.4, 6.1, 7.8])

# Create the figure and primary axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the communication tools data on the primary axis
ax1.plot(years, postal_mail, label='Postal Mail', marker='o', color='#ff7f0e', linewidth=2)
ax1.plot(years, telephone, label='Telephone', marker='^', color='#1f77b4', linewidth=2, linestyle='--')
ax1.plot(years, radio, label='Radio', marker='s', color='#2ca02c', linewidth=2, linestyle='-.')
ax1.plot(years, television, label='Television', marker='D', color='#d62728', linewidth=2, linestyle=':')
ax1.plot(years, internet, label='Internet', marker='x', color='#9467bd', linewidth=2)

# Annotate data points for communication tools
for i, year in enumerate(years):
    ax1.annotate(f'{postal_mail[i]}', (year, postal_mail[i]), textcoords="offset points", xytext=(0,10), ha='center', color='#ff7f0e')
    ax1.annotate(f'{telephone[i]}', (year, telephone[i]), textcoords="offset points", xytext=(0,10), ha='center', color='#1f77b4')
    ax1.annotate(f'{radio[i]}', (year, radio[i]), textcoords="offset points", xytext=(0,10), ha='center', color='#2ca02c')
    ax1.annotate(f'{television[i]}', (year, television[i]), textcoords="offset points", xytext=(0,10), ha='center', color='#d62728')
    ax1.annotate(f'{internet[i]}', (year, internet[i]), textcoords="offset points", xytext=(0,10), ha='center', color='#9467bd')

# Set labels for the primary axis
ax1.set_title('The Evolution of Communication Tools\nFrom 1900 to 2020 & World Population Growth', fontsize=18, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Users (in millions)', fontsize=14)
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Create a secondary axis for world population
ax2 = ax1.twinx()
ax2.bar(years, world_population, width=5, alpha=0.3, color='gray', label='World Population (in billions)')
ax2.set_ylabel('World Population (in billions)', fontsize=14, color='gray')

# Combine legends from both axes
lines, labels = ax1.get_legend_handles_labels()
bars, bar_labels = ax2.get_legend_handles_labels()
ax1.legend(lines + bars, labels + bar_labels, title='Communication Tool & Population', loc='upper left', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()