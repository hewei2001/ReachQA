import matplotlib.pyplot as plt
import numpy as np

# Define emotion categories
categories = ['Joy', 'Sadness', 'Anger', 'Fear', 'Love']

# Data for each culture
data_western = [8, 5, 4, 3, 7]
data_eastern = [6, 4, 5, 5, 9]
data_african = [7, 6, 6, 4, 8]
data_latin_american = [9, 3, 5, 4, 10]

# Extend data to close the radar chart
data_western += data_western[:1]
data_eastern += data_eastern[:1]
data_african += data_african[:1]
data_latin_american += data_latin_american[:1]

# Compute angles for radar chart
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

# Data for bar chart: average emotion intensity for each culture
avg_emotion_intensity = [
    np.mean(data_western[:-1]),  # Remove duplicated closing point
    np.mean(data_eastern[:-1]),
    np.mean(data_african[:-1]),
    np.mean(data_latin_american[:-1])
]
cultures = ['Western', 'Eastern', 'African', 'Latin American']

# Initialize subplot grid
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), subplot_kw={'polar': [True, False]})
fig.suptitle('Cultural Differences in Emotion Intensity', size=16, weight='bold', color='darkslategray')

# Radar chart
ax1.set_title('Emotion Distribution in Cultures', size=14, color='indigo')
ax1.set_theta_offset(np.pi / 2)
ax1.set_theta_direction(-1)

ax1.plot(angles, data_western, color='blue', linewidth=2, label='Western')
ax1.fill(angles, data_western, color='blue', alpha=0.1)
ax1.plot(angles, data_eastern, color='green', linewidth=2, label='Eastern')
ax1.fill(angles, data_eastern, color='green', alpha=0.1)
ax1.plot(angles, data_african, color='red', linewidth=2, label='African')
ax1.fill(angles, data_african, color='red', alpha=0.1)
ax1.plot(angles, data_latin_american, color='orange', linewidth=2, label='Latin American')
ax1.fill(angles, data_latin_american, color='orange', alpha=0.1)

ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(categories, color='grey', size=11)
ax1.set_yticks([1, 3, 5, 7, 9])
ax1.set_yticklabels(['1', '3', '5', '7', '9'], color='grey', size=8)
ax1.set_ylim(0, 10)

ax1.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10, title="Cultures")

# Bar chart
ax2.set_title('Average Emotion Intensity', size=14, color='indigo')
ax2.bar(cultures, avg_emotion_intensity, color=['blue', 'green', 'red', 'orange'], alpha=0.7)
ax2.set_ylabel('Average Intensity', size=12)
ax2.set_ylim(0, 10)

# Rotate x-tick labels for clarity
ax2.set_xticklabels(cultures, rotation=45, ha='right', fontsize=10, color='grey')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()