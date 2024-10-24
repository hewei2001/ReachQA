import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
genres = ['Fiction', 'Mystery', 'Science Fiction', 'Fantasy', 'Biography', 'Historical', 'Poetry']
percentages = [35, 20, 15, 10, 8, 7, 5]

# Colors for the genres
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c0c0c0']

# Creating the plot
fig, ax = plt.subplots()

# Pie chart with donut hole
wedges, texts, autotexts = ax.pie(
    percentages, 
    labels=genres, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    pctdistance=0.85, 
    wedgeprops=dict(width=0.3, edgecolor='w'),
    explode=[0.1 if genre == 'Fiction' else 0 for genre in genres],  # Highlighting 'Fiction'
    shadow=True
)

# Customizing the aesthetics
plt.setp(autotexts, size=10, weight="bold", color="navy")
plt.setp(texts, size=12)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Title with a creative approach
plt.title("The Art of Literature:\nA Glimpse into Literary Genres", pad=20, fontsize=14, fontweight='bold', color='darkgreen')

# Adding a legend with title
ax.legend(wedges, genres, title="Genres", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize='medium')

# Automatically adjust the subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()