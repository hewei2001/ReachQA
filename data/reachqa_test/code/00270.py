import matplotlib.pyplot as plt

# Enhanced data for endangered species awareness
species = ['Amur Leopard', 'Javan Rhino', 'Mountain Gorilla', 'Vaquita', 'Sumatran Elephant',
           'Hawksbill Turtle', 'Saola', 'Tapanuli Orangutan', 'Yangtze Finless Porpoise']
awareness_proportions = [18.5, 10.5, 16.8, 8.2, 22.0, 5.5, 4.8, 6.4, 7.3]  # Sums to 100
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2',
          '#FF7F50', '#8B4513', '#2E8B57', '#4169E1']

# Create the main figure and axis
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the donut chart with autopct for percentage labels
wedges, texts, autotexts = ax.pie(awareness_proportions, colors=colors, labels=species, autopct='%1.1f%%',
                                  startangle=90, pctdistance=0.85,
                                  wedgeprops=dict(edgecolor='w'), explode=[0.05]*len(species), shadow=True)
# Draw a circle at the center of the pie to create a donut shape
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Maintain equal aspect ratio
ax.axis('equal')

# Enhanced title
ax.set_title("Endangered Animal Species Awareness\nDistribution & Analysis (2023)", fontsize=16, fontweight='bold', pad=20)

# Customize text for better readability
plt.setp(autotexts, size=10, weight="bold", color="darkblue")
plt.setp(texts, size=10)

# Add a legend outside the plot
ax.legend(wedges, species, title="Species", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Additional subplot for a bar chart displaying awareness vs. hypothetical population counts
population_counts = [70, 50, 80, 30, 120, 15, 10, 25, 18]  # Hypothetical data
fig, ax2 = plt.subplots(figsize=(10, 5))
ax2.bar(species, population_counts, color=colors, edgecolor='black')
ax2.set_title("Hypothetical Population Counts of Endangered Species", fontsize=14, fontweight='bold')
ax2.set_ylabel("Hypothetical Population (in hundreds)")
ax2.set_xticklabels(species, rotation=45, ha='right')

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the pie and bar charts
plt.show()