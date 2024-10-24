import matplotlib.pyplot as plt
import squarify  # Make sure to install the squarify library if you haven't already using: pip install squarify

# Define the architectural styles and data
styles = ["Gothic", "Modern", "Colonial", "Baroque"]

# Area covered by each style in square kilometers for each district (for demonstration)
central_district = [2.5, 4.0, 1.5, 2.0]
north_district = [3.0, 2.0, 2.5, 1.0]
south_district = [1.5, 5.0, 1.0, 2.5]
west_district = [2.0, 3.5, 3.0, 1.5]

# Combine all data into a single list
style_data = [
    {'label': 'Gothic\nCentral', 'value': central_district[0], 'color': '#8B0000'},
    {'label': 'Modern\nCentral', 'value': central_district[1], 'color': '#4682B4'},
    {'label': 'Colonial\nCentral', 'value': central_district[2], 'color': '#DAA520'},
    {'label': 'Baroque\nCentral', 'value': central_district[3], 'color': '#8A2BE2'},
    {'label': 'Gothic\nNorth', 'value': north_district[0], 'color': '#A52A2A'},
    {'label': 'Modern\nNorth', 'value': north_district[1], 'color': '#6495ED'},
    {'label': 'Colonial\nNorth', 'value': north_district[2], 'color': '#FFD700'},
    {'label': 'Baroque\nNorth', 'value': north_district[3], 'color': '#9370DB'},
    {'label': 'Gothic\nSouth', 'value': south_district[0], 'color': '#DC143C'},
    {'label': 'Modern\nSouth', 'value': south_district[1], 'color': '#5F9EA0'},
    {'label': 'Colonial\nSouth', 'value': south_district[2], 'color': '#FFD700'},
    {'label': 'Baroque\nSouth', 'value': south_district[3], 'color': '#8A2BE2'},
    {'label': 'Gothic\nWest', 'value': west_district[0], 'color': '#B22222'},
    {'label': 'Modern\nWest', 'value': west_district[1], 'color': '#00CED1'},
    {'label': 'Colonial\nWest', 'value': west_district[2], 'color': '#B8860B'},
    {'label': 'Baroque\nWest', 'value': west_district[3], 'color': '#9370DB'},
]

# Plotting the tree map
fig = plt.figure(figsize=(12, 8))
plt.title('Architectural Diversity in Arcaville:\nA District-Wise Analysis', fontsize=16, fontweight='bold', pad=20)
squarify.plot(sizes=[item['value'] for item in style_data], 
              label=[item['label'] for item in style_data],
              color=[item['color'] for item in style_data], 
              alpha=0.8,
              edgecolor='black',
              linewidth=1)

# Add axis off and a tight layout to make the chart look better
plt.axis('off')
plt.tight_layout()

# Show the plot
plt.show()