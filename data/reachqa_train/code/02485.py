import matplotlib.pyplot as plt

# Data for shoe popularity
shoe_types = ['Heels', 'Sneakers', 'Boots', 'Loafers', 'Sandals']
popularity = [25, 30, 20, 15, 10]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Create a donut pie chart
wedges, texts, autotexts = ax.pie(
    popularity, 
    labels=shoe_types, 
    autopct='%1.1f%%',
    startangle=140, 
    colors=colors, 
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    shadow=True
)

# Draw center circle for 'donut' effect
centre_circle = plt.Circle((0, 0), 0.55, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# Set the title with multiple lines
plt.title("Shoe Trends of the Century:\nA Fashion Odyssey", fontsize=16, fontweight='bold')

# Customize the text properties
for text in texts:
    text.set_color('grey')
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

# Add legend
ax.legend(wedges, shoe_types, title="Shoe Types", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the chart
plt.show()