import matplotlib.pyplot as plt
import numpy as np

# Fantasy sub-genres and corresponding sales data
sub_genres = ['Epic Fantasy', 'Urban Fantasy', 'Dark Fantasy', 'High Fantasy', 'Sword & Sorcery']
sales = [1200, 800, 600, 1000, 400]

# Define colors for each genre segment
colors = ['#FF5733', '#33FFCE', '#FF33A8', '#335BFF', '#B8FF33']

# Create figure and axis for the plot
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(aspect="equal"))

# Plot a pie chart to create a donut effect
wedges, texts, autotexts = ax.pie(
    sales,
    labels=sub_genres,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    explode=(0.05, 0.05, 0.05, 0.05, 0.05),
    shadow=True
)

# Add a central circle to transform the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Set the title of the chart with a multi-line approach for clarity
plt.title('Enchanted Pages: Fantasy Sub-Genre Sales\nDistribution in Last Quarter', fontsize=16, fontweight='bold')

# Customize autotexts (percentage labels inside the chart)
plt.setp(autotexts, size=12, weight="bold", color='darkblue')

# Customize the category labels on the chart
plt.setp(texts, size=12, color='black')

# Add a legend to the chart for clarity, placing it outside the plot area
ax.legend(wedges, sub_genres, title="Sub-Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Ensure that the layout is tight so that everything fits well
plt.tight_layout()

# Display the donut pie chart
plt.show()