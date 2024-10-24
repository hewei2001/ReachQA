import matplotlib.pyplot as plt
import numpy as np

# Define the years and market share data for each operating system
years = np.arange(2013, 2024)
android_share = [60, 65, 70, 72, 75, 78, 80, 81, 83, 85, 86]
ios_share = [30, 28, 25, 25, 20, 18, 18, 17, 15, 13, 12]
windows_share = [7, 5, 3, 2, 2, 2, 1, 1, 1, 1, 1]
other_share = [3, 2, 2, 1, 3, 2, 1, 1, 1, 1, 1]

# Stack data for plotting
market_share_data = np.array([android_share, ios_share, windows_share, other_share])

# Colors for each operating system
colors = ['#3DDC84', '#A2AAAD', '#0078D6', '#FF6347']

# Create a percentage bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the stacked bar chart with percentages
ax.stackplot(years, market_share_data, labels=["Android", "iOS", "Windows Phone", "Others"], colors=colors, alpha=0.8)

# Add percentage labels on each segment
for i in range(len(years)):
    android_top = android_share[i]
    ios_top = android_top + ios_share[i]
    windows_top = ios_top + windows_share[i]
    other_top = windows_top + other_share[i]
    
    ax.text(years[i], android_top - 3, f'{android_share[i]}%', color='white', ha='center', va='center', fontweight='bold')
    ax.text(years[i], ios_top - 1.5, f'{ios_share[i]}%', color='white', ha='center', va='center', fontweight='bold')
    ax.text(years[i], windows_top - 0.5, f'{windows_share[i]}%', color='black', ha='center', va='center', fontweight='bold')
    ax.text(years[i], other_top - 0.3, f'{other_share[i]}%', color='black', ha='center', va='center', fontweight='bold')

# Title and labels
ax.set_title("Global Smartphone OS Market Share:\nA Decade of Change (2013-2023)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Market Share (%)", fontsize=12)

# Configure x and y axes
ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 100)
ax.set_xticks(years)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{int(y)}%'))

# Adding a legend
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Operating Systems', fontsize=10, title_fontsize='12', frameon=True)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Grid settings
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Automatic layout adjustment
plt.tight_layout()

# Display the plot
plt.show()