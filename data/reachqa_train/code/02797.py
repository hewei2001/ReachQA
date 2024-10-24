import matplotlib.pyplot as plt

# Data for budget allocation (as percentages)
labels = ['Planetary Defense', 'Scientific Research', 'Infrastructure Development', 
          'Education & Culture', 'Health & Wellbeing']
sizes = [25, 20, 30, 15, 10]
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1']
explode = (0.05, 0, 0.1, 0, 0)  # Emphasize 'Infrastructure Development' and slightly 'Planetary Defense'

# Create a donut pie chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=140,
    pctdistance=0.75, explode=explode, wedgeprops=dict(width=0.3, edgecolor='w'), shadow=True)

# Draw circle in the center to make it a donut
centre_circle = plt.Circle((0,0),0.65,fc='white')
fig.gca().add_artist(centre_circle)

# Adjust label font size and weight
plt.setp(autotexts, size=12, weight='bold')
plt.setp(texts, size=12, weight='semibold')

# Title and custom legend
ax.set_title('Interstellar Budget Allocation\nby the Galactic Council', fontsize=16, fontweight='bold', pad=20)
ax.legend(wedges, labels, title="Sectors", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')  

# Adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()