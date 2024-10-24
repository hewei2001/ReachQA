import matplotlib.pyplot as plt

# Define the gaming platforms and their respective popularity percentages
platforms = ['PC', 'PlayStation', 'Xbox', 'Nintendo Switch', 'Mobile']
popularity = [30, 25, 20, 15, 10]

# Define colors for each segment
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the pie chart with shadow for depth effect
wedges, texts, autotexts = ax.pie(
    popularity,
    labels=platforms,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(edgecolor='w'),
    explode=[0.1, 0.1, 0, 0, 0],  # Slight emphasis on PC and PlayStation
    shadow=True
)

# Set equal aspect ratio to ensure the pie chart is circular
ax.axis('equal')

# Customize text appearance
plt.setp(autotexts, size=10, weight='bold', color='black')
plt.setp(texts, size=12, weight='bold')

# Add a title with line breaks for readability
ax.set_title(
    "Popularity of Gaming Platforms in 2023:\n"
    "A Global Survey Analysis",
    fontsize=14, weight='bold', pad=20
)

# Add a legend outside the pie chart
ax.legend(
    wedges, platforms,
    title="Platforms",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=10
)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the pie chart
plt.show()