import matplotlib.pyplot as plt

# Data for the chart
coffee_types = ['Espresso', 'Cappuccino', 'Latte', 'Mocha', 'Americano', 'Cold Brew']
preferences = [25, 20, 18, 15, 12, 10]

# Colors for each segment
colors = ['#6F4E37', '#D2B48C', '#FFF8DC', '#8B4513', '#A0522D', '#2E8B57']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the ring chart using pie function and setting width for a donut shape
wedges, texts, autotexts = ax.pie(preferences, labels=coffee_types, autopct='%1.1f%%', startangle=90, 
                                  colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w'))

# Draw a circle in the center to enhance the donut appearance
centre_circle = plt.Circle((0, 0), 0.6, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Setting label and text properties
for text in texts:
    text.set_fontsize(11)
    text.set_color('navy')

for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('darkblue')

# Adding a central label in the ring
ax.text(0, 0, 'Coffee Preferences\n2023', horizontalalignment='center', verticalalignment='center', 
        fontsize=14, fontweight='bold', color='navy')

# Title and layout adjustments
plt.title('Global Gourmet Coffee Preferences\nAmong Enthusiasts in 2023', fontsize=15, fontweight='bold', pad=20)
plt.tight_layout()

# Display the plot
plt.show()