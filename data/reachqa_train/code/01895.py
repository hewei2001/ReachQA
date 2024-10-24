import matplotlib.pyplot as plt

# Define the fruit categories and their corresponding consumption percentages
fruits = ["Apples", "Bananas", "Oranges", "Grapes", "Mangoes", "Berries"]
percentages = [25, 20, 15, 10, 18, 12]

# Define colors to differentiate each segment of the pie chart
colors = ['#FF9999', '#FFCC99', '#99CCFF', '#FF6666', '#FFFF99', '#66B3FF']

# Optional explode parameter to highlight Mangoes
explode = (0, 0, 0, 0, 0.1, 0)

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(percentages, labels=fruits, autopct='%1.1f%%', startangle=90,
                                  colors=colors, textprops=dict(color="black", fontsize=10), explode=explode,
                                  shadow=True)

# Title of the pie chart
ax.set_title("Global Fruit Consumption Preferences in 2023", fontsize=14, fontweight='bold', pad=20)

# Draw a circle in the center to make it a donut chart for aesthetic enhancement
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Customize legend
ax.legend(wedges, fruits, title="Fruits", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Annotate each slice with a descriptive label
annotations = ["Rich in fiber", "Great for energy", "High in Vitamin C", "Antioxidant-rich", "Exotic choice", "Berry benefits"]
for i, a in enumerate(autotexts):
    a.set_text(f"{annotations[i]}\n{a.get_text()}")
    a.set_fontsize(9)

# Automatically adjust layout to prevent clipping of labels or legends
plt.tight_layout()

# Display the plot
plt.show()