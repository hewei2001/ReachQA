import matplotlib.pyplot as plt

# Data for beverage preferences
labels = ['Coffee', 'Tea', 'Water', 'Soda', 'Energy Drinks']
sizes = [40, 20, 25, 10, 5]
colors = ['#8B4513', '#D2691E', '#1E90FF', '#FF4500', '#FFD700']
explode = (0.1, 0, 0, 0, 0)  # explode the first slice (Coffee) to highlight it

# Create a donut pie chart
fig, ax = plt.subplots(figsize=(9, 7))
wedges, texts, autotexts = ax.pie(
    sizes, 
    explode=explode, 
    labels=labels, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140, 
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    shadow=True
)

# Styling adjustments
plt.setp(autotexts, size=10, weight="bold", color='white')
plt.setp(texts, size=12)

# Draw a white circle in the center to enhance the donut effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='white')
fig.gca().add_artist(centre_circle)

# Title
plt.title("Daily Beverage Preferences\nin a Modern Office", size=16, fontweight='bold', va='center')

# Add a legend
plt.legend(wedges, labels, title="Beverages", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Ensure layout is clear and elements do not overlap
plt.tight_layout()

# Display the chart
plt.show()