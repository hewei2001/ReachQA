import matplotlib.pyplot as plt

# Define the preference categories and their percentages
categories = [
    'Internet Connectivity', 
    'Cost of Living', 
    'Climate', 
    'Cultural Opportunities', 
    'Time Zone Compatibility', 
    'Safety'
]
percentages = [25, 20, 15, 15, 15, 10]

# Define colors for the pie chart
colors = ['#4CAF50', '#FF9800', '#2196F3', '#9C27B0', '#FF5722', '#607D8B']

# Define explode settings to highlight the most significant category
explode = (0.1, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    percentages, 
    labels=categories, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors,
    explode=explode,
    shadow=True,
    textprops=dict(color="w", fontsize=10, weight="bold"),
    wedgeprops=dict(edgecolor='w', linewidth=1.5)
)

# Set a title for the pie chart
ax.set_title(
    "Digital Nomad Lifestyle Preferences in 2023:\n"
    "Key Considerations for Remote Work Locations",
    fontsize=16, weight='bold', pad=20
)

# Customize the appearance of the legend
ax.legend(
    wedges, categories, title="Preferences",
    loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10
)

# Ensure the pie is a circle
ax.axis('equal')

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the chart
plt.show()