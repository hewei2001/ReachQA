import matplotlib.pyplot as plt
import numpy as np

# Fantasy sub-genres and corresponding sales data
sub_genres = ['Epic Fantasy', 'Urban Fantasy', 'Dark Fantasy', 'High Fantasy', 'Sword & Sorcery']
sales = [1200, 800, 600, 1000, 400]

# Define colors for each genre segment
colors = ['#FF5733', '#33FFCE', '#FF33A8', '#335BFF', '#B8FF33']

# Create figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 9), subplot_kw=dict(aspect="equal"))

# Plot a pie chart to create a donut effect
wedges, texts, autotexts = ax.pie(
    sales,
    labels=sub_genres,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w', linestyle='-', linewidth=1.5),
    explode=(0.05, 0.08, 0.05, 0.02, 0.1),
    shadow=True
)

# Add a central circle to transform the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Set the title of the chart with a multi-line approach
plt.title('Enchanted Pages:\nFantasy Sub-Genre Sales Distribution\nLast Quarter', fontsize=18, fontweight='bold', ha='center')

# Customize autotexts (percentage labels inside the chart)
plt.setp(autotexts, size=10, weight="bold", color='darkblue')

# Customize the category labels on the chart
plt.setp(texts, size=12, color='black')

# Add annotations outside the wedges
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 - wedge.theta1)/2. + wedge.theta1
    y = np.sin(np.deg2rad(angle))
    x = np.cos(np.deg2rad(angle))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    ax.annotate(f'{sales[i]} copies',
                xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, fontsize=10, color='darkred',
                arrowprops=dict(arrowstyle="-", color='gray'))

# Add a legend
ax.legend(wedges, sub_genres, title="Sub-Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Enhance layout
plt.tight_layout()

# Display the donut pie chart
plt.show()