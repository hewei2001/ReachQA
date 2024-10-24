import matplotlib.pyplot as plt

# Define the EV brands and their market shares
brands = ['ElectroMotion', 'GreenWheels', 'VoltVoyage', 'EcoCruise', 'SkyLine EVs', 'Others']
market_shares = [35, 25, 15, 10, 8, 7]

# Define colors for each brand
colors = ['#4CAF50', '#2196F3', '#FF9800', '#FF5722', '#9C27B0', '#607D8B']

# Select one brand to explode for emphasis
explode = (0.1, 0, 0, 0, 0, 0)  # Exploding the 'ElectroMotion' slice

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))
wedges, texts, autotexts = ax.pie(
    market_shares, labels=brands, colors=colors, startangle=140, explode=explode,
    autopct='%1.1f%%', pctdistance=0.85,
    wedgeprops=dict(edgecolor='white', linewidth=2, alpha=0.9),
    textprops=dict(color="w", fontsize=10)
)

# Customize the text in wedges
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

# Add a circle at the center to transform the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Set the title with line breaks for better visibility
plt.title('Market Share of Electric Vehicles in EcoCity - 2023\n(Percentage of Total Vehicles)', fontsize=14, fontweight='bold')

# Add legend outside the chart
plt.legend(wedges, brands, title='Brands', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Automatically adjust layout for better presentation
plt.tight_layout()

# Display the plot
plt.show()