import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2020)

# Simulated number of stellar events observed by each observatory per year
hubble_events = np.array([102, 110, 115, 123, 131, 140, 145, 150, 160, 165])
chandra_events = np.array([95, 100, 103, 110, 117, 124, 130, 135, 140, 148])
spitzer_events = np.array([88, 92, 98, 105, 112, 120, 125, 130, 137, 145])

# Error associated with each observatory's observations
hubble_errors = np.array([5, 5, 6, 7, 7, 8, 8, 9, 9, 10])
chandra_errors = np.array([6, 6, 6, 7, 7, 8, 8, 8, 9, 10])
spitzer_errors = np.array([7, 7, 7, 8, 8, 9, 9, 9, 10, 11])

# Simulated budget data for each observatory in millions of dollars
hubble_budget = np.array([200, 210, 220, 230, 240, 250, 260, 270, 280, 290])
chandra_budget = np.array([180, 185, 190, 200, 210, 220, 230, 235, 245, 255])
spitzer_budget = np.array([160, 165, 170, 180, 190, 200, 210, 215, 225, 235])

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot each line with error bars for stellar events
ax1.errorbar(years, hubble_events, yerr=hubble_errors, label='Hubble Observatory',
            fmt='-o', capsize=5, color='blue', alpha=0.7)
ax1.errorbar(years, chandra_events, yerr=chandra_errors, label='Chandra Observatory',
            fmt='-s', capsize=5, color='green', alpha=0.7)
ax1.errorbar(years, spitzer_events, yerr=spitzer_errors, label='Spitzer Observatory',
            fmt='-^', capsize=5, color='orange', alpha=0.7)

# Customizing the primary y-axis
ax1.set_title('Annual Stellar Observations and Budgets of Leading Space Observatories\n(2010-2019)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of Observable Stellar Events', fontsize=14)
ax1.legend(title='Space Observatory', fontsize=10, loc='upper left')
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Setting x-ticks and labels
ax1.set_xticks(years)
ax1.set_xticklabels([str(year) for year in years], fontsize=12)
ax1.set_ylim(80, 180)

# Creating a secondary y-axis for budget data
ax2 = ax1.twinx()
ax2.plot(years, hubble_budget, label='Hubble Budget', linestyle='--', color='blue', alpha=0.6)
ax2.plot(years, chandra_budget, label='Chandra Budget', linestyle='--', color='green', alpha=0.6)
ax2.plot(years, spitzer_budget, label='Spitzer Budget', linestyle='--', color='orange', alpha=0.6)

# Customizing the secondary y-axis
ax2.set_ylabel('Annual Budget (in millions USD)', fontsize=14)
ax2.set_ylim(150, 300)
ax2.legend(title='Annual Budget', fontsize=10, loc='upper right')

# Annotate a significant event or trend
max_observed_year = years[np.argmax(hubble_events)]
ax1.annotate('Highest Observations',
             xy=(max_observed_year, np.max(hubble_events)),
             xytext=(max_observed_year-2, 170),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, fontweight='bold', color='darkred')

# Improve layout
plt.tight_layout()
plt.show()