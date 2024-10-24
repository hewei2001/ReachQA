import matplotlib.pyplot as plt
import numpy as np

# Define decades and number of satellite launches for each agency
decades = np.array([1970, 1980, 1990, 2000, 2010, 2020])
nasa_launches = np.array([5, 15, 25, 35, 50, 70])
esa_launches = np.array([3, 10, 20, 30, 45, 65])
cnsa_launches = np.array([1, 5, 15, 25, 40, 60])

# Set up the plot
plt.figure(figsize=(12, 8))

# Plot the data with custom styles
plt.plot(decades, nasa_launches, marker='o', linestyle='-', color='royalblue', linewidth=2, label='NASA')
plt.plot(decades, esa_launches, marker='s', linestyle='--', color='green', linewidth=2, label='ESA')
plt.plot(decades, cnsa_launches, marker='^', linestyle='-.', color='red', linewidth=2, label='CNSA')

# Annotate key points with background color for visibility
plt.annotate('Rise of GPS', xy=(1990, 25), xytext=(1985, 40),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10,
             bbox=dict(boxstyle='round,pad=0.3', edgecolor='none', facecolor='white', alpha=0.8))
plt.annotate('Commercial Launch Boom', xy=(2010, 45), xytext=(2005, 60),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10,
             bbox=dict(boxstyle='round,pad=0.3', edgecolor='none', facecolor='white', alpha=0.8))

# Label each point
for (x, y) in zip(decades, nasa_launches):
    plt.text(x, y + 2, str(y), ha='center', va='bottom', fontsize=9, color='royalblue')
for (x, y) in zip(decades, esa_launches):
    plt.text(x, y + 2, str(y), ha='center', va='bottom', fontsize=9, color='green')
for (x, y) in zip(decades, cnsa_launches):
    plt.text(x, y + 2, str(y), ha='center', va='bottom', fontsize=9, color='red')

# Customize the plot
plt.title("Space Exploration: The Rise of Satellite Launches Over Time\n(1970-2020)",
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Decade", fontsize=12)
plt.ylabel("Number of Satellite Launches", fontsize=12)
plt.xticks(decades)
plt.yticks(np.arange(0, 81, 10))
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Space Agencies', loc='upper left', fontsize=10, frameon=True)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()