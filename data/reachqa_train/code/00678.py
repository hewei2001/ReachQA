import matplotlib.pyplot as plt
import squarify

# Define data for global music genre popularity
genres = ['Pop', 'Rock', 'Hip-hop', 'Jazz', 'Classical', 'Country', 
          'Electronic', 'Reggae', 'Latin', 'Folk']
popularity = [25, 15, 20, 10, 5, 8, 7, 3, 4, 3]

# Ensure all percentages add up to 100
assert sum(popularity) == 100, "Popularity percentages should add up to 100."

# Create color palette for genres
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0',
          '#ffb3e6','#c2f0c2','#ff6666','#c2f0c2','#ff66b2']

# Create a figure
plt.figure(figsize=(14, 10))

# Plot the treemap
squarify.plot(sizes=popularity, label=[f"{genre}\n{pop}%" for genre, pop in zip(genres, popularity)], 
              color=colors, alpha=0.8, text_kwargs={'fontsize':12, 'weight':'bold', 'color':'black'})

# Customize the plot with a title
plt.title('Global Music Genre Popularity in 2023', fontsize=20, fontweight='bold', color='navy')

# Remove axis for better appearance
plt.axis('off')

# Adjust layout for better fit and display
plt.tight_layout()

# Display the plot
plt.show()