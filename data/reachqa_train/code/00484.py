import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Data for each genre (percentage of total readership)
fantasy = np.array([15, 17, 19, 21, 20, 19, 18, 18, 19, 20, 22])
sci_fi = np.array([12, 11, 13, 14, 15, 16, 18, 20, 21, 22, 23])
mystery = np.array([25, 24, 23, 21, 20, 19, 18, 18, 17, 16, 15])
romance = np.array([20, 21, 22, 23, 23, 24, 25, 26, 25, 24, 23])
non_fiction = np.array([28, 27, 23, 21, 22, 22, 21, 18, 18, 18, 17])

# Synthesized data for total readership (in millions)
total_readership = np.array([100, 105, 110, 115, 118, 122, 125, 127, 130, 134, 138])

# Create figure and axis with secondary y-axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting the stacked area chart
ax1.stackplot(years, fantasy, sci_fi, mystery, romance, non_fiction,
             labels=['Fantasy', 'Sci-Fi', 'Mystery', 'Romance', 'Non-Fiction'],
             colors=['#c9d1d3', '#aad6a1', '#f6b393', '#f7e1a0', '#b0a8d0'], alpha=0.85)

# Configure primary axis
ax1.set_title('Literature Evolution: Reading Preferences and Total Readership\n(2010-2020)', fontsize=18, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Percentage of Total Readership', fontsize=14)
ax1.grid(True, linestyle='--', linewidth=0.7, alpha=0.6)

# Adding legend for stacked area
ax1.legend(loc='upper left', title='Genres', fontsize=12, frameon=False)

# Rotating x-axis labels to prevent overlap
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)

# Annotations for key trends
ax1.annotate('Rise in Sci-Fi', xy=(2018, 60), xytext=(2016, 70),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)
ax1.annotate('Steady Interest in Romance', xy=(2020, 82), xytext=(2015, 90),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Create secondary y-axis for total readership
ax2 = ax1.twinx()
ax2.plot(years, total_readership, color='red', marker='o', linestyle='-', linewidth=2, label='Total Readership')
ax2.set_ylabel('Total Readership (Millions)', fontsize=14, color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Adding legend for the overlay plot
ax2.legend(loc='upper right', fontsize=12, frameon=False)

# Automatically adjust the layout
plt.tight_layout()

# Show plot
plt.show()