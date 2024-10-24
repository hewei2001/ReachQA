import matplotlib.pyplot as plt

# Define the sectors and their GDP contributions
sectors = [
    'Advanced Electronics', 
    'Biotechnology', 
    'Robotics', 
    'Renewable Energy Mfg.', 
    'Autonomous Vehicles', 
    'Precision Machinery'
]
gdp_contribution = [40, 20, 15, 10, 10, 5]

# Define colors for each sector
colors = ['#FFD700', '#8A2BE2', '#FF4500', '#32CD32', '#00CED1', '#FF6347']

# Create a pie chart, then adjust to make it a ring chart
fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    gdp_contribution,
    labels=sectors,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'edgecolor': 'gray', 'linewidth': 1, 'width': 0.3}, # Set width for ring effect
    pctdistance=0.85
)

# Add a center circle to emphasize the ring style
centre_circle = plt.Circle((0, 0), 0.50, fc='white')
ax.add_artist(centre_circle)

# Customize text on the chart
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Add a central label inside the ring
ax.text(0, 0, 'Technotopia\n2023', fontsize=14, fontweight='bold', ha='center', va='center')

# Title and legend
plt.title("Industrial Growth in Technotopia:\nGDP Contribution by Manufacturing Sectors", 
          fontsize=16, fontweight='bold', ha='center', pad=20)
plt.legend(wedges, sectors, title="Sectors", loc='center left', 
           bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Ensure the layout is tidy
plt.tight_layout()

# Display the plot
plt.show()