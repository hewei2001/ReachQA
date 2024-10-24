import matplotlib.pyplot as plt

# Data for the chart
art_forms = ['Calligraphy', 'Pottery', 'Dance', 'Weaving', 'Painting']
interest_percentages = [25, 15, 30, 10, 20]

# Colors for each section of the donut chart
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the pie chart and a circular center for the donut effect
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    interest_percentages, 
    labels=art_forms, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'), 
    textprops=dict(color="black", fontsize=10, weight='bold'))

# Draw a circle at the center to make it a donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that the pie is drawn as a circle.
ax.axis('equal')

# Title of the chart
plt.title('Popularity of Traditional Art Forms\nat Harmony Arts Festival 2023', fontsize=14, fontweight='bold')

# Customize autotexts (percentage labels)
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Annotate the highest and lowest percentage areas
ax.annotate('Most Popular', xy=(0.1, 0.7), xytext=(-1.5, 1.2),
            arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle="arc3,rad=.5"),
            fontsize=10, backgroundcolor='white')

ax.annotate('Least Popular', xy=(-0.6, -0.4), xytext=(-1.5, -1.2),
            arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle="arc3,rad=-.5"),
            fontsize=10, backgroundcolor='white')

# Add a legend
plt.legend(wedges, art_forms, title="Art Forms", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()