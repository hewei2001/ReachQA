import matplotlib.pyplot as plt

# Data for the original donut chart
regions = ['South America', 'Africa', 'Asia', 'Europe', 'North America']
contributions = [25, 20, 15, 30, 10]
colors = ['#8B4513', '#D2691E', '#DAA520', '#CD853F', '#DEB887']

# Data for the new bar chart
production_tons = [400000, 200000, 300000, 100000, 150000]

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Plot the donut chart
wedges, texts, autotexts = ax1.pie(
    contributions, 
    labels=regions, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Center circle for the donut effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax1.add_artist(centre_circle)

ax1.axis('equal')
ax1.set_title('Coffee Culture Around the World\nA Flavorful Journey', fontsize=15, pad=20, color='darkred', weight='bold')
plt.setp(autotexts, size=10, weight='bold', color='black')
plt.setp(texts, size=11, color='darkred')

# Legend for donut chart
ax1.legend(wedges, regions, title="Regions", loc="center left", bbox_to_anchor=(0.9, 0, 0.5, 1))

# Plot the bar chart
ax2.bar(regions, production_tons, color=colors, edgecolor='black')
ax2.set_title('Coffee Production by Region\n(in Tons)', fontsize=14, color='darkred', weight='bold')
ax2.set_ylabel('Production (Tons)', fontsize=12)
ax2.set_xlabel('Regions', fontsize=12)
ax2.set_xticklabels(regions, rotation=30, ha='right', fontsize=11, color='darkred')
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x/1000)}k'))

# Add data labels on the bars
for idx, value in enumerate(production_tons):
    ax2.text(idx, value + 5000, f'{value:,}', ha='center', va='bottom', fontsize=10, color='black')

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the combined plot
plt.show()