import matplotlib.pyplot as plt
import numpy as np

# Define the data
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Australia']
cuisines = ['Italian', 'Chinese', 'Indian', 'Mexican', 'French', 'American']

# Percentage of cuisine preferences by continent
data_by_continent = {
    "Africa": [20, 15, 30, 10, 15, 10],
    "Asia": [5, 40, 35, 5, 10, 5],
    "Europe": [30, 10, 10, 10, 25, 15],
    "North America": [15, 10, 10, 25, 10, 30],
    "South America": [10, 5, 15, 40, 5, 25],
    "Australia": [25, 15, 10, 15, 20, 15]
}

# Colors for each cuisine category
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Create a sector pie chart for each continent
def plot_sector_pie_chart(data, continent, cuisines, colors):
    plt.figure(figsize=(8, 6))
    
    # Create pie chart
    wedges, texts, autotexts = plt.pie(
        data,
        labels=cuisines,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        pctdistance=0.85,
        wedgeprops=dict(width=0.3, edgecolor='w', linewidth=0.5),
        textprops=dict(size=10)
    )
    
    # Draw a white circle at the center to create a sector look
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    
    # Add a title and make sure the pie is round
    plt.gca().set(aspect="equal", title=f"{continent}:\nCulinary Preferences")
    
    # Add a legend
    plt.legend(wedges, cuisines, title="Cuisine Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    # Automatically adjust layout to prevent overlap
    plt.tight_layout()

    # Show the plot
    plt.show()

# Plot each continent's data
for continent, data in data_by_continent.items():
    plot_sector_pie_chart(data, continent, cuisines, colors)