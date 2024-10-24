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

# Create the plot
plt.figure(figsize=(12, 8))

# Plot each line with error bars
plt.errorbar(months, cosmic_explorers_accuracy, yerr=cosmic_explorers_error, fmt='-o', label='Cosmic Explorers',
             color='mediumorchid', linestyle='-', linewidth=2, capsize=5, elinewidth=1.5, alpha=0.8)
plt.errorbar(months, stargazers_guild_accuracy, yerr=stargazers_guild_error, fmt='-s', label='Stargazers Guild',
             color='mediumseagreen', linestyle='-', linewidth=2, capsize=5, elinewidth=1.5, alpha=0.8)
plt.errorbar(months, skywatchers_league_accuracy, yerr=skywatchers_league_error, fmt='-^', label='Skywatchers League',
             color='steelblue', linestyle='-', linewidth=2, capsize=5, elinewidth=1.5, alpha=0.8)

# Add titles and labels
plt.title("Astronomy Enthusiasts' Star Observation\nAccuracy Over Time", fontsize=16, pad=20)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Accuracy (%)", fontsize=12)

# Displaying a legend
plt.legend(loc='lower left', title='Astronomy Clubs')

# Grid and aesthetic improvements
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

# Annotate notable data points
plt.annotate('Peak Accuracy', xy=('Jun', 90), xytext=('Aug', 92),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')
plt.annotate('Consistent Observations', xy=('Nov', 76), xytext=('Sep', 78),
             arrowprops=dict(facecolor='green', arrowstyle='->'), fontsize=10, color='green')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()