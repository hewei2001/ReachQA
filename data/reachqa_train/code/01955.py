import matplotlib.pyplot as plt

# Data for the chart: investment distribution in renewable energy sectors
sectors = ['Solar Power', 'Wind Power', 'Hydroelectric Energy', 'Geothermal Energy', 'Biomass Energy']
investment_distribution = [35, 25, 20, 10, 10]  # Percentage of investment in each sector

# Define distinct colors for each segment for visual differentiation
colors = ['#FFD700', '#7CFC00', '#4682B4', '#FF6347', '#8A2BE2']

# Create the ring chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    investment_distribution, 
    labels=sectors, 
    autopct='%1.1f%%', 
    startangle=140,
    colors=colors, 
    wedgeprops=dict(width=0.3, edgecolor='w'),  # Create ring effect
    textprops=dict(color="black")
)

# Style the percentage text
plt.setp(autotexts, size=10, weight="bold")

# Add title and center label
ax.set_title('Innovation in Renewable Energy:\nGlobal Sector Investment in 2040', fontsize=14, fontweight='bold', pad=20)
plt.text(0, 0, '2040', fontsize=20, ha='center', va='center', fontweight='bold', color='gray', alpha=0.5)

# Add a legend with descriptions
ax.legend(wedges, sectors, title="Energy Sectors", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()