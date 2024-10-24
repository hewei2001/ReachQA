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

# Hypothetical sentiment scores for each language
sentiment_scores = np.array([0.8, 0.7, 0.75, 0.65, 0.9])

# Set up the figure
fig, ax1 = plt.subplots(figsize=(12, 8))

# Define colors for each greeting
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot the bar chart
x = np.arange(len(languages))
bar_width = 0.15
offset = np.arange(-(len(greetings)-1)/2, (len(greetings)+1)/2) * bar_width

for idx, (greeting, color) in enumerate(zip(greetings, colors)):
    ax1.bar(x + offset[idx], usage_frequency[:, idx], bar_width, label=greeting, color=color)

# Configure the first y-axis
ax1.set_ylabel('Frequency of Usage\n(times per day)', fontsize=11, color='black')
ax1.set_title('Greetings Across Cultures:\nFrequency & Sentiment of Phrases', 
              fontsize=14, fontweight='bold', pad=20)
ax1.set_xticks(x)
ax1.set_xticklabels(languages, fontsize=10)
ax1.legend(title='Greeting Phrase', loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0.)

# Annotate each bar with frequency values
for i in range(len(languages)):
    for j in range(len(greetings)):
        ax1.text(i + offset[j], usage_frequency[i, j] + 0.5, f'{usage_frequency[i, j]}', 
                 ha='center', va='bottom', fontsize=9, color='black')

# Rotate x-axis labels for better readability
plt.xticks(rotation=0, ha='center')

# Add grid lines to enhance readability
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Create a twin Axes sharing the x-axis
ax2 = ax1.twinx()
ax2.plot(x, sentiment_scores, color='purple', marker='o', markersize=8, linewidth=2, linestyle='-', label='Sentiment Score')
ax2.set_ylabel('Sentiment Score', fontsize=11, color='purple')
ax2.tick_params(axis='y', labelcolor='purple')

# Annotate sentiment scores
for i, score in enumerate(sentiment_scores):
    ax2.annotate(f'{score:.2f}', xy=(i, score), xytext=(0, 10), textcoords='offset points',
                 ha='center', va='bottom', fontsize=9, color='purple')

# Adjust the layout to prevent overlapping
fig.tight_layout()

# Display the plot
plt.show()