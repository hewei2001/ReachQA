import matplotlib.pyplot as plt
import numpy as np

# Age groups
age_groups = ['18-24', '25-34', '35-44', '45-54', '55+']

# Coffee types
coffee_types = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Cold Brew']

# Data for the average number of cups consumed per week for each coffee type by age group
consumption_data = np.array([
    [5, 3, 4, 2, 1],  # 18-24
    [4, 5, 2, 3, 2],  # 25-34
    [3, 4, 4, 4, 3],  # 35-44
    [2, 3, 3, 5, 4],  # 45-54
    [1, 2, 3, 4, 5]   # 55+
])

# Bar width and positions for grouped bar chart
bar_width = 0.15
x_positions = np.arange(len(age_groups))

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting each coffee type's consumption across age groups
colors = plt.cm.cividis(np.linspace(0, 1, len(coffee_types)))

for i, (coffee_type, color) in enumerate(zip(coffee_types, colors)):
    bars = ax.bar(x_positions + i * bar_width, consumption_data[:, i], bar_width, label=coffee_type, color=color)
    
    # Adding text labels on top of the bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, f'{int(yval)}', ha='center', va='bottom', fontsize=10)

# Titles and labels
ax.set_title("Caffeination Nation:\nCoffee Preferences Across Age Groups", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Age Groups', fontsize=14)
ax.set_ylabel('Average Cups per Week', fontsize=14)
ax.set_xticks(x_positions + bar_width * 2)
ax.set_xticklabels(age_groups, fontsize=12)

# Grid and legend
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax.legend(title='Coffee Type', fontsize=12)

# Rotate x-axis labels if needed to prevent overlap
plt.xticks(rotation=45)

# Adjust layout to prevent clipping of title/labels
plt.tight_layout()

# Display the plot
plt.show()