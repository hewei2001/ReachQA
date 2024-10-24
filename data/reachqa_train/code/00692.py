import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import ConnectionPatch

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

# Enhanced color palette
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Custom function to format the percentage labels in the pie chart
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{:.1f}%\n({:d})'.format(pct, val)
    return my_autopct

# Create a sector pie chart for each continent with enhancements
def plot_sector_pie_chart(data, continent, cuisines, colors):
    fig, ax = plt.subplots(figsize=(9, 7), subplot_kw=dict(aspect="equal"))
    
    # Create pie chart
    wedges, texts, autotexts = ax.pie(
        data,
        labels=cuisines,
        autopct=make_autopct(data),
        startangle=90,
        colors=colors,
        pctdistance=0.85,
        wedgeprops=dict(width=0.3, edgecolor='w', linewidth=0.5),
        textprops=dict(size=9)
    )
    
    # Draw a white circle at the center to create a sector look
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)
    
    # Add a title and ensure the pie is round
    ax.set_title(f"{continent}:\nCulinary Preferences", fontsize=14)
    
    # Add a legend with a new arrangement
    ax.legend(wedges, cuisines, title="Cuisine Types", loc="upper right", bbox_to_anchor=(1.25, 1))
    
    # Add enhanced labels with connections
    for i, autotext in enumerate(autotexts):
        autotext.set_color('white')
        autotext.set_fontsize(8)
        autotext.set_fontweight('bold')
        conn = ConnectionPatch(
            (0.9 * np.cos(np.radians((wedges[i].theta1 + wedges[i].theta2)/2)),
             0.9 * np.sin(np.radians((wedges[i].theta1 + wedges[i].theta2)/2))),
            (1.2 * np.cos(np.radians((wedges[i].theta1 + wedges[i].theta2)/2)),
             1.2 * np.sin(np.radians((wedges[i].theta1 + wedges[i].theta2)/2))),
            'data', 'data',
            arrowstyle='->', color='gray'
        )
        ax.add_artist(conn)
    
    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Show the plot
    plt.show()

# Plot each continent's data
for continent, data in data_by_continent.items():
    plot_sector_pie_chart(data, continent, cuisines, colors)