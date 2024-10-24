import matplotlib.pyplot as plt
import numpy as np

# Define languages and greeting phrases
languages = ['English', 'Spanish', 'French', 'German', 'Japanese']
greetings = ['Hello', 'Good Morning', 'Good Evening', 'Good Night', 'Thank You']

# Data representing the frequency of each greeting phrase used per day
usage_frequency = np.array([
    [50, 25, 15, 10, 30],  # English
    [40, 30, 20, 15, 35],  # Spanish
    [45, 20, 25, 10, 30],  # French
    [35, 25, 20, 15, 25],  # German
    [30, 20, 20, 15, 40]   # Japanese
])

# Set up the figure
fig, ax = plt.subplots(figsize=(10, 7))

# Define colors for each greeting
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot the bar chart
x = np.arange(len(languages))
bar_width = 0.15
offset = np.arange(-(len(greetings)-1)/2, (len(greetings)+1)/2) * bar_width

for idx, (greeting, color) in enumerate(zip(greetings, colors)):
    ax.bar(x + offset[idx], usage_frequency[:, idx], bar_width, label=greeting, color=color)

# Add labels and title
ax.set_ylabel('Frequency of Usage\n(times per day)', fontsize=11)
ax.set_title('Greetings Across Cultures:\nFrequency of Phrase Usage in Daily Conversations', 
             fontsize=13, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(languages, fontsize=10)
ax.legend(title='Greeting Phrase', loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0.)

# Annotate each bar with the frequency values
for i in range(len(languages)):
    for j in range(len(greetings)):
        ax.text(i + offset[j], usage_frequency[i, j] + 0.5, f'{usage_frequency[i, j]}', 
                ha='center', va='bottom', fontsize=9, color='black')

# Rotate x-axis labels if necessary for better readability
plt.xticks(rotation=0, ha='center')

# Enhance readability with grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()