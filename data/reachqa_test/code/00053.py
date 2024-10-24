import matplotlib.pyplot as plt
import numpy as np

# Define the months of the year
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Air Quality Index (AQI) data for each city over 12 months
ecoville_aqi = np.array([85, 80, 78, 72, 70, 68, 65, 63, 62, 60, 58, 56])
greenburg_aqi = np.array([90, 88, 86, 83, 80, 79, 77, 75, 74, 72, 70, 68])
clearhaven_aqi = np.array([95, 92, 90, 87, 85, 83, 80, 78, 77, 75, 73, 71])
freshfield_aqi = np.array([88, 86, 84, 81, 79, 78, 76, 74, 73, 71, 70, 68])

# Calculate average AQI for each city
avg_aqi = {
    'EcoVille': np.mean(ecoville_aqi),
    'Greenburg': np.mean(greenburg_aqi),
    'Clearhaven': np.mean(clearhaven_aqi),
    'Freshfield': np.mean(freshfield_aqi)
}

# Create a figure with 1 row and 2 columns of subplots
fig, axes = plt.subplots(1, 2, figsize=(15, 7))

# Plot each city's AQI trend
axes[0].plot(months, ecoville_aqi, marker='o', linestyle='-', linewidth=2, 
             label='EcoVille', color='#1f77b4')
axes[0].plot(months, greenburg_aqi, marker='s', linestyle='-', linewidth=2, 
             label='Greenburg', color='#ff7f0e')
axes[0].plot(months, clearhaven_aqi, marker='^', linestyle='-', linewidth=2, 
             label='Clearhaven', color='#2ca02c')
axes[0].plot(months, freshfield_aqi, marker='d', linestyle='-', linewidth=2, 
             label='Freshfield', color='#d62728')

# Set titles and labels for line plot
axes[0].set_title("Monthly AQI Trends by City\nEnvironmental Research Group", fontsize=14, weight='bold')
axes[0].set_xlabel("Months", fontsize=12)
axes[0].set_ylabel("Air Quality Index (AQI)", fontsize=12)
axes[0].set_xticks(months)
axes[0].set_xticklabels(months, rotation=45)
axes[0].set_yticks(np.arange(55, 101, 5))
axes[0].grid(True, linestyle='--', alpha=0.6)
axes[0].legend(title='Cities', loc='upper right', fontsize=10)

# Plot average AQI using a bar chart
cities = list(avg_aqi.keys())
avg_values = list(avg_aqi.values())
bar_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
axes[1].bar(cities, avg_values, color=bar_colors)

# Set titles and labels for bar chart
axes[1].set_title("Average AQI for Each City", fontsize=14, weight='bold')
axes[1].set_xlabel("Cities", fontsize=12)
axes[1].set_ylabel("Average AQI", fontsize=12)
axes[1].set_ylim(55, 100)
axes[1].grid(axis='y', linestyle='--', alpha=0.6)

# Adjust layout to ensure no overlapping text
plt.tight_layout()

# Display the plot
plt.show()