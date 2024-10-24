import matplotlib.pyplot as plt

# Categories of ocean species and their percentage representation in marine biodiversity
species_categories = ['Fish', 'Mollusks', 'Crustaceans', 'Coral', 'Marine Mammals', 'Others']
biodiversity_percentage = [35, 20, 15, 10, 5, 15]

# Assign distinct colors for each category for visual appeal
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Create the figure and axis for the ring chart
fig, ax = plt.subplots(figsize=(9, 9))

# Generate the ring chart with wedges
wedges, texts, autotexts = ax.pie(
    biodiversity_percentage,
    labels=species_categories,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='white')
)

# Customize the appearance of text for clarity
plt.setp(autotexts, size=11, weight="bold", color="darkblue")
plt.setp(texts, size=13, weight="bold")

# Central title in the ring for context
ax.text(0, 0, 'Ocean\nBiodiversity', ha='center', va='center', fontsize=14, color='gray', weight='bold')

# Outer title with thematic context, split into lines for readability
plt.title("Global Ocean Species Diversity\nHighlighting Marine Biodiversity", 
          fontsize=16, fontweight='bold', color='navy', pad=20)

# Add a circle at the center to complete the ring appearance
center_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(center_circle)

# Adjust legend to avoid occlusion of chart elements
ax.legend(wedges, species_categories, title="Species Categories", loc="center left", 
          bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Ensure the aspect ratio is equal so the plot is circular
ax.axis('equal')

# Automatically adjust the layout for better visibility
plt.tight_layout()

# Display the ring chart
plt.show()