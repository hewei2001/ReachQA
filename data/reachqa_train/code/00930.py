import matplotlib.pyplot as plt
import numpy as np

# Define weeks of the year for a more detailed dataset
weeks = np.array(range(1, 53))

# Construct complex coffee consumption data for different brewing methods
espresso_consumption = 220 + 50 * np.sin(np.linspace(0, 4 * np.pi, 52)) + np.linspace(0, 10, 52)
french_press_consumption = 200 + 45 * np.sin(np.linspace(0, 4 * np.pi, 52) + np.pi / 8) + np.linspace(5, 15, 52)
americano_consumption = 180 + 40 * np.sin(np.linspace(0, 4 * np.pi, 52) - np.pi / 6) + np.linspace(10, 20, 52)

# Error margins representing the uncertainty in consumption data
espresso_errors = 5 + 3 * np.abs(np.sin(np.linspace(0, 4 * np.pi, 52)))
french_press_errors = 6 + 4 * np.abs(np.cos(np.linspace(0, 4 * np.pi, 52)))
americano_errors = 7 + 2 * np.abs(np.sin(np.linspace(0, 4 * np.pi, 52) + np.pi / 3))

# Create subplots to display all categories in separate plots
fig, ax = plt.subplots(3, 1, figsize=(14, 18), sharex=True)

# Plot data with error bars for each coffee type
ax[0].errorbar(weeks, espresso_consumption, yerr=espresso_errors, label='Espresso',
               capsize=3, marker='o', linestyle='-', color='#2b8cbe', alpha=0.8)
ax[0].set_title("Weekly Coffee Consumption Trends (2022)\nEspresso", fontsize=14, fontweight='bold')
ax[0].set_ylabel("Consumption (Cups)", fontsize=12)
ax[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

ax[1].errorbar(weeks, french_press_consumption, yerr=french_press_errors, label='French Press',
               capsize=3, marker='s', linestyle='--', color='#fdae61', alpha=0.8)
ax[1].set_title("Weekly Coffee Consumption Trends (2022)\nFrench Press", fontsize=14, fontweight='bold')
ax[1].set_ylabel("Consumption (Cups)", fontsize=12)
ax[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

ax[2].errorbar(weeks, americano_consumption, yerr=americano_errors, label='Americano',
               capsize=3, marker='^', linestyle='-.', color='#d73027', alpha=0.8)
ax[2].set_title("Weekly Coffee Consumption Trends (2022)\nAmericano", fontsize=14, fontweight='bold')
ax[2].set_ylabel("Consumption (Cups)", fontsize=12)
ax[2].set_xlabel("Week", fontsize=12)
ax[2].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Ensure labels and titles are shown correctly
for a in ax:
    a.legend(title="Brewing Method", loc='upper left')
    a.set_xticks(weeks[::4])
    a.set_xticklabels(['Week {}'.format(i) for i in weeks[::4]], rotation=45)

# Automatically adjust layout for better readability
plt.tight_layout()

# Display the completed chart
plt.show()