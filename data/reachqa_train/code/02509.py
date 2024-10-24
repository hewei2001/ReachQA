import numpy as np
import matplotlib.pyplot as plt

# Define the decades
decades = np.arange(1980, 2030, 10)

# Artificial data representing the frequency of word usage in "mentions per million words"
# These represent trends over each decade from the 1980s to the 2020s
internet = [5, 10, 50, 200, 300]
sustainability = [10, 30, 50, 100, 150]
groovy = [150, 100, 50, 20, 5]
emoji = [0, 0, 5, 50, 100]
blockchain = [0, 0, 0, 10, 75]

# Organize the data into a list of lists
data = [internet, sustainability, groovy, emoji, blockchain]

# Define labels for each word
words = ['Internet', 'Sustainability', 'Groovy', 'Emoji', 'Blockchain']

# Define colors for each word's line
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each word's frequency as a line in the chart
for i, word in enumerate(words):
    ax.plot(decades, [d + np.random.normal(0, 5) for d in data[i]], 
            marker='o', color=colors[i], linewidth=2, linestyle='-', label=word)

# Customize the chart title and axis labels
ax.set_title("Evolving Language Usage Over the Decades:\nExploring Word Popularity", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Mentions per Million Words', fontsize=12)

# Ensure x and y axis limits are set for clarity
ax.set_xlim(1980, 2020)
ax.set_ylim(0, 350)

# Display a legend to identify different lines
ax.legend(title='Words', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))

# Add grid lines to improve readability
ax.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust subplots to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()