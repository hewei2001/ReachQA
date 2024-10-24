import matplotlib.pyplot as plt
import numpy as np

# Define the expanded decades and genres
decades = ['1800s', '1810s', '1820s', '1830s', '1840s', '1850s', '1860s', '1870s', '1880s', 
           '1890s', '1900s', '1910s', '1920s', '1930s', '1940s', '1950s', '1960s', '1970s', 
           '1980s', '1990s', '2000s', '2010s', '2020s', '2030s', '2040s', '2050s']

genres = ['Mystery', 'Romance', 'Historical Fiction', 'Science Fiction', 
          'Fantasy', 'Thriller', 'Non-Fiction', 'Drama', 'Horror', 'Biography']

# Fictional, complex pattern data
mystery = np.clip(np.abs(np.sin(np.linspace(0, 3*np.pi, len(decades)))*50 + 25), 0, 100)
romance = np.clip(np.abs(np.cos(np.linspace(0, 2.5*np.pi, len(decades)))*40 + 35), 0, 100)
historical_fiction = np.clip(np.abs(np.cos(np.linspace(0, 2*np.pi, len(decades)))*30 + 20), 0, 100)
science_fiction = np.linspace(0, 60, len(decades))
fantasy = np.linspace(60, 0, len(decades))
thriller = np.abs(np.sin(np.linspace(0, 4*np.pi, len(decades)))*30 + 20)
non_fiction = np.abs(np.sin(np.linspace(0, 1.5*np.pi, len(decades)))*30 + 25)
drama = np.abs(np.sin(np.linspace(0, 2.8*np.pi, len(decades)))*35 + 15)
horror = np.abs(np.sin(np.linspace(0, 3.5*np.pi, len(decades)))*25 + 10)
biography = np.linspace(30, 20, len(decades))

# Stack the data for the stacked area chart
data = np.vstack([mystery, romance, historical_fiction, science_fiction, fantasy, 
                  thriller, non_fiction, drama, horror, biography])

# Create a stacked area chart with added subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the stacked area chart
ax.stackplot(decades, data, labels=genres, 
             colors=['#4c72b0', '#55a868', '#c44e52', '#8172b3', '#ccb974', 
                     '#64b5cd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22'], alpha=0.85)

# Title and labels with multi-line for clarity
ax.set_title("Evolution of Literary Genres:\nA Journey Through the Centuries (1800 - 2050)", fontsize=16, pad=20)
ax.set_xlabel("Decade", fontsize=12)
ax.set_ylabel("Popularity (Imaginary Units)", fontsize=12)

# Adding a legend
ax.legend(loc='upper left', title="Genres", fontsize=10, bbox_to_anchor=(1.05, 1))

# Enhancing the aesthetics with gridlines and layout
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Adjust x-axis labels to avoid overlap
plt.xticks(rotation=45, ha='right')

# Ensure layout is adjusted to fit everything nicely
plt.tight_layout()

# Display the chart
plt.show()