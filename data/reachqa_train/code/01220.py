import matplotlib.pyplot as plt

# Data for fairytale creatures popularity
creatures = ['Dragons', 'Unicorns', 'Elves', 'Fairies', 'Giants']
popularity = [25, 20, 15, 25, 15]  # Percentages

# Assigning distinct colors for each creature type
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Explode the slices to highlight the categories
explode = (0.1, 0, 0, 0, 0)  # Only 'Dragons' slice is slightly exploded

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(popularity, labels=creatures, colors=colors, autopct='%1.1f%%', startangle=140, 
       explode=explode, shadow=True, wedgeprops={'edgecolor': 'black'}, textprops={'fontsize': 12})

# Title for the pie chart
ax.set_title("Popularity of Fairytale Creatures\nin Children's Books (Last Decade)", 
             fontsize=14, fontweight='bold', pad=20)

# Legend configuration
ax.legend(creatures, title="Creatures", loc="upper right", bbox_to_anchor=(1.2, 0.8))

# Automatically adjust layout for the best fit
plt.tight_layout()

# Display the pie chart
plt.show()