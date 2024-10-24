import matplotlib.pyplot as plt

# Data definition for ocean exploration objectives
objectives = ['Scientific Research', 'Biodiversity\nAssessment', 'Resource\nExploration', 'Climate\nMonitoring', 'Pollution\nStudies']
proportions = [30, 20, 25, 15, 10]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFD700', '#FF6347']
explode = (0.1, 0, 0, 0, 0)  # Explode the first slice for emphasis

# Create the pie chart
fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(
    proportions, 
    labels=objectives, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=explode,
    shadow=True,
    textprops=dict(color="w"),
    wedgeprops=dict(edgecolor='w', linewidth=2)
)

# Set title and configure text elements
plt.title("Priorities in Ocean Exploration Missions:\nA Decadal Overview", fontsize=16, fontweight='bold', pad=20)
plt.setp(autotexts, size=10, weight="bold")

# Position the legend outside the pie chart
ax.legend(wedges, objectives, title="Objectives", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout for better appearance
fig.tight_layout()

# Display the plot
plt.show()