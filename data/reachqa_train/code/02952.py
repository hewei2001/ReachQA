import numpy as np
import matplotlib.pyplot as plt

# Define the months
months = np.array([
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
])

# Create AQI data for three futuristic cities
ecoville_aqi = np.array([50, 45, 40, 35, 30, 32, 31, 30, 28, 30, 35, 40])
greenopolis_aqi = np.array([60, 55, 50, 45, 40, 42, 38, 35, 37, 40, 45, 50])
sustaincity_aqi = np.array([55, 50, 45, 40, 35, 37, 36, 34, 32, 34, 38, 42])

# Create the line chart
fig, ax = plt.subplots(figsize=(14, 7))

# Plot each city's AQI data
ax.plot(months, ecoville_aqi, marker='o', linestyle='-', color='teal', linewidth=2.0, label='EcoVille')
ax.plot(months, greenopolis_aqi, marker='s', linestyle='--', color='forestgreen', linewidth=2.0, label='Greenopolis')
ax.plot(months, sustaincity_aqi, marker='^', linestyle='-.', color='royalblue', linewidth=2.0, label='SustainCity')

# Titles and labels
ax.set_title("Air Quality Index Trends\nSustainable Cities in 2123", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Months", fontsize=14)
ax.set_ylabel("Average Monthly AQI", fontsize=14)

# Add a legend
ax.legend(loc='upper right', title='Cities', fontsize=11, title_fontsize=13, frameon=False)

# Customize grid
ax.grid(True, linestyle='--', alpha=0.6)

# Customize x-axis ticks
plt.xticks(rotation=45, fontsize=11)

# Highlight significant improvement months with annotations
improvement_months = [4, 8]  # Index for May and September
annotations = ["EcoVille leads improvement", "All cities see reductions"]

for i, month in enumerate(improvement_months):
    ax.annotate(
        annotations[i], 
        (months[month], ecoville_aqi[month]),
        xytext=(-30, 20), 
        textcoords='offset points',
        arrowprops=dict(facecolor='black', arrowstyle='->'),
        fontsize=10,
        color='darkred'
    )

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the chart
plt.show()