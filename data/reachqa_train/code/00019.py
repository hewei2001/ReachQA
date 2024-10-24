import matplotlib.pyplot as plt

# Galaxy names and their respective preference percentages
galaxies = ['Milky Way', 'Andromeda', 'Triangulum', 'Whirlpool', 'Sombrero', 'Pinwheel']
preferences = [20, 15, 10, 30, 15, 10]

# Define a distinct color for each galaxy
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Emphasize the 'Whirlpool Galaxy' by exploding it
explode = (0, 0, 0, 0.1, 0, 0)

# Create a pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(preferences, labels=galaxies, autopct='%1.1f%%', startangle=90,
       colors=colors, explode=explode, shadow=True)

# Adding a title, split into two lines for clarity
ax.set_title('Survey on Intergalactic Travel Preferences\nYear 2200', fontsize=14, weight='bold')

# Place legend outside the pie chart
ax.legend(galaxies, title='Galaxies', loc='upper left', bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()