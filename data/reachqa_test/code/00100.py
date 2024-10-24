import matplotlib.pyplot as plt
import numpy as np

# Years from 2013 to 2023
years = np.arange(2013, 2024)

# Adoption rate data (in percentage)
education = np.array([2, 3, 5, 8, 12, 18, 25, 33, 45, 58, 70])
healthcare = np.array([1, 2, 4, 7, 10, 15, 22, 30, 42, 55, 68])
entertainment = np.array([5, 8, 12, 18, 25, 33, 44, 57, 70, 80, 85])
military = np.array([3, 5, 8, 13, 20, 28, 35, 45, 55, 68, 75])
retail = np.array([1, 2, 3, 5, 8, 14, 22, 32, 45, 60, 73])

# Investment data (in billions)
investment = np.array([0.5, 0.8, 1.2, 1.8, 2.5, 3.3, 4.0, 5.0, 6.5, 8.0, 9.5])

# Create a figure and a main axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the stacked area chart
ax1.stackplot(years, education, healthcare, entertainment, military, retail,
              labels=['Education', 'Healthcare', 'Entertainment', 'Military', 'Retail'],
              colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#D5AAFF'], alpha=0.8)

# Title and labels
ax1.set_title("VR Adoption in Various Fields and Investment Trends (2013-2023)", fontsize=16, pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("VR Adoption Rate (%)", fontsize=12)
ax1.tick_params(axis='x', rotation=45)

# Customize legend and grid for adoption rates
ax1.legend(loc='upper left', title='Field of Application')
ax1.grid(axis='y', linestyle='--', alpha=0.5)

# Add the overlay line plot on a secondary y-axis
ax2 = ax1.twinx()
ax2.plot(years, investment, color='darkblue', linestyle='--', marker='o', label='VR Investment')
ax2.set_ylabel("VR Investment (Billion $)", fontsize=12)
ax2.legend(loc='upper right', title='Investment Trends')

# Add annotations for significant milestones in investment
for i, year in enumerate(years):
    if investment[i] in [3.3, 5.0, 9.5]:  # Example investment milestones
        ax2.annotate(f'{year}: ${investment[i]}B',
                     (year, investment[i]),
                     textcoords="offset points", xytext=(-10, -20), ha='center',
                     arrowprops=dict(arrowstyle='->', lw=0.5, color='darkblue'))

# Automatically adjust layout to avoid overlaps
fig.tight_layout()

# Show the plot
plt.show()