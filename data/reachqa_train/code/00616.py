import matplotlib.pyplot as plt
import numpy as np

# Define years from 2013 to 2023
years = np.arange(2013, 2024)

# Artificial data for sentiment scores
skepticism = np.array([-70, -68, -60, -55, -50, -45, -30, -20, -15, -10, 0])
curiosity = np.array([-20, -10, 0, 5, 10, 20, 30, 40, 50, 60, 70])
optimism = np.array([0, 5, 10, 15, 25, 35, 50, 65, 75, 85, 90])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each sentiment category
ax.plot(years, skepticism, label='Skepticism', color='red', linestyle='-', marker='o', linewidth=2)
ax.plot(years, curiosity, label='Curiosity', color='blue', linestyle='--', marker='s', linewidth=2)
ax.plot(years, optimism, label='Optimism', color='green', linestyle='-.', marker='^', linewidth=2)

# Highlight significant transitions
ax.annotate('Turning Point', xy=(2017, -30), xytext=(2015, -50),
            arrowprops=dict(facecolor='gray', shrink=0.05),
            fontsize=10, backgroundcolor='white', color='darkred')

ax.annotate('Tech Revolution', xy=(2021, 70), xytext=(2019, 75),
            arrowprops=dict(facecolor='gray', shrink=0.05),
            fontsize=10, backgroundcolor='white', color='darkblue')

# Add a title and labels
plt.title('Rise of the Robots:\nThe Evolution of AI Sentiment Over a Decade', 
          fontsize=18, fontweight='bold', loc='center')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Sentiment Score', fontsize=14)

# Set y-axis limits and customize ticks
plt.ylim(-80, 100)
plt.xticks(years)
plt.yticks(np.arange(-80, 101, 20))
plt.axhline(0, color='black', linewidth=1, linestyle='--')

# Add a grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Add a legend
plt.legend(title='Sentiment', loc='upper left', fontsize=12)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()