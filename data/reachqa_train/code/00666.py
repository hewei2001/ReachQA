import matplotlib.pyplot as plt

# Data: Solar energy systems in urban households
labels = ['Rooftop Systems', 'Ground-Mounted Systems', 'Community Solar Projects', 'BIPV']
sizes = [45, 25, 20, 10]  # Percentage of households
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Distinct color palette
explode = (0.05, 0, 0, 0)  # Emphasize the largest segment

# Create a donut pie chart
fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(
    sizes, explode=explode, labels=labels, autopct='%1.1f%%',
    startangle=140, colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.3),
    shadow=True, textprops=dict(color="black", weight='bold')
)

# Draw a circle for the donut shape
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Title and layout adjustments
ax.set_title('Solar Energy System Adoption in Urban Households - 2023', fontsize=16, fontweight='bold', loc='center', pad=20)
ax.axis('equal')  # Ensure the pie is drawn as a circle

# Enhance the legend with more detail
plt.legend(wedges, labels, title="System Type", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Auto adjust layout to avoid overlapping elements
plt.tight_layout()

# Display the plot
plt.show()