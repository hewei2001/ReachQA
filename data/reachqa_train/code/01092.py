import matplotlib.pyplot as plt
import numpy as np

# Years of analysis
years = np.array([2000, 2005, 2010, 2015, 2020, 2025, 2030])

# Popularity data for each futuristic concept
ai_popularity = np.array([10, 20, 40, 70, 85, 95, 100])
vr_popularity = np.array([5, 15, 35, 50, 60, 75, 90])
qc_popularity = np.array([2, 10, 25, 45, 70, 80, 85])
nano_popularity = np.array([15, 25, 40, 55, 65, 70, 80])

# Calculate average annual growth rate for each concept
def compute_average_growth(data):
    return np.diff(data) / (years[1:] - years[:-1])

ai_growth = compute_average_growth(ai_popularity)
vr_growth = compute_average_growth(vr_popularity)
qc_growth = compute_average_growth(qc_popularity)
nano_growth = compute_average_growth(nano_popularity)

growth_labels = ['2000-2005', '2005-2010', '2010-2015', '2015-2020', '2020-2025', '2025-2030']

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(16, 8))

# Original line chart
ax1.plot(years, ai_popularity, label='AI', marker='o', linestyle='-', color='b', linewidth=2)
ax1.plot(years, vr_popularity, label='VR', marker='s', linestyle='--', color='r', linewidth=2)
ax1.plot(years, qc_popularity, label='QC', marker='^', linestyle='-.', color='g', linewidth=2)
ax1.plot(years, nano_popularity, label='Nano', marker='d', linestyle=':', color='purple', linewidth=2)

ax1.set_title("Techno-Cultural Evolution:\nPopularity of Futuristic Concepts (2000-2030)", fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Popularity Score', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend(loc='upper left', fontsize=10, title='Concepts')

ax1.annotate('AI Breakthrough', xy=(2020, 85), xytext=(2012, 90), arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=10, color='blue')
ax1.annotate('VR Mainstream', xy=(2025, 75), xytext=(2015, 80), arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=10, color='red')
ax1.annotate('QC Milestone', xy=(2030, 85), xytext=(2020, 88), arrowprops=dict(facecolor='green', arrowstyle='->'), fontsize=10, color='green')
ax1.annotate('Nano in Health', xy=(2030, 80), xytext=(2020, 75), arrowprops=dict(facecolor='purple', arrowstyle='->'), fontsize=10, color='purple')

# New bar chart subplot
bar_width = 0.2
index = np.arange(len(growth_labels))

ax2.bar(index, ai_growth, bar_width, label='AI', color='b')
ax2.bar(index + bar_width, vr_growth, bar_width, label='VR', color='r')
ax2.bar(index + 2*bar_width, qc_growth, bar_width, label='QC', color='g')
ax2.bar(index + 3*bar_width, nano_growth, bar_width, label='Nano', color='purple')

ax2.set_title("Average Annual Growth Rate\nof Futuristic Concepts", fontsize=14, fontweight='bold')
ax2.set_xlabel('Period', fontsize=12)
ax2.set_ylabel('Average Growth Rate', fontsize=12)
ax2.set_xticks(index + 1.5*bar_width)
ax2.set_xticklabels(growth_labels, fontsize=10)
ax2.legend(loc='upper left', fontsize=10, title='Concepts')
ax2.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout
plt.tight_layout()
plt.show()