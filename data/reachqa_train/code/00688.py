import matplotlib.pyplot as plt
import squarify

# Data for the tree map
labels = ['Streaming\nServices', 'Social\nMedia', 'News\nPlatforms', 'Podcasts', 'E-books']
sizes = [35, 30, 20, 10, 5]  # Percentage share of daily media consumption
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create a figure
fig = plt.figure(figsize=(12, 8))

# Plot the tree map using squarify
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8, edgecolor="white", linewidth=2,
              text_kwargs={'fontsize': 14, 'weight': 'bold', 'color': 'black'})

# Set the title and remove axes
plt.title("Digital Media Consumption Trends\nin 2023", fontsize=18, weight='bold', pad=20)
plt.axis('off')

# Add a descriptive footnote for context
plt.figtext(0.5, 0.01, "Each section represents the average daily percentage of digital media consumption per user.", 
            ha="center", fontsize=10, color='gray')

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()