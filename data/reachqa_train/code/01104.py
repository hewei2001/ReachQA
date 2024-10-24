import matplotlib.pyplot as plt

# Data for the chart
civilizations = ['Egyptians', 'Romans', 'Mayans', 'Mesopotamians', 'Greeks']
allocation_percentages = [25, 20, 15, 10, 30]
colors = ['#FFD700', '#FF6347', '#ADFF2F', '#8A2BE2', '#1E90FF']

# Plotting
fig, ax = plt.subplots(figsize=(9, 9))

# Create a donut pie chart
wedges, texts, autotexts = ax.pie(
    allocation_percentages,
    labels=civilizations,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    pctdistance=0.75,
    explode=[0.05]*5,  # Slightly 'explode' each slice for emphasis
    shadow=True  # Add shadow for depth
)

# Enhance text properties for better visibility
for text in autotexts:
    text.set_color('white')
    text.set_fontsize(11)

# Adding a legend
ax.legend(wedges, civilizations,
          title="Civilizations",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# Title
plt.title("Ancient Worlds Initiative:\nArchaeological Fund Allocation",
          fontsize=16, fontweight='bold')

# Automatic layout adjustment
plt.tight_layout()

# Display the plot
plt.show()