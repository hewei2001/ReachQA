import matplotlib.pyplot as plt

# Data preparation
missions = [
    'Voyager 1',
    'Voyager 2',
    'Solar and Heliospheric Observatory (SOHO)',
    'Cassini-Huygens',
    'Pioneer 10'
]
durations = [
    15664,
    14485,
    8421,
    4935,
    31226
]

# Normalize durations for visual distinction (Optional, depending on the scale of the data)
# durations = [duration / 1000 for duration in durations]

# Plot configuration
plt.figure(figsize=(12, 7))
plt.gca().set_facecolor('#EAEAF2')  # Set background color to a light gray

# Define a color scheme
color_scheme = plt.cm.Paired(range(len(missions)))

# Plot horizontal bars with error bars for simulated data uncertainty
bars = plt.barh(missions, durations, color=color_scheme, xerr=100)

# Ticks and labels
plt.xlabel('Mission Duration (Days)')
plt.ylabel('Space Mission')

# Grid for readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Title with smaller font size
plt.title('Top 5\nSpace Exploration Missions\nby Mission Duration', fontsize=14, fontweight='bold')

# Ensure the y-axis labels are aligned with the center of the bars
plt.yticks(range(len(missions)), missions)

# Annotate bars with actual duration values
for bar, duration in zip(bars, durations):
    # Horizontal offset varies to avoid overlapping with bars, considering duration values
    x_offset = 350 if duration > 10000 else 100
    plt.text(bar.get_width() + x_offset, bar.get_y() + bar.get_height()/2,
             f'{duration} days', ha='left', va='center')

# Set x-axis to logarithmic scale for better data representation if durations vary greatly
plt.xscale('log')

# Prevent clipping of title and labels, adjust layout automatically
plt.tight_layout()

# Show the plot
plt.show()