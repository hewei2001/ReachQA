import matplotlib.pyplot as plt

# Data representing the number of travelers (in millions) visiting each continent
travelers = [8, 25, 40, 15, 7, 5, 2]
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Australia', 'Antarctica']

# Define colors for each continent
colors = ['#FFD700', '#FF6347', '#87CEEB', '#32CD32', '#FF69B4', '#800080', '#A9A9A9']

# Plot the pie chart
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(
    travelers, 
    labels=continents, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    shadow=True, 
    explode=[0, 0.1, 0.1, 0, 0, 0, 0]  # Explode Asia and Europe slices for emphasis
)

# Customize the text properties
plt.setp(autotexts, size=10, weight="bold", color="white")
plt.setp(texts, size=12, weight="bold")

# Title and legend
plt.title('World Travel Trends in 2023\nPercentage of Travelers by Continent', fontsize=16, fontweight='bold')
plt.legend(wedges, continents, title='Continents', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()