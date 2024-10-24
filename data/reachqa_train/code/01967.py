import matplotlib.pyplot as plt
import numpy as np

# Define the data for the chart
years = np.array([2010, 2012, 2014, 2016, 2018, 2020])
movies = ["Enchanted Dawn", "Mystic Warriors", "Dragon's Quest", 
          "Sorcerer's Secret", "Realm of Shadows", "Cursed Fate"]
earnings = np.array([150, 200, 250, 220, 300, 270])  # Earnings in millions USD

# Create the bar chart
plt.figure(figsize=(12, 7))
bars = plt.bar(years, earnings, color=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6'], edgecolor='gray', width=1.5)

# Annotate each bar with the earnings value
for bar, earning in zip(bars, earnings):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, f'{earning}M', 
             ha='center', va='bottom', fontsize=10, color='darkslategray')

# Add title and axis labels
plt.title("Box Office Performance of the Enchanted Series\n(2010-2020)", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Release Year", fontsize=12)
plt.ylabel("Earnings (Million USD)", fontsize=12)

# Add x-tick labels as movie titles and adjust rotation
plt.xticks(years, movies, rotation=45, ha='right')

# Add gridlines to the chart
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()