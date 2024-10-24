import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Define the EV brands and their market shares
brands = ['ElectroMotion', 'GreenWheels', 'VoltVoyage', 'EcoCruise', 'SkyLine EVs', 'Others']
market_shares = [35, 25, 15, 10, 8, 7]

# Define colors for each brand with gradients
colors = ['#4CAF50', '#2196F3', '#FF9800', '#FF5722', '#9C27B0', '#607D8B']

# Select brands to explode for emphasis
explode = (0.1, 0.1, 0.1, 0, 0, 0)  # Exploding the top three brands

# Create a pie chart with shadow effect
fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))
wedges, texts, autotexts = ax.pie(
    market_shares, labels=brands, colors=colors, startangle=140, explode=explode,
    autopct=lambda pct: f'{pct:.1f}%\n({int(pct/100.*sum(market_shares))}k)',
    pctdistance=0.85, shadow=True,
    wedgeprops=dict(edgecolor='w', linewidth=2, alpha=0.9),
    textprops=dict(color="w", fontsize=10)
)

# Enhance text properties for better visibility
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

# Add a circle at the center to transform the pie chart into a donut chart
centre_circle = Circle((0, 0), 0.70, fc='white', linewidth=1.25, edgecolor='w')
ax.add_artist(centre_circle)

# Set the title with line breaks for better visibility
plt.title('Market Share of Electric Vehicles in EcoCity - 2023\n(Percentage of Total Vehicles)', fontsize=14, fontweight='bold')

# Add legend outside the chart
plt.legend(wedges, brands, title='Brands', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Automatically adjust layout for better presentation
plt.tight_layout()

# Display the plot
plt.show()