import matplotlib.pyplot as plt
import numpy as np

# Define years from 2008 to 2028
years = np.arange(2008, 2029)

# Growth percentage data for various art categories
digital_paintings = np.array([2, 3, 5, 8, 12, 18, 25, 32, 40, 50, 62, 75, 90, 98, 100, 102, 104, 105, 106, 107, 108])
sculptures = np.array([1, 2, 3, 5, 7, 12, 18, 25, 33, 42, 52, 63, 75, 80, 82, 85, 87, 88, 89, 90, 91])
photography = np.array([3, 5, 7, 11, 16, 22, 30, 39, 49, 60, 72, 85, 100, 101, 102, 104, 105, 107, 108, 109, 110])
traditional_paintings = np.array([2, 3, 4, 6, 9, 13, 20, 29, 38, 48, 58, 70, 82, 87, 90, 91, 92, 93, 94, 95, 96])
installations = np.array([1, 2, 4, 7, 10, 15, 22, 30, 39, 50, 62, 75, 88, 90, 92, 93, 94, 95, 96, 97, 98])

# Set up the plot
plt.figure(figsize=(16, 10))

# Plotting each art category
plt.plot(years, digital_paintings, marker='o', label='Digital Paintings', color='#1f77b4', linestyle='-', linewidth=2)
plt.plot(years, sculptures, marker='s', label='Sculptures', color='#ff7f0e', linestyle='--', linewidth=2)
plt.plot(years, photography, marker='^', label='Photography', color='#2ca02c', linestyle='-.', linewidth=2)
plt.plot(years, traditional_paintings, marker='d', label='Traditional Paintings', color='#d62728', linestyle=':', linewidth=2)
plt.plot(years, installations, marker='x', label='Installations', color='#9467bd', linestyle='-', linewidth=2)

# Calculate the average growth for a secondary y-axis
average_growth = (digital_paintings + sculptures + photography + traditional_paintings + installations) / 5

# Add a secondary y-axis for average growth
ax2 = plt.gca().twinx()
ax2.plot(years, average_growth, color='grey', linestyle='--', linewidth=1.5, label='Average Growth')
ax2.set_ylabel('Average Growth (%)', fontsize=12)
ax2.grid(False)

# Annotating significant data points for Digital Paintings
for year, dp in zip(years, digital_paintings):
    if year in [2008, 2018, 2028]:
        plt.annotate(f'{dp}%', xy=(year, dp), xytext=(-30, 10), textcoords='offset points',
                     fontsize=10, arrowprops=dict(arrowstyle='->', color='#1f77b4', lw=1))

# Customize the plot
plt.title("The Growth of Online Art Sales\nAcross Diverse Categories (2008-2028)", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Growth in Sales (%)", fontsize=14)

# Add grid lines and set ticks
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 111, 10))
ax2.set_yticks(np.arange(0, 111, 10))

# Add legends
plt.legend(title="Art Categories", title_fontsize=12, fontsize=10, loc='upper left')
ax2.legend(loc='upper right', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()