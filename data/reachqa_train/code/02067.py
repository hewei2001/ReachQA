import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2015 to 2023
years = np.arange(2015, 2024)

# Define conservation efforts as percentage of total
reforestation = np.array([20, 25, 30, 35, 33, 31, 30, 28, 26])
wildlife_protection = np.array([15, 18, 20, 22, 25, 27, 29, 31, 30])
anti_deforestation_laws = np.array([65, 57, 50, 43, 42, 42, 41, 41, 44])

# Define a new dataset for budgets allocated (in millions) for each strategy
budgets = {
    'Reforestation': [10, 12, 15, 18, 20, 22, 21, 20, 19],
    'Wildlife Protection': [8, 9, 10, 12, 14, 15, 16, 18, 17],
    'Anti-Deforestation Laws': [30, 28, 25, 22, 21, 21, 20, 20, 21]
}

# Define colors for each strategy
colors = ['#66c2a5', '#fc8d62', '#8da0cb']

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 7), gridspec_kw={'width_ratios': [2, 1]})

# Plot the area chart on the first subplot
axs[0].stackplot(years, reforestation, wildlife_protection, anti_deforestation_laws,
                 labels=['Reforestation', 'Wildlife Protection', 'Anti-Deforestation Laws'],
                 colors=colors, alpha=0.8)
axs[0].set_title("Trends in Forest Conservation Strategies (2015-2023)\nGlobal Forest Conservation Initiative",
                 fontsize=14, fontweight='bold')
axs[0].set_xlabel("Year", fontsize=12)
axs[0].set_ylabel("Conservation Effort (%)", fontsize=12)
axs[0].set_xticks(years)
axs[0].set_xticklabels(years, rotation=45)
axs[0].set_yticks(np.arange(0, 101, 10))
axs[0].legend(loc='upper right', fontsize=10)
axs[0].grid(True, which='both', axis='y', linestyle='--', alpha=0.5)

# Plot the bar chart on the second subplot
bar_width = 0.25
x = np.arange(len(years))  # the label locations

# Create bars for each category
axs[1].bar(x - bar_width, budgets['Reforestation'], bar_width, label='Reforestation', color=colors[0])
axs[1].bar(x, budgets['Wildlife Protection'], bar_width, label='Wildlife Protection', color=colors[1])
axs[1].bar(x + bar_width, budgets['Anti-Deforestation Laws'], bar_width, label='Anti-Deforestation Laws', color=colors[2])

# Set title and labels for the second subplot
axs[1].set_title("Budget Allocation in Conservation Strategies\n(2015-2023)", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Year", fontsize=12)
axs[1].set_ylabel("Budget (Millions)", fontsize=12)
axs[1].set_xticks(x)
axs[1].set_xticklabels(years, rotation=45)
axs[1].legend(loc='upper left', fontsize=10)
axs[1].grid(True, which='both', axis='y', linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()