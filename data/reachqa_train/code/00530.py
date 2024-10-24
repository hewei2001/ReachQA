import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2013 to 2023
years = np.arange(2013, 2024)

# Growth percentage data for different art categories
digital_paintings = np.array([5, 8, 12, 18, 25, 32, 40, 50, 62, 75, 90])
sculptures = np.array([3, 5, 7, 12, 18, 25, 33, 42, 52, 63, 75])
photography = np.array([7, 11, 16, 22, 30, 39, 49, 60, 72, 85, 100])

# Set up the plot
plt.figure(figsize=(14, 9))

# Plotting the line chart for each art category with distinct markers
plt.plot(years, digital_paintings, marker='o', label='Digital Paintings', color='#1f77b4', linestyle='-')
plt.plot(years, sculptures, marker='s', label='Sculptures', color='#ff7f0e', linestyle='--')
plt.plot(years, photography, marker='^', label='Photography', color='#2ca02c', linestyle='-.')

# Annotating significant data points
for year, dp, sc, ph in zip(years, digital_paintings, sculptures, photography):
    if year in [2013, 2018, 2023]:
        plt.annotate(f'{dp}%', xy=(year, dp), xytext=(-25, 10),
                     textcoords='offset points', fontsize=10,
                     arrowprops=dict(arrowstyle='->', color='#1f77b4', lw=1))
        plt.annotate(f'{sc}%', xy=(year, sc), xytext=(-25, -20),
                     textcoords='offset points', fontsize=10,
                     arrowprops=dict(arrowstyle='->', color='#ff7f0e', lw=1))
        plt.annotate(f'{ph}%', xy=(year, ph), xytext=(10, 0),
                     textcoords='offset points', fontsize=10,
                     arrowprops=dict(arrowstyle='->', color='#2ca02c', lw=1))

# Customize the plot
plt.title("The Growth of Online Art Sales\nOver a Decade (2013-2023)", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Growth in Sales (%)", fontsize=14)

# Add grid lines and set ticks
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(years)
plt.yticks(np.arange(0, 101, 10))

# Add legend
plt.legend(title="Art Categories", title_fontsize=12, fontsize=10, loc='upper left')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()