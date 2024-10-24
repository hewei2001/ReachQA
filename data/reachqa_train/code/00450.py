import matplotlib.pyplot as plt
import numpy as np

# Define data for the pie chart
flowers = ['Roses', 'Yellow Tulips', 'Lilies', 'Daisies', 'Lavenders']
meanings = [40, 20, 15, 15, 10]
colors = ['#FF6347', '#FFD700', '#D8BFD8', '#FFDEAD', '#9ACD32']
explode = (0.1, 0.05, 0.05, 0.05, 0.05)  # Slightly explode all slices

# Creating a subplot with 2 charts
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Plotting the pie chart with additional enhancements
axs[0].pie(meanings, labels=flowers, autopct='%1.1f%%', startangle=140,
           colors=colors, explode=explode, shadow=True, wedgeprops={'edgecolor': 'black'})

# Donut chart (inner circle) to show the total
circle = plt.Circle((0, 0), 0.70, color='white')
axs[0].add_artist(circle)

axs[0].set_title('The Language of Flowers:\nSymbolism in Floristry')

# Adding a legend outside the pie chart
axs[0].legend(flowers, title="Flower Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Second plot: a comparison bar chart
compare_flowers = ['Sunflowers', 'Bluebells', 'Orchids', 'Carnations']
compare_meanings = [25, 18, 35, 22]
bar_colors = ['#FFA500', '#1E90FF', '#9932CC', '#FF69B4']

# Plotting the bar chart
axs[1].bar(compare_flowers, compare_meanings, color=bar_colors, edgecolor='black')
axs[1].set_title('Other Popular Flowers')
axs[1].set_ylabel('Symbolic Significance')
axs[1].set_xlabel('Flower Types')

# Tightly layout the subplots to handle text overlap
plt.tight_layout()

# Display the entire visualization
plt.show()