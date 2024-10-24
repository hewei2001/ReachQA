import matplotlib.pyplot as plt

# Data for the pie chart
art_movements = ['Impressionism', 'Cubism', 'Surrealism', 
                 'Abstract Expressionism', 'Pop Art', 
                 'Minimalism', 'Contemporary Art']

influence_percentages = [20, 15, 18, 12, 10, 8, 17]

# Define colors for each art movement
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f']

# Exploding the slice for 'Contemporary Art' to highlight it
explode = (0, 0, 0, 0, 0, 0, 0.1)

# Plotting the pie chart
plt.figure(figsize=(10, 8))
plt.pie(influence_percentages, labels=art_movements, autopct='%1.1f%%', startangle=140, 
        colors=colors, explode=explode, wedgeprops={'edgecolor': 'black'}, 
        textprops={'fontsize': 10}, shadow=True)

# Title of the chart with line break for better readability
plt.title("Influence of Major Art Movements\n in the Last Century", fontsize=14, pad=20)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Add a legend outside of the pie chart
plt.legend(title="Art Movements", loc='center left', bbox_to_anchor=(1, 0.5))

# Ensure the layout fits well within the plot window
plt.tight_layout()

# Display the pie chart
plt.show()