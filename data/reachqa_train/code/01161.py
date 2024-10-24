import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
genres = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Mystery', 'Biography', 'Self-Help', 'Historical Fiction', 'Young Adult', 'Crime Mystery']
percentages = [20, 15, 10, 10, 10, 5, 5, 10, 10, 5]
average_sales = [5000, 4500, 3000, 3500, 3200, 1500, 2000, 2800, 3100, 1900]  # Additional data for average sales per genre

# Colors for each genre
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2', '#ff6666', '#66ffb3', '#ffcc66']

fig, ax = plt.subplots(1, 2, figsize=(14, 7))

# Create a donut chart
wedges, texts, autotexts = ax[0].pie(percentages, labels=genres, autopct='%1.1f%%', startangle=90, 
                                     colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w'), 
                                     textprops=dict(color="black"))

for text in texts:
    text.set_fontsize(8)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(8)
    autotext.set_weight('bold')

centre_circle = plt.Circle((0,0),0.70,fc='white')
ax[0].add_artist(centre_circle)

ax[0].axis('equal')  

# Central label within the donut
ax[0].text(0, 0, 'Litopia\n2023', ha='center', va='center', fontsize=12, fontweight='bold')
ax[0].set_title('Book Genres Published in Litopia, 2023', fontsize=14, fontweight='bold', pad=20)

# Create a bar chart for average sales
ax[1].barh(genres, average_sales, color=colors, edgecolor='black')
ax[1].set_xlabel('Average Sales')
ax[1].set_title('Average Book Sales per Genre', fontsize=14, fontweight='bold', pad=20)
ax[1].invert_yaxis()

# Annotating each bar with their respective value
for i, v in enumerate(average_sales):
    ax[1].text(v + 100, i, str(v), color='black', va='center', fontsize=10)

# Tight layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()