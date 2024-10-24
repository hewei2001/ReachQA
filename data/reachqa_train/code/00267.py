import matplotlib.pyplot as plt

# Data for caffeine content in different beverages (in mg)
beverages = ['Coffee', 'Tea', 'Energy Drinks', 'Soft Drinks', 'Chocolate']
caffeine_content = [95, 47, 80, 30, 9]  # average caffeine content in mg

# Colors for each section of the pie chart
colors = ['#8c564b', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Explode the slices to emphasize Coffee and Energy Drinks
explode = (0.1, 0, 0.1, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(caffeine_content, labels=beverages, autopct='%1.1f%%', startangle=90,
       colors=colors, explode=explode, shadow=True, wedgeprops={'edgecolor': 'black'})

# Add a title to the pie chart
plt.title('Distribution of Average Caffeine Content\nin Popular Beverages', fontsize=16, fontweight='bold', pad=20)

# Add a legend with a title
plt.legend(title='Beverage Types', loc='upper right', bbox_to_anchor=(1.15, 1))

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()