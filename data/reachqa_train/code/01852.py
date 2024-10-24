import matplotlib.pyplot as plt

# Data representing the percentage of different digital detox practices
practices = ['Meditation', 'Nature Walks', 'Digital-Free Zones', 'Reading', 'Art Therapy']
percentages = [30, 20, 15, 25, 10]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']

# Create the ring chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=practices,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='white')
)

# Draw a circle at the center of the pie to make it a ring
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# Title with line breaks for better visibility
plt.title("Digital Detox Distribution:\nModern Relaxation Practices", fontsize=14, weight='bold', pad=20)

# Customize the text on the wedges
for text in texts:
    text.set_size(10)
    text.set_weight('bold')
    text.set_color('darkblue')
    
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_weight('bold')
    autotext.set_size(9)

# Add a central text inside the ring
plt.text(0, 0, 'Digital Detox', horizontalalignment='center', verticalalignment='center', fontsize=12, color='black', weight='bold')

# Add a legend outside the chart
ax.legend(wedges, practices, title="Practices", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()