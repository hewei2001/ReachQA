import matplotlib.pyplot as plt

# Define the generations and their respective coffee preferences (in percentage)
generations = ["Silent Generation", "Baby Boomers", "Generation X", "Millennials", "Generation Z"]
coffee_preferences = {
    "Espresso": [20, 25, 30, 20, 35],
    "Cappuccino": [15, 20, 25, 30, 28],
    "Latte": [18, 15, 20, 25, 22],
    "Americano": [30, 30, 15, 15, 10],
    "Mocha": [10, 10, 10, 10, 5],
    "Flat White": [7, 5, 0, 0, 0],
    "Cold Brew": [0, 0, 0, 0, 0]
}

# Define colors for each coffee type
colors = ['#8B4513', '#CD853F', '#F5DEB3', '#DEB887', '#D2691E', '#8A3324', '#2F4F4F']

# Create a figure and axis for each generation
fig, axes = plt.subplots(2, len(generations)//2 + 1, figsize=(20, 10))
axes = axes.flatten()

# Plot the sector pie charts for each generation
for i, generation in enumerate(generations):
    data = [coffee_preferences[coffee][i] for coffee in coffee_preferences]
    explode = [0.05 if coffee == "Cappuccino" else 0 for coffee in coffee_preferences]
    wedges, texts, autotexts = axes[i].pie(data, labels=coffee_preferences.keys(), autopct='%1.1f%%', 
                                           startangle=90, colors=colors, pctdistance=0.85, explode=explode)
    for text in texts + autotexts:
        text.set_fontsize(8)
    axes[i].set_title(f"{generation}\nCoffee Preferences", fontsize=12, fontweight='bold')
    axes[i].axis('equal')

# Stacked bar chart
bar_width = 0.15
x = range(len(generations))
bottom_values = [0] * len(generations)

for coffee, color in zip(coffee_preferences.keys(), colors):
    preferences = [coffee_preferences[coffee][i] for i in range(len(generations))]
    plt.bar(x, preferences, bar_width, bottom=bottom_values, color=color, label=coffee)
    bottom_values = [sum(val) for val in zip(bottom_values, preferences)]

plt.xticks([r + bar_width*3 for r in range(len(generations))], generations, fontsize=10, rotation=45)
plt.title("Cumulative Coffee Preferences\nAcross Generations", fontsize=14, fontweight='bold')
plt.ylabel('Percentage', fontsize=12)
plt.xlabel('Generations', fontsize=12)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Adjust layout
plt.tight_layout(rect=[0, 0, 0.9, 0.95])

# Main title for all plots
plt.suptitle("Exploration of Coffee Preferences\nAcross Generations and Their Variations", fontsize=16, fontweight='bold', y=1.05)

plt.show()