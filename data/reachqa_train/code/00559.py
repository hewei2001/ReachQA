import matplotlib.pyplot as plt

# Data for the pie chart
sectors = ['Quantum Computing', 'Artificial Intelligence', 'Renewable Energy', 'Space Exploration', 'Biotechnology']
funding_distribution = [20, 30, 25, 15, 10]  # Percentage of funding for each sector

# Colors for each sector
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Explode the second slice (Artificial Intelligence) for emphasis
explode = (0, 0.1, 0, 0, 0)

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    funding_distribution, explode=explode, labels=sectors, colors=colors, autopct='%1.1f%%',
    startangle=140, pctdistance=0.85, wedgeprops={'edgecolor': 'black'}, shadow=True
)

# Draw a circle at the center to make it a donut chart for a modern look
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Customize text properties for better readability
for text in texts + autotexts:
    text.set_fontsize(10)
    text.set_color('black')

# Adjust the aspect ratio to be equal so that pie is drawn as a circle
ax.axis('equal')

# Title of the pie chart
plt.title("Funding Distribution for\nFuturistic Innovations in 2050", fontsize=14, fontweight='bold', pad=20)

# Legend positioning
plt.legend(wedges, sectors, title="Sectors", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout to prevent overlap and ensure clarity
plt.tight_layout()

# Show the plot
plt.show()