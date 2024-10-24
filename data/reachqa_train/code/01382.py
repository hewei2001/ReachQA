import matplotlib.pyplot as plt
import numpy as np

# Define the weeks within months for more granularity
weeks = np.array(['Jan W1', 'Jan W2', 'Jan W3', 'Jan W4',
                  'Feb W1', 'Feb W2', 'Feb W3', 'Feb W4',
                  'Mar W1', 'Mar W2', 'Mar W3', 'Mar W4',
                  'Apr W1', 'Apr W2', 'Apr W3', 'Apr W4',
                  'May W1', 'May W2', 'May W3', 'May W4',
                  'Jun W1', 'Jun W2', 'Jun W3', 'Jun W4',
                  'Jul W1', 'Jul W2', 'Jul W3', 'Jul W4',
                  'Aug W1', 'Aug W2', 'Aug W3', 'Aug W4',
                  'Sep W1', 'Sep W2', 'Sep W3', 'Sep W4',
                  'Oct W1', 'Oct W2', 'Oct W3', 'Oct W4',
                  'Nov W1', 'Nov W2', 'Nov W3', 'Nov W4',
                  'Dec W1', 'Dec W2', 'Dec W3', 'Dec W4'])

# Create commuter data with a slight trend and pattern
base_values = np.linspace(20, 60, num=len(weeks))

# Simulate different cities with varied patterns around the base trend
copenhagen_commuters = base_values + np.sin(np.linspace(0, 2 * np.pi, len(weeks))) * 5 + 5
amsterdam_commuters = base_values + np.cos(np.linspace(0, 2 * np.pi, len(weeks))) * 4 + 7
portland_commuters = base_values + np.sin(np.linspace(0, 2 * np.pi, len(weeks))) * 3 - 2
barcelona_commuters = base_values + np.cos(np.linspace(0, 2 * np.pi, len(weeks))) * 3 + 4
new_city_commuters = base_values + np.sin(np.linspace(0, 2 * np.pi, len(weeks) * 2))[:len(weeks)] * 2

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 10))

# Plot the data for each city
ax.plot(weeks, copenhagen_commuters, label='Copenhagen', color='skyblue', linewidth=2)
ax.plot(weeks, amsterdam_commuters, label='Amsterdam', color='lightgreen', linewidth=2)
ax.plot(weeks, portland_commuters, label='Portland', color='salmon', linewidth=2)
ax.plot(weeks, barcelona_commuters, label='Barcelona', color='orchid', linewidth=2)
ax.plot(weeks, new_city_commuters, label='New City', color='gold', linewidth=2)

# Adding title and labels
ax.set_title('Urban Buzz: Comprehensive Bicycle Commute Trends Across Cities in 2023', fontsize=16, pad=20)
ax.set_xlabel('Time (Weeks)', fontsize=14)
ax.set_ylabel('Bicycle Commuters (in thousands)', fontsize=14)

# Adding grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Adding legend with title
ax.legend(title='Cities', fontsize=12, loc='upper left', title_fontsize='13', frameon=False)

# Rotate x-tick labels for better readability
plt.xticks(rotation=45)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()