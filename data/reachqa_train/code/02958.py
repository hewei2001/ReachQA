import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Popularity data (in millions of albums/streams) for each genre
rock_popularity = np.array([150, 145, 140, 138, 135, 130, 125, 120, 118, 115, 110, 105, 102, 100, 98, 96, 95, 94, 92, 90, 88])
pop_popularity = np.array([110, 120, 130, 150, 170, 180, 200, 220, 250, 270, 290, 310, 330, 350, 360, 370, 380, 390, 400, 410, 420])
hiphop_popularity = np.array([50, 60, 70, 80, 95, 110, 125, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400])
electronic_popularity = np.array([20, 25, 30, 35, 40, 50, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340])
jazz_popularity = np.array([80, 78, 76, 74, 72, 70, 68, 65, 62, 60, 58, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47])

# Create the plot
plt.figure(figsize=(16, 9))
plt.style.use('ggplot')  # Use a valid Matplotlib style

# Subtle background gradient
plt.gca().set_facecolor('#f0f0f5')
plt.gca().set_alpha(0.85)

# Plot the line chart for each genre
plt.plot(years, rock_popularity, label='Rock', color='#FF6347', linestyle='-', linewidth=2.5, marker='o')
plt.plot(years, pop_popularity, label='Pop', color='#87CEEB', linestyle='--', linewidth=2.5, marker='^')
plt.plot(years, hiphop_popularity, label='Hip-Hop', color='#32CD32', linestyle='-.', linewidth=2.5, marker='s')
plt.plot(years, electronic_popularity, label='Electronic', color='#FFD700', linestyle=':', linewidth=2.5, marker='d')
plt.plot(years, jazz_popularity, label='Jazz', color='#8A2BE2', linestyle='-', linewidth=1.5, marker='x')

# Fill between lines to show gaps
plt.fill_between(years, rock_popularity, pop_popularity, color='gray', alpha=0.1)

# Title and labels with multiline title for improved readability
plt.title("The Melodic Journey:\nEvolution of Music Genres (2000-2020)", fontsize=18, fontweight='bold', pad=30)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Popularity (Millions of Albums/Streams)', fontsize=14)

# Legend with adjusted placement
plt.legend(title='Music Genres', title_fontsize=12, fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))

# Gridlines and minor ticks for better visual guidance
plt.grid(True, linestyle='--', alpha=0.7)
plt.minorticks_on()

# Rotate x-axis labels for better readability
plt.xticks(years, rotation=45)

# Additional Annotations
plt.annotate('Rise of Hip-Hop', xy=(2015, 300), xytext=(2010, 350), 
             arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10, color='darkblue')
plt.annotate('Peak of Pop', xy=(2020, 420), xytext=(2015, 380), 
             arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10, color='darkred')
plt.annotate('Electronic Surge', xy=(2012, 100), xytext=(2008, 150),
             arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10, color='darkgreen')

# Highlight key years with vertical lines
for year in [2010, 2015, 2020]:
    plt.axvline(x=year, color='gray', linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()