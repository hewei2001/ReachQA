import matplotlib.pyplot as plt
import numpy as np

# Data for the area chart
years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
activities_data = {
    'Arts & Crafts': [2.5, 2.6, 2.8, 3.0, 3.2, 3.6, 3.8, 4.1, 4.4, 4.8],
    'Music & Theater': [1.2, 1.3, 1.4, 1.6, 1.8, 2.1, 2.3, 2.6, 2.9, 3.3],
    'Scientific Learning': [1.0, 1.1, 1.2, 1.4, 1.6, 1.9, 2.1, 2.4, 2.6, 2.8],
    'Digital Creation': [0.8, 0.9, 1.1, 1.3, 1.6, 2.0, 2.3, 2.7, 3.1, 3.6]
}

# Prepare data for plotting
data = np.array([activities_data[activity] for activity in activities_data])
labels = list(activities_data.keys())
colors = ['#F9A602', '#36454F', '#4682B4', '#FFDAB9']

# Plot stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each area with outlines and percentage increase
for idx, (label, ydata) in enumerate(zip(labels, data)):
    ydata_cumulative = np.cumsum(data[:idx+1], axis=0)  # Cumulative sum for stacking
    if idx == 0:
        ax.fill_between(years, ydata, color=colors[idx], alpha=0.7, label=label)
    else:
        ax.fill_between(years, ydata_cumulative[-1], ydata_cumulative[-2], color=colors[idx], alpha=0.7, label=label)

    # Show percentage increase since 2013
    percent_change = (ydata[-1] - ydata[0]) / ydata[0] * 100
    ax.text(years[-1], ydata_cumulative[-1, -1], f'+{percent_change:.1f}%', ha='left', va='center', color=colors[idx], rotation=90)

# Set title, labels, and grid
plt.title('Creative and Learning Activities (2013-2022)', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Hours per Week', fontsize=12)
plt.xticks(years, rotation=45, ha='right')
plt.grid(True, which='major', axis='y', linestyle=':', linewidth=0.75, alpha=0.5)

# Add legend outside the plot
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), frameon=True)

# Display chart
plt.tight_layout()
plt.show()