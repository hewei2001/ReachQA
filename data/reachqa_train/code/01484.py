import matplotlib.pyplot as plt

# Data representing market share of programming languages
languages = ['Python', 'JavaScript', 'Java', 'C#', 'C++', 'Ruby', 'PHP']
market_shares = [35, 25, 15, 10, 7, 5, 3]  # Percentage distribution

# Colors for each programming language
colors = ['#377eb8', '#ff7f00', '#4daf4a', '#f781bf', '#a65628', '#984ea3', '#e41a1c']

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    market_shares, 
    labels=languages, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    pctdistance=0.85,  # Adjust text position inside the donut
    textprops=dict(color="black", fontsize=10, fontweight='bold')
)

# Draw a circle in the center to create a donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Add a shadow effect
ax.set_facecolor('#f2f2f2')  # Background color for the plot
plt.gca().set_aspect('equal')  # Equal aspect ratio ensures that the pie is circular

# Title and styling
plt.title('Current Market Share of Programming Languages\nin the Tech Industry (2023)', fontsize=14, fontweight='bold', pad=20)

# Create a legend
ax.legend(wedges, languages, title="Languages", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout to ensure nothing is clipped
plt.tight_layout()

# Display the plot
plt.show()