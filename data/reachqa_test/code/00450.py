import numpy as np
import matplotlib.pyplot as plt

# Define the quarters
quarters = np.array(['Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 
                     'Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022', 
                     'Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023'])

# Create artificial data for word count and confidence level
word_count = np.array([1500, 2200, 3500, 4000, 
                       4500, 6000, 7500, 9000, 
                       9500, 11000, 13000, 14500])
confidence_level = np.array([3, 4, 5, 6, 
                             7, 6, 8, 9, 
                             9, 10, 10, 10])

# New data for average words per day
average_words_per_day = np.array([50, 74, 116, 133, 
                                   150, 200, 250, 300, 
                                   316, 366, 433, 483])

# Create the plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Plotting the word count
ax1.plot(quarters, word_count, label='Word Count', color='blue', marker='o', 
         linewidth=2, linestyle='-', alpha=0.7)
ax1.set_xlabel('Quarter', fontsize=14, fontweight='semibold')
ax1.set_ylabel('Word Count', fontsize=14, fontweight='semibold', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_title('The Journey of a Young Aspiring Author\nTracking Writing Progress Over Time', 
              fontsize=16, fontweight='bold', pad=15)
ax1.grid(axis='both', linestyle='--', alpha=0.6)

# Creating a second y-axis for confidence level
ax2_ = ax1.twinx()
ax2_.plot(quarters, confidence_level, label='Confidence Level', color='orange', marker='s', 
          linewidth=2, linestyle='--', alpha=0.7)
ax2_.set_ylabel('Confidence Level (1-10)', fontsize=14, fontweight='semibold', color='orange')
ax2_.tick_params(axis='y', labelcolor='orange')

# Adding legends
ax1.legend(loc='upper left', fontsize=10)
ax2_.legend(loc='upper right', fontsize=10)

# Annotate key points on the word count
annotations = {
    2: "First Story Completed",
    7: "Gained Confidence!",
    11: "Self-Published!"
}
for index, text in annotations.items():
    ax1.annotate(text, xy=(quarters[index], word_count[index]), 
                 xytext=(quarters[index], word_count[index] + 1000),
                 arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

# Second subplot: Average Words Per Day
ax2.bar(quarters, average_words_per_day, color='green', alpha=0.6, label='Avg Words per Day')
ax2.set_ylabel('Average Words per Day', fontsize=14, fontweight='semibold', color='green')
ax2.set_title('Average Words Written per Day\nAlongside Writing Progress', fontsize=16, fontweight='bold', pad=10)
ax2.tick_params(axis='y', labelcolor='green')
ax2.grid(axis='y', linestyle='--', alpha=0.6)
ax2.legend(loc='upper right', fontsize=10)

# Adjust x-axis label rotation
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()