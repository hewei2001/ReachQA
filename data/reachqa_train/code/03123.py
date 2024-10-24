import matplotlib.pyplot as plt

# Streaming services and their corresponding subscribers in millions
streaming_services = ['Netflix', 'Disney+', 'Amazon Prime Video', 'Hulu', 'Apple TV+']
subscribers = [230, 160, 150, 48, 40]

# Colors for the pie chart segments
colors = ['#FF5733', '#33FFCE', '#FF33FF', '#33FF57', '#335BFF']

# Explode the largest segment slightly to highlight it
explode = (0.1, 0, 0, 0, 0)

# Create a pie chart
plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(
    subscribers, 
    labels=streaming_services, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=90,
    explode=explode,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3)  # Donut shape
)

# Customize the text labels
for text in texts:
    text.set_size(12)
    text.set_color('black')
for autotext in autotexts:
    autotext.set_size(12)
    autotext.set_color('white')

# Add title
plt.title(
    "The Rise of Streaming Services\nin Global Entertainment: 2023",
    fontsize=16,
    fontweight='bold',
    color='darkblue',
    pad=20
)

# Draw the circle in the middle for donut chart appearance
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Ensure the pie chart is drawn as a circle
plt.axis('equal')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()