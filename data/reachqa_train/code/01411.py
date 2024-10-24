import matplotlib.pyplot as plt
import numpy as np

# Define the months in a year
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Accuracy percentages for each club (in percentage)
cosmic_explorers_accuracy = np.array([75, 78, 82, 85, 88, 90, 89, 86, 84, 83, 81, 79])
stargazers_guild_accuracy = np.array([70, 73, 75, 79, 82, 84, 83, 81, 80, 78, 76, 74])
skywatchers_league_accuracy = np.array([68, 70, 73, 76, 79, 81, 80, 78, 77, 75, 73, 71])

# Error margins for each club (in percentage)
cosmic_explorers_error = np.array([3, 2.5, 3, 2.5, 2, 2, 2.5, 3, 3.5, 4, 4.5, 5])
stargazers_guild_error = np.array([4, 3.5, 3, 3, 2.5, 2.5, 3, 3.5, 4, 4.5, 5, 5.5])
skywatchers_league_error = np.array([5, 4.5, 4, 3.5, 3, 3, 3.5, 4, 4.5, 5, 5.5, 6])

# Create the plots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 8))

# First subplot: Line chart with error bars
axes[0].errorbar(months, cosmic_explorers_accuracy, yerr=cosmic_explorers_error, fmt='-o', label='Cosmic Explorers',
             color='mediumorchid', linestyle='-', linewidth=2, capsize=5, elinewidth=1.5, alpha=0.8)
axes[0].errorbar(months, stargazers_guild_accuracy, yerr=stargazers_guild_error, fmt='-s', label='Stargazers Guild',
             color='mediumseagreen', linestyle='-', linewidth=2, capsize=5, elinewidth=1.5, alpha=0.8)
axes[0].errorbar(months, skywatchers_league_accuracy, yerr=skywatchers_league_error, fmt='-^', label='Skywatchers League',
             color='steelblue', linestyle='-', linewidth=2, capsize=5, elinewidth=1.5, alpha=0.8)

axes[0].set_title("Astronomy Enthusiasts' Star Observation\nAccuracy Over Time", fontsize=14, pad=20)
axes[0].set_xlabel("Month", fontsize=12)
axes[0].set_ylabel("Accuracy (%)", fontsize=12)
axes[0].legend(loc='lower left', title='Astronomy Clubs')
axes[0].grid(True, linestyle='--', alpha=0.6)

# Annotate notable data points
axes[0].annotate('Peak Accuracy', xy=('Jun', 90), xytext=('Aug', 92),
                 arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')
axes[0].annotate('Consistent Observations', xy=('Nov', 76), xytext=('Sep', 78),
                 arrowprops=dict(facecolor='green', arrowstyle='->'), fontsize=10, color='green')

# Second subplot: Bar chart showing cumulative annual accuracy
total_accuracy = np.array([cosmic_explorers_accuracy.sum(), 
                           stargazers_guild_accuracy.sum(), 
                           skywatchers_league_accuracy.sum()])
clubs = ['Cosmic Explorers', 'Stargazers Guild', 'Skywatchers League']
colors = ['mediumorchid', 'mediumseagreen', 'steelblue']

axes[1].bar(clubs, total_accuracy, color=colors, alpha=0.7)
axes[1].set_title("Total Annual Accuracy", fontsize=14)
axes[1].set_ylabel("Total Accuracy (%)", fontsize=12)

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()