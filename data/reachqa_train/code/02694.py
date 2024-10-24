import matplotlib.pyplot as plt
import numpy as np

# Define the themes and their respective percentages
themes = ['Love', 'War', 'Adventure', 'Mystery', 'Philosophy']
percentages = [30, 20, 25, 15, 10]

# Choose colors that are visually appealing and distinct
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))

# Create the pie chart and use 'wedgeprops' to set the width for donut shape
wedges, texts, autotexts = ax.pie(
    percentages, labels=themes, autopct='%1.1f%%', startangle=90,
    colors=colors, wedgeprops=dict(width=0.3, edgecolor='w'), pctdistance=0.85)

# Enhance the labels and percentages
plt.setp(texts, size=10, weight="bold", color="navy")
plt.setp(autotexts, size=10, weight="bold", color="darkorange")

# Set the title with line breaks for better readability
ax.set_title("Distribution of Themes in Classic Literature\nExploring Timeless Narratives", 
             fontsize=14, weight='bold', color='darkgreen', pad=20)

# Add a legend with theme descriptions
ax.legend(wedges, themes, title="Themes", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()