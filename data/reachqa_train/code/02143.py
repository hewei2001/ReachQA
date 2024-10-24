import matplotlib.pyplot as plt

# Data for the pie chart
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 'Fantasy', 'Romance']
market_share = [35, 25, 15, 10, 8, 7]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
explode = (0.1, 0, 0, 0, 0, 0)  # Explode the Fiction slice

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    market_share, labels=genres, colors=colors, autopct='%1.1f%%',
    startangle=140, pctdistance=0.85, wedgeprops=dict(edgecolor='w'),
    explode=explode
)

# Draw circle for a 'donut' style
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

# Customize annotations
plt.setp(autotexts, size=10, weight="bold", color="navy")
plt.setp(texts, size=12)

# Adding title
ax.set_title("Global Book Genre Preferences in 2023", fontsize=16, fontweight='bold', pad=20)

# Adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()