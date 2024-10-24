import matplotlib.pyplot as plt

# Define the data
labels = ['Smart Speakers', 'Smart Thermostats', 'Smart Lights', 'Smart Security Systems', 'Smart Kitchen Appliances']
sizes = [25, 15, 20, 18, 22]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create a figure and axis for plotting
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(aspect="equal"))

# Create the donut pie chart
wedges, texts, autotexts = ax.pie(
    sizes, 
    labels=labels, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140, 
    pctdistance=0.85,
    wedgeprops=dict(width=0.3), 
    explode=(0.05, 0.05, 0.05, 0.05, 0.05)
)

# Draw a white circle at the center to create the donut shape
center_circle = plt.Circle((0,0),0.55,fc='white')
fig.gca().add_artist(center_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# Adding title with line break for clarity
plt.title('Adoption Rates of Smart Home Technologies\n(A Hypothetical Survey)', fontsize=16, fontweight='bold', y=1.05)

# Customize the text of the percentage labels
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_size(12)
    autotext.set_weight('bold')

# Add a legend
ax.legend(wedges, labels, title="Technologies", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Automatically adjust the layout to ensure everything fits without overlapping
plt.tight_layout()

# Display the chart
plt.show()