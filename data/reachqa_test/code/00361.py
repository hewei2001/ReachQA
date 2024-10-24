import matplotlib.pyplot as plt
import numpy as np

# Data
ages = np.arange(5, 13)
reading = [0.2, 0.4, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95]
writing = [0.1, 0.3, 0.5, 0.6, 0.7, 0.75, 0.8, 0.85]
listening = [0.3, 0.5, 0.7, 0.8, 0.9, 0.92, 0.95, 0.98]
speaking = [0.2, 0.4, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95]
vocabulary = [0.1, 0.2, 0.4, 0.5, 0.6, 0.65, 0.7, 0.75]

# Create figure and axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot data (line chart)
ax1.plot(ages, reading, marker='o', label='Reading', linewidth=2, linestyle='-', color='blue')
ax1.plot(ages, writing, marker='s', label='Writing', linewidth=2, linestyle='--', color='green')
ax1.plot(ages, listening, marker='^', label='Listening', linewidth=2, linestyle='-.', color='red')
ax1.plot(ages, speaking, marker='D', label='Speaking', linewidth=2, linestyle=':', color='purple')
ax1.plot(ages, vocabulary, marker='*', label='Vocabulary', linewidth=2, linestyle=(0, (3, 1, 1, 1)), color='orange')

# Set title and labels
ax1.set_title("Language Proficiency Development in Children Aged 5-12\n"
              "Average Proficiency Levels Across Five Language Skills")
ax1.set_xlabel("Age")
ax1.set_ylabel("Proficiency Level")

# Set grid and legend
ax1.grid(True)
ax1.legend(loc='upper right', fontsize='small')

# Plot data (bar chart)
ax2.bar(ages, reading, label='Reading', color='blue')
ax2.bar(ages, writing, bottom=reading, label='Writing', color='green')
ax2.bar(ages, listening, bottom=[i+j for i, j in zip(reading, writing)], label='Listening', color='red')
ax2.bar(ages, speaking, bottom=[i+j+k for i, j, k in zip(reading, writing, listening)], label='Speaking', color='purple')
ax2.bar(ages, vocabulary, bottom=[i+j+k+l for i, j, k, l in zip(reading, writing, listening, speaking)], label='Vocabulary', color='orange')

# Set title and labels
ax2.set_title("Language Proficiency Development in Children Aged 5-12\n"
              "Stacked Bar Chart of Proficiency Levels")
ax2.set_xlabel("Age")
ax2.set_ylabel("Proficiency Level")

# Set grid and legend
ax2.grid(True)
ax2.legend(loc='upper right', fontsize='small')

# Show plot
plt.tight_layout()
plt.show()