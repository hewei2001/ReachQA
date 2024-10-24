import matplotlib.pyplot as plt
import numpy as np

# Communication methods and their respective usage percentages
methods = ['Face-to-Face', 'Phone Calls', 'Text Messaging', 'Email', 'Video Calls', 'Social Media', 'VR Meetings']
percentages_2023 = [25, 15, 20, 15, 10, 10, 5]
percentages_2033 = [15, 10, 15, 10, 20, 20, 10]

# Hypothetical average daily time (in minutes) spent on each communication method across the years
avg_daily_time = {
    'Face-to-Face': [60, 50],
    'Phone Calls': [30, 20],
    'Text Messaging': [40, 30],
    'Email': [45, 35],
    'Video Calls': [20, 35],
    'Social Media': [30, 45],
    'VR Meetings': [10, 25]
}

# Colors for each communication method segment
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#C0C0C0', '#FF69B4']

# Create a figure with a 1x3 grid to compare both years and add a bar chart
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(21, 7))

# Plot the 2023 donut chart
ax1.pie(percentages_2023, labels=methods, autopct='%1.1f%%', startangle=140, 
        colors=colors, wedgeprops=dict(width=0.3), pctdistance=0.85,
        explode=[0.1 if method == 'Face-to-Face' else 0 for method in methods])
ax1.set_title('Communication Methods\nin 2023', fontsize=14)

# Plot the 2033 donut chart
ax2.pie(percentages_2033, labels=methods, autopct='%1.1f%%', startangle=140, 
        colors=colors, wedgeprops=dict(width=0.3), pctdistance=0.85,
        explode=[0.1 if method == 'VR Meetings' else 0 for method in methods])
ax2.set_title('Communication Methods\nin 2033', fontsize=14)

# Plot a bar chart showing average daily time spent on each communication method
avg_times_2023 = [avg_daily_time[method][0] for method in methods]
avg_times_2033 = [avg_daily_time[method][1] for method in methods]
x = np.arange(len(methods))
width = 0.35

# Plot bars for 2023 and 2033
bars1 = ax3.bar(x - width/2, avg_times_2023, width, label='2023', color=colors)
bars2 = ax3.bar(x + width/2, avg_times_2033, width, label='2033', color=colors)

# Labeling the bar chart
ax3.set_ylabel('Average Daily Time (minutes)', fontsize=12)
ax3.set_title('Average Daily Time\nSpent per Method', fontsize=14)
ax3.set_xticks(x)
ax3.set_xticklabels(methods, rotation=45, ha='right')
ax3.legend()

# Adding text for each bar
def add_bar_labels(bars, ax):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom')

add_bar_labels(bars1, ax3)
add_bar_labels(bars2, ax3)

# Adjust layout to ensure no overlapping and all elements are visible
plt.tight_layout()

# Add a super title to the entire figure
plt.suptitle("Evolution and Impact of Communication Methods:\nA Decade's Perspective", fontsize=16, fontweight='bold', y=1.02)

# Add a shared legend outside of the plots
fig.legend(bars1, methods, title="Methods", loc="center left", bbox_to_anchor=(1.02, 0.5))

# Display the chart
plt.show()