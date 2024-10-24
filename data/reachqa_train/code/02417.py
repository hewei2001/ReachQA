import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Data for 30 days of meditation practice
days = np.arange(1, 31)
meditation_duration = [5, 10, 7, 12, 15, 20, 18, 25, 30, 28,
                       35, 40, 38, 45, 48, 50, 55, 60, 58, 65,
                       68, 70, 75, 78, 80, 82, 85, 87, 90, 95]
mood_score = [5, 5, 6, 6, 7, 6, 7, 7, 7, 8,
              8, 8, 9, 8, 9, 9, 9, 10, 9, 9,
              10, 10, 9, 9, 10, 10, 10, 9, 10, 10]

# Setting up the plot with dual y-axes
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot for meditation duration
color = 'tab:blue'
ax1.set_xlabel('Days', fontsize=13)
ax1.set_ylabel('Meditation Duration (min)', color=color, fontsize=13)
ax1.plot(days, meditation_duration, color=color, marker='o', linewidth=2, label='Meditation Duration')
ax1.tick_params(axis='y', labelcolor=color)
ax1.fill_between(days, meditation_duration, mood_score, where=(np.array(meditation_duration) >= np.array(mood_score)),
                 interpolate=True, color='blue', alpha=0.1)

# Second y-axis for mood score
ax2 = ax1.twinx()
color = 'tab:green'
ax2.set_ylabel('Mood Score', color=color, fontsize=13)
ax2.plot(days, mood_score, color=color, linestyle='--', marker='s', linewidth=2, label='Mood Score')
ax2.tick_params(axis='y', labelcolor=color)

# Add linear regression lines
slope, intercept, _, _, _ = linregress(days, meditation_duration)
ax1.plot(days, slope*days + intercept, color='darkblue', linestyle=':', linewidth=1, label='Trend: Meditation')

slope, intercept, _, _, _ = linregress(days, mood_score)
ax2.plot(days, slope*days + intercept, color='darkgreen', linestyle=':', linewidth=1, label='Trend: Mood')

# Annotate significant events every 5 days
for i in range(0, len(days), 5):
    ax1.annotate(f'Day {days[i]}\nMeditation: {meditation_duration[i]} min\nMood: {mood_score[i]}',
                 xy=(days[i], meditation_duration[i]), xytext=(days[i] + 0.5, meditation_duration[i] + 5),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=9, ha='center', color='navy')

# Add titles and grid
plt.title("The Journey to Serenity:\nAnalyzing Daily Meditation's Impact on Mood Over a Month", fontsize=16, pad=20)
plt.grid(True, linestyle='--', alpha=0.5)

# Legends for both y-axes
fig.legend(loc='upper left', bbox_to_anchor=(0.15, 0.85), fontsize=12, edgecolor='black')

# Adjust layout for readability
fig.tight_layout()

# Show plot
plt.show()