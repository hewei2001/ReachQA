import matplotlib.pyplot as plt

# Astrobiology topics and corresponding fictional interest data
topics = [
    'Mars Colonization',
    'Search for Extraterrestrial Intelligence',
    'Habitability of Exoplanets',
    'Microbial Life on Icy Moons',
    'Evolution in Extreme Environments'
]

interest_percentages = [25, 20, 30, 15, 10]

# Plotting the donut pie chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))

# Custom colors for each segment
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1']

# Create wedges for the donut chart
wedges, texts, autotexts = ax.pie(
    interest_percentages,
    labels=topics,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    pctdistance=0.85,  # Move the percentage labels closer to the center
    explode=[0.05, 0, 0.05, 0, 0]  # Explode specific segments for emphasis
)

# Customize the annotation text style
plt.setp(autotexts, size=10, weight="bold", color="black")

# Adding the central circle to create the donut shape
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Title and additional context
plt.title("Astrobiology Interests Among\nSpace Enthusiasts in 2050", fontsize=14, fontweight='bold', pad=20)

# Adding a legend with descriptions
ax.legend(wedges, topics, title="Topics", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the chart
plt.show()