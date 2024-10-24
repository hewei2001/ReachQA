import numpy as np
import matplotlib.pyplot as plt

# Define the time periods
decades = ['1990s', '2000s', '2010s', '2020s']

# Define attendance in thousands for each event type over the decades
music_festivals = [100, 150, 200, 250]
art_exhibitions = [80, 120, 160, 200]
theatre_performances = [90, 110, 130, 140]
film_screenings = [70, 100, 180, 220]
literary_fairs = [60, 85, 90, 95]

# Stack data together
attendance_data = np.array([music_festivals, art_exhibitions, theatre_performances, film_screenings, literary_fairs])

# Define labels for each event type
event_labels = ['Music Festivals', 'Art Exhibitions', 'Theatre Performances', 'Film Screenings', 'Literary Fairs']

# Calculate total attendance per decade
total_attendance = np.sum(attendance_data, axis=0)

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Stacked area chart
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
axes[0].stackplot(decades, attendance_data, labels=event_labels, colors=colors, alpha=0.8)
axes[0].set_title('Cultural Engagement Trends Over Decades\n(1990s - 2020s)', fontsize=14, fontweight='bold', pad=20)
axes[0].set_xlabel('Decades', fontsize=12)
axes[0].set_ylabel('Attendance (Thousands)', fontsize=12)
axes[0].legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Event Types')
axes[0].grid(True, linestyle='--', alpha=0.7, which='both')
axes[0].set_xticks(np.arange(len(decades)))
axes[0].set_xticklabels(decades)

# Bar chart for total attendance per decade
bar_colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072']
axes[1].bar(decades, total_attendance, color=bar_colors, alpha=0.7, edgecolor='black')
axes[1].set_title('Total Cultural Attendance Per Decade', fontsize=14, fontweight='bold', pad=20)
axes[1].set_xlabel('Decades', fontsize=12)
axes[1].set_ylabel('Total Attendance (Thousands)', fontsize=12)
for i, v in enumerate(total_attendance):
    axes[1].text(i, v + 10, str(v), ha='center', va='bottom', fontweight='bold')
axes[1].grid(True, linestyle='--', alpha=0.7, which='both')
axes[1].set_xticks(np.arange(len(decades)))
axes[1].set_xticklabels(decades)

# Tight layout adjustment
plt.tight_layout()

# Show the plots
plt.show()