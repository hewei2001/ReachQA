import matplotlib.pyplot as plt

# Define the data for the Mediterranean diet components
components = ['Olive Oil', 'Grains', 'Vegetables', 'Fruits', 'Legumes']
values = [20, 30, 25, 15, 10]
colors = ['#ffcc80', '#ffeb3b', '#81c784', '#ff7043', '#4db6ac']
explode = (0.05, 0.05, 0.05, 0.05, 0.05)  # Slightly explode all slices for emphasis

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    values, labels=components, autopct='%1.1f%%', startangle=90, colors=colors,
    explode=explode, shadow=True, wedgeprops=dict(width=0.3, edgecolor='w')
)

# Adjust text properties for better visibility
plt.setp(autotexts, size=10, weight="bold", color='white')
plt.setp(texts, size=12)

# Title with line break for readability
ax.set_title("The Journey of Flavors:\nA Culinary Analysis of Mediterranean Diet Components",
             fontsize=16, fontweight='bold', pad=20)

# Add a legend
ax.legend(wedges, components, title="Components", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout for neatness
plt.tight_layout()

# Display the plot
plt.show()