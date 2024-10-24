import matplotlib.pyplot as plt

# Define the generations and their respective coffee preferences (in percentage)
generations = ["Baby Boomers", "Generation X", "Millennials"]
coffee_preferences = {
    "Espresso": [25, 30, 20],
    "Cappuccino": [20, 25, 30],
    "Latte": [15, 20, 25],
    "Americano": [30, 15, 15],
    "Mocha": [10, 10, 10]
}

# Define colors for each coffee type for the pie chart
colors = ['#8B4513', '#CD853F', '#F5DEB3', '#DEB887', '#D2691E']

# Create a figure and axis
fig, ax = plt.subplots(1, len(generations), figsize=(18, 6))

# Plot the sector pie charts for each generation
for i, generation in enumerate(generations):
    data = [coffee_preferences[coffee][i] for coffee in coffee_preferences]
    explode = [0.05 if coffee == "Cappuccino" else 0 for coffee in coffee_preferences]  # Highlight Cappuccino
    wedges, texts, autotexts = ax[i].pie(data, labels=coffee_preferences.keys(), autopct='%1.1f%%', startangle=90,
                                         colors=colors, pctdistance=0.85, explode=explode)
    # Enhance text readability
    for text in texts + autotexts:
        text.set_fontsize(10)
    
    # Title for each subplot
    ax[i].set_title(f"{generation}\nCoffee Preferences", fontsize=14, fontweight='bold')
    ax[i].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Add a central title
plt.suptitle("Exploration of Coffee Preferences\nAcross Different Generations", fontsize=16, fontweight='bold', y=1.02)

# Automatically adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Adding a legend outside the plots for clarity
fig.legend(coffee_preferences.keys(), loc='upper center', ncol=5, fontsize=11, bbox_to_anchor=(0.5, -0.05))

# Display the plot
plt.show()