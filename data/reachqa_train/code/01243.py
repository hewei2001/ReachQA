import matplotlib.pyplot as plt

# Data for the ring chart
labels = ['Waste Management', 'Public Transport', 'Renewable Energy', 'Urban Greenery', 'Air Quality']
scores = [25, 20, 30, 15, 10]
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

# Create a ring chart (donut chart)
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the outer ring
wedges, texts, autotexts = ax.pie(scores, labels=labels, autopct='%.1f%%', startangle=140, counterclock=False,
                                  colors=colors, wedgeprops=dict(width=0.3, edgecolor='white'))

# Add a central circle to turn the pie chart into a ring chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Ensure the pie is a perfect circle
ax.axis('equal')

# Title inside the ring
ax.text(0, 0, 'EcoVille\nGreen Score', horizontalalignment='center', verticalalignment='center',
        fontsize=14, weight='bold', color='darkgreen')

# Title for the whole chart
plt.title('Contribution to EcoVille\'s Green Score by Sector', fontsize=16, weight='bold', pad=20)

# Adjust label font size for better visibility
plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=10)

# Add legend with optimal positioning
ax.legend(wedges, labels, title="Sectors", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()