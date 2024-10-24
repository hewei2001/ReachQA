import matplotlib.pyplot as plt

# Ingredients and their respective proportions in the dream potion
ingredients = [
    "Stardust", "Moonbeam Essence", "Whispering Breeze", 
    "Dewdrop Elixir", "Glistening Crystal", "Aurora Glow"
]
proportions = [25, 20, 15, 20, 10, 10]

# Assign mystical colors to each potion ingredient
colors = ['#b0e0e6', '#ffdead', '#add8e6', '#90ee90', '#d3d3d3', '#ffb6c1']

# Optional explode setting to highlight a particular slice
explode = (0.1, 0, 0, 0, 0, 0)  # Slightly separate the 'Stardust' slice

# Create the plot
fig, ax = plt.subplots(figsize=(8, 8))

# Plotting the pie chart
wedges, texts, autotexts = ax.pie(
    proportions, 
    labels=ingredients, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors,
    explode=explode,
    wedgeprops=dict(edgecolor='white'),
    shadow=True
)

# Styling the text
plt.setp(autotexts, size=11, weight='bold', color='black')
plt.setp(texts, size=12)

# Title of the chart with a whimsical font weight
plt.title('Dream Potion Composition in Alchemistoria\nIngredient Proportions', fontsize=14, fontweight='bold', color='#4b0082')

# Adding a legend for clarity, positioned outside the chart
ax.legend(wedges, ingredients, title="Ingredients", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()