import matplotlib.pyplot as plt

# Define the mystical resources and their distribution percentages
resources = ['Mana Crystals', 'Enchanted Herbs', 'Dragon Scales', 'Phoenix Feathers', 'Star Dust']
distribution_percentages = [25, 30, 15, 10, 20]

# Define colors for each segment of the pie chart
colors = ['#8A2BE2', '#7FFF00', '#FF4500', '#FF69B4', '#FFD700']

# Explode the largest segment to highlight it
explode = (0, 0.1, 0, 0, 0)  # Only explode the second segment (Enchanted Herbs)

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    distribution_percentages, 
    explode=explode,
    labels=resources, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    shadow=True,
    wedgeprops=dict(width=0.4, edgecolor='w')
)

# Customize text properties
plt.setp(autotexts, size=12, weight='bold', color='white')
plt.setp(texts, size=12, weight='bold')

# Set title
ax.set_title(
    "Mystic Realm Resource Allocation:\nA Glimpse into Magical Abundance (3023)", 
    fontsize=16, 
    weight='bold', 
    pad=20
)

# Add legend outside the plot
ax.legend(
    wedges, resources, title="Resources", 
    loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10
)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()