import matplotlib.pyplot as plt
import numpy as np

# Define years for the data
years = np.arange(2010, 2021)

# Manually crafted data for EV registrations (in thousands)
north_america_ev = np.array([20, 25, 30, 50, 75, 110, 160, 230, 320, 450, 600])
europe_ev = np.array([15, 18, 25, 35, 50, 80, 130, 200, 300, 430, 580])
asia_ev = np.array([10, 15, 20, 35, 60, 100, 150, 250, 400, 600, 850])

# Calculate growth rates (year-over-year growth percentages)
north_america_growth = np.diff(north_america_ev) / north_america_ev[:-1] * 100
europe_growth = np.diff(europe_ev) / europe_ev[:-1] * 100
asia_growth = np.diff(asia_ev) / asia_ev[:-1] * 100

# Initialize the figure and the two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# Plotting the line chart for EV registrations
ax1.plot(years, north_america_ev, marker='o', linestyle='-', color='blue', linewidth=2, label='North America')
ax1.plot(years, europe_ev, marker='s', linestyle='-', color='green', linewidth=2, label='Europe')
ax1.plot(years, asia_ev, marker='^', linestyle='-', color='red', linewidth=2, label='Asia')
ax1.set_title('Electric Vehicle Registrations by Region\n(2010-2020)', fontsize=14, weight='bold', pad=15)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Registrations (in thousands)', fontsize=12)
ax1.legend(loc='upper left', fontsize=10, title='Regions', title_fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.annotate('Rapid growth in Asia', xy=(2019, 600), xytext=(2015, 700),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=10, color='darkred')
ax1.annotate('Initial surge in North America', xy=(2013, 50), xytext=(2011, 150),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=10, color='darkblue')
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Plotting the bar chart for growth rates
ax2.bar(years[1:], north_america_growth, color='skyblue', width=0.2, label='North America')
ax2.bar(years[1:] + 0.25, europe_growth, color='lightgreen', width=0.2, label='Europe')
ax2.bar(years[1:] + 0.5, asia_growth, color='salmon', width=0.2, label='Asia')
ax2.set_title('Year-over-Year Growth Rate in EV Registrations', fontsize=14, weight='bold', pad=15)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.legend(loc='upper right', fontsize=10, title='Regions', title_fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.set_xticks(years[1:] + 0.25)
ax2.set_xticklabels(years[1:], rotation=45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()