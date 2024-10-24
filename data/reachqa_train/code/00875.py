import matplotlib.pyplot as plt

# Data for tea production share by region
regions = ['Asia', 'Africa', 'South America', 'Europe', 'North America', 'Oceania']
production_share = [60, 20, 10, 5, 3, 2]

# Colors for each region
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Create the ring chart
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Wedge properties for ring effect
wedges, texts, autotexts = ax.pie(
    production_share, 
    labels=regions, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    pctdistance=0.85, 
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Customize text inside the chart
plt.setp(autotexts, size=10, weight="bold", color='black')
plt.setp(texts, size=12)

# Add a central label inside the ring
ax.text(0, 0, "Global\nTea Production", horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold')

# Set title with a split to avoid overcrowding
ax.set_title("A Global Brew:\nTea Production Share by Region in 2023", fontsize=14, fontweight='bold', pad=20)

# Place the legend outside the plot
ax.legend(wedges, regions, title="Regions", loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)

# Improve layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()