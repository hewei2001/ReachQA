import matplotlib.pyplot as plt

# Define pasta types and their preferences (percentages)
pasta_types = ['Spaghetti', 'Penne', 'Fettuccine', 'Ravioli', 'Lasagna']
preferences = [30, 25, 20, 15, 10]

# Colors for each pasta type
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']

# Create a pie chart
fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(preferences, labels=pasta_types, autopct='%1.1f%%',
                                  startangle=90, colors=colors, explode=(0.1, 0, 0, 0, 0),
                                  wedgeprops=dict(edgecolor='w'))

# Customize text properties for readability
for text in texts:
    text.set_fontsize(11)
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(11)

# Set a title for the chart
plt.title("The Great Pasta Preference Survey:\nA Slice of Italian Flavors in 2023",
          fontsize=16, fontweight='bold')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()