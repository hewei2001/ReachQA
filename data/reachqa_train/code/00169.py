import matplotlib.pyplot as plt

# Data: Projected global energy contributions in 2050 (in percentage)
energy_sources = ['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal', 'Nuclear', 'Others']
contributions = [30, 25, 20, 10, 5, 7, 3]

# Colors for the slices
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c2f0c2']

# Create the donut pie chart
plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(
    contributions,
    labels=energy_sources,
    colors=colors,
    startangle=140,
    autopct='%1.1f%%',
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    textprops=dict(color='darkgrey', fontsize=10)
)

# Enhance the aesthetics of the autotexts (percentage labels)
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontweight('bold')

# Draw a white circle in the center to create a donut effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Title and layout adjustments
plt.title("Global Energy Sources in 2050:\nA Renewed Vision", fontsize=14, weight='bold')
plt.tight_layout()

# Add a legend that is outside the pie chart to avoid overlap
plt.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Show the plot
plt.show()