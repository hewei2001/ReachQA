import matplotlib.pyplot as plt

# Define data for the pie chart
flowers = ['Roses', 'Yellow Tulips', 'Lilies', 'Daisies', 'Lavenders']
meanings = [40, 20, 15, 15, 10]
colors = ['#FF6347', '#FFD700', '#D8BFD8', '#FFDEAD', '#9ACD32']
explode = (0.1, 0, 0, 0, 0)  # Explode the 'Roses' slice to highlight it

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(meanings, labels=flowers, autopct='%1.1f%%', startangle=140,
       colors=colors, explode=explode, shadow=True, wedgeprops={'edgecolor': 'black'})

# Ensure the pie chart is a circle
ax.axis('equal')

# Title of the pie chart, split into two lines for better readability
plt.title('The Language of Flowers:\nSymbolism in Floristry')

# Use tight layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()