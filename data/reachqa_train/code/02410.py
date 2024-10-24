import numpy as np
import matplotlib.pyplot as plt

# Data representing 30 days of meditation practice
days = np.arange(1, 31)
meditation_duration = [5, 10, 7, 12, 15, 20, 18, 25, 30, 28,
                       35, 40, 38, 45, 48, 50, 55, 60, 58, 65,
                       68, 70, 75, 78, 80, 82, 85, 87, 90, 95]

# Mood score corresponding to each day
mood_score = [5, 5, 6, 6, 7, 6, 7, 7, 7, 8,
              8, 8, 9, 8, 9, 9, 9, 10, 9, 9,
              10, 10, 9, 9, 10, 10, 10, 9, 10, 10]

# Set up the plotting area
plt.figure(figsize=(14, 8))

# Plot the meditation duration
plt.plot(days, meditation_duration, label='Meditation Duration (min)', color='b', linewidth=2, marker='o')

# Plot the mood score
plt.plot(days, mood_score, label='Mood Score', color='g', linewidth=2, linestyle='--', marker='s')

# Annotate significant events every 5 days
for i in range(0, len(days), 5):
    plt.annotate(f'Day {days[i]}\nMeditation: {meditation_duration[i]} min\nMood: {mood_score[i]}',
                 xy=(days[i], mood_score[i]), xytext=(days[i], mood_score[i]+1.5),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=9, ha='center')

# Add titles and labels
plt.title("The Journey to Serenity:\nAnalyzing Daily Meditation's Impact on Mood Over a Month", fontsize=16, pad=20)
plt.xlabel("Days", fontsize=13)
plt.ylabel("Meditation Duration (minutes) / Mood Score", fontsize=13)

# Display the legend
plt.legend(loc='upper left', fontsize=12, edgecolor='black')

# Show grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Customize ticks
plt.xticks(days)
plt.yticks(np.arange(0, 101, 10))

# Adjust the layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()