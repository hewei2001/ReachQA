import matplotlib.pyplot as plt
import numpy as np

# Data for the original line chart with error bars
years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
ev_percentages = np.array([0.5, 0.8, 1.5, 2.3, 3.2, 5.0, 7.8, 12.0, 18.5, 25.0])
errors = np.array([0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0])

# Hypothetical data for the new bar chart
# Cumulative number of EVs registered in thousands
ev_cumulative = np.array([10, 20, 35, 55, 80, 120, 180, 280, 450, 700])

# Create the figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Line chart with error bars
axs[0].errorbar(
    years, ev_percentages, yerr=errors, fmt='-o', ecolor='lightgray',
    capsize=5, elinewidth=2, markeredgewidth=2, color='teal', label='EV Adoption Rate'
)
axs[0].set_title("Riding the Electric Wave:\nA Decade of EV Adoption in Metropolis", fontsize=13, fontweight='bold')
axs[0].set_xlabel("Year", fontsize=11)
axs[0].set_ylabel("Percentage of Vehicle Registrations", fontsize=11)
axs[0].legend(loc='upper left', fontsize='medium')
axs[0].grid(True, linestyle='--', alpha=0.5)
axs[0].set_xticks(years)
axs[0].set_xticklabels(years, rotation=45)
axs[0].set_yticks(np.arange(0, 30, 5))

# Bar chart for cumulative EV registrations
axs[1].bar(years, ev_cumulative, color='coral', edgecolor='black', label='Cumulative EVs Registered (Thousands)')
axs[1].set_title("A Surge in Numbers:\nCumulative EV Registrations", fontsize=13, fontweight='bold')
axs[1].set_xlabel("Year", fontsize=11)
axs[1].set_ylabel("Cumulative EV Registrations (in Thousands)", fontsize=11)
axs[1].legend(loc='upper left', fontsize='medium')
axs[1].grid(True, linestyle='--', alpha=0.5)
axs[1].set_xticks(years)
axs[1].set_xticklabels(years, rotation=45)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()