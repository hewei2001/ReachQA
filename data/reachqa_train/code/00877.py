import matplotlib.pyplot as plt

# Data for the sectors
sectors = ['Smart Transportation', 'Green Energy', 'Digital Infrastructure', 'Urban Agriculture', 'Healthcare']
investment_distribution = [25, 20, 30, 10, 15]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6666']
explode = (0.1, 0, 0, 0, 0)  # explode Smart Transportation

# Create the pie chart
plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(
    investment_distribution, 
    labels=sectors, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=90, 
    pctdistance=0.85, 
    explode=explode,
    wedgeprops=dict(edgecolor='w')
)

# Draw center circle to create a donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Title and adjustments
plt.title("The Future of Cities: Innovation Investment\nDistribution in Urban Sectors by 2050", fontsize=14, fontweight='bold')
plt.tight_layout()

# Beautify autotexts
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_weight('bold')

# Display the pie chart
plt.show()