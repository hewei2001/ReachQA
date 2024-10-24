import matplotlib.pyplot as plt

# Data for the pie chart
commodities = ['Rare Minerals', 'Advanced Biofuels', 'Exotic Spices', 'Nano-Circuit Elements', 'Anti-Gravity Devices']
values = [25, 20, 15, 30, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
explode = (0, 0.1, 0, 0, 0.1)  # Slightly explode the 'Advanced Biofuels' and 'Anti-Gravity Devices' sectors

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    values, explode=explode, colors=colors, labels=commodities, 
    autopct='%1.1f%%', startangle=140, pctdistance=0.85, 
    textprops=dict(color="black", fontsize=10)
)

# Customize the text in the chart
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('navy')

# Draw a circle at the center to create a donut-like appearance
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# Title and layout adjustments
plt.title('Galactic Trading Commodities\nDistribution - Year 2150', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()

# Add legend to describe the commodities
plt.legend(wedges, commodities, title="Commodities", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Show the plot
plt.show()