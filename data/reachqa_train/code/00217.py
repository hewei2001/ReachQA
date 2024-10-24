import matplotlib.pyplot as plt

# Define languages and respective percentages of the population
languages = ['Elvish', 'Dwarvish', 'Orkish', 'Merfolk', 'Pixie', 'Human Common']
percentages = [25, 15, 20, 10, 5, 25]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Create the ring chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    percentages, labels=languages, colors=colors, autopct='%1.1f%%',
    startangle=140, pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w')
)

# Add a circle in the center to complete the ring effect
center_circle = plt.Circle((0, 0), 0.55, fc='white')
fig.gca().add_artist(center_circle)

# Ensure equal aspect ratio for a perfect circle
ax.axis('equal')

# Customize text appearance
plt.setp(autotexts, size=10, weight="bold", color="black")
plt.setp(texts, size=12)

# Add a legend outside the chart
plt.legend(wedges, languages, title="Languages", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Title with a line break for clarity
plt.title("Linguistic Diversity\nin the World of Linguistica", fontsize=14, weight='bold', pad=20)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()