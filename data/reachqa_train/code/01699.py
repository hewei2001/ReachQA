import matplotlib.pyplot as plt

# Define the categories and corresponding data
categories = [
    'Fish', 
    'Coral Reefs', 
    'Marine Mammals', 
    'Sea Turtles', 
    'Crustaceans', 
    'Mollusks', 
    'Other Marine Life'
]

percentages = [40, 15, 10, 5, 12, 8, 10]

# Define colors for each category for clear visualization
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Create a pie chart
plt.figure(figsize=(10, 8))

# Explode the Sea Turtles slice for emphasis
explode = (0, 0, 0, 0.1, 0, 0, 0)

wedges, texts, autotexts = plt.pie(
    percentages, 
    labels=categories, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors,
    pctdistance=0.85, 
    wedgeprops=dict(edgecolor='w'),
    explode=explode,
    shadow=True
)

# Adjust text sizes for better readability
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(10)

# Draw a central circle to make the pie chart look like a donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
plt.gca().add_artist(centre_circle)

# Set title with a thematic color and appropriate font size
plt.title('Marine Biodiversity Composition\nin the Oceans of Oceania', 
          fontsize=14, 
          color='navy', 
          fontweight='bold', 
          pad=20)

# Enhance layout to avoid overlap and ensure clarity
plt.tight_layout()

# Adding a legend outside the chart
plt.legend(wedges, categories, title="Species Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Display the plot
plt.show()