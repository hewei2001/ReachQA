import numpy as np
import matplotlib.pyplot as plt

# Define the years for the x-axis
years = np.arange(2015, 2026)

# Define subscription data for each platform and region (in millions)
streamflix_na = np.array([10, 12, 15, 20, 25, 30, 35, 38, 40, 43, 45])
streamflix_eu = np.array([8, 9, 11, 14, 18, 22, 25, 27, 29, 31, 33])
streamflix_ap = np.array([5, 6, 8, 11, 15, 20, 25, 30, 35, 38, 40])

primestream_na = np.array([5, 7, 9, 12, 14, 16, 18, 20, 22, 23, 25])
primestream_eu = np.array([3, 4, 5, 7, 9, 11, 13, 15, 17, 18, 20])
primestream_ap = np.array([2, 3, 4, 5, 7, 10, 14, 18, 20, 22, 24])

viewnow_na = np.array([2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13])
viewnow_eu = np.array([1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12])
viewnow_ap = np.array([0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Initialize the plot
fig, ax = plt.subplots(1, 3, figsize=(18, 8), sharey=True)

# Colors for each platform
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plot each region's data
regions = [
    ("North America", streamflix_na, primestream_na, viewnow_na),
    ("Europe", streamflix_eu, primestream_eu, viewnow_eu),
    ("Asia-Pacific", streamflix_ap, primestream_ap, viewnow_ap)
]

for idx, (region, streamflix, primestream, viewnow) in enumerate(regions):
    ax[idx].bar(years, streamflix, color=colors[0], label='StreamFlix')
    ax[idx].bar(years, primestream, bottom=streamflix, color=colors[1], label='PrimeStream')
    ax[idx].bar(years, viewnow, bottom=streamflix + primestream, color=colors[2], label='ViewNow')
    ax[idx].set_title(region, fontsize=14)

# Common labels and overall title
for axis in ax:
    axis.set_xlabel('Year', fontsize=12)
    axis.set_xticks(years)
    axis.tick_params(axis='x', rotation=45)
ax[0].set_ylabel('Subscriptions (millions)', fontsize=12)

fig.suptitle('Global Streaming Platform Subscriptions by Region\n2015 to 2025', fontsize=16, fontweight='bold', y=1.05)

# Add a legend for all regions
fig.legend(loc='upper center', ncol=3, fontsize=12)

# Adjust layout to ensure no overlap
plt.tight_layout()

# Display the plot
plt.show()