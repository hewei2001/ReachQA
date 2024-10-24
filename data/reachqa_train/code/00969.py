import matplotlib.pyplot as plt

# Data for the chart
operating_systems = ['Windows', 'macOS', 'Linux', 'Chrome OS', 'BSD', 'Others']
market_share = [40, 25, 20, 5, 3, 7]

# Colors for the operating systems
colors = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f', '#edc949']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Create a ring chart
wedges, texts, autotexts = ax.pie(
    market_share,
    labels=operating_systems,
    colors=colors,
    autopct='%1.1f%%',
    pctdistance=0.85,
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Add a central circle to make the pie a ring chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Ensures the pie chart is a circle
ax.axis('equal')

# Customize text and legend properties
plt.setp(autotexts, size=10, weight="bold", color="white")
plt.setp(texts, size=12)

# Set chart title
ax.set_title("2023 Operating System Market Share\nTech Community Snapshot", fontsize=16, fontweight='bold', y=1.05)

# Draw legend outside the ring chart
ax.legend(wedges, operating_systems, title="Operating Systems", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout to fit everything nicely
plt.tight_layout()

# Display the chart
plt.show()