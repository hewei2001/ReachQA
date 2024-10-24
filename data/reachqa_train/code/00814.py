import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2013, 2024)

# Internet traffic data in petabytes (hypothetical)
streaming_services = np.array([30, 40, 55, 65, 75, 90, 100, 115, 130, 150, 170])
online_gaming = np.array([15, 20, 22, 24, 28, 35, 45, 50, 58, 70, 85])
social_media = np.array([10, 12, 15, 20, 25, 35, 50, 60, 80, 100, 130])

# Create a figure and axis for plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Plot lines for each digital media type with different styles
ax.plot(years, streaming_services, marker='o', linestyle='-', color='#1f77b4', linewidth=2, label='Streaming Services')
ax.plot(years, online_gaming, marker='s', linestyle='--', color='#ff7f0e', linewidth=2, label='Online Gaming')
ax.plot(years, social_media, marker='^', linestyle='-.', color='#2ca02c', linewidth=2, label='Social Media')

# Customize the title and axis labels
ax.set_title('Internet Traffic Trends in FantasyLand\nA Decade of Digital Change', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Monthly Internet Traffic (Petabytes)', fontsize=12)

# Customize x-ticks
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add a legend
ax.legend(title='Digital Media Types', loc='upper left', fontsize=10)

# Annotate key milestones
annotations = {
    2015: ("Mobile Streaming Surges", streaming_services[2]),
    2020: ("Gaming Goes Global", online_gaming[7]),
    2023: ("Social Media Dominance", social_media[10]),
}

for year, (text, y_value) in annotations.items():
    ax.annotate(text, xy=(year, y_value), xytext=(year, y_value + 15),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5), fontsize=10, color='black', ha='center')

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()