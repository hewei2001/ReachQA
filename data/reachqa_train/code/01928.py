import matplotlib.pyplot as plt
import numpy as np

# Define the data for each country and plant-based milk type (liters per capita)
countries = ['USA', 'Germany', 'India', 'Brazil', 'China']
almond_milk = np.array([4.2, 2.7, 1.5, 3.3, 2.0])
soy_milk = np.array([3.5, 1.9, 4.5, 2.8, 3.7])
oat_milk = np.array([2.8, 3.6, 0.7, 1.2, 2.9])
coconut_milk = np.array([1.6, 1.2, 2.1, 3.7, 1.5])
rice_milk = np.array([1.1, 1.3, 1.0, 0.9, 2.0])

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 7))
width = 0.15  # Width of each bar
y_pos = np.arange(len(countries))  # Positions for countries

# Plot bars for each milk type
bars1 = ax.barh(y_pos - 2*width, almond_milk, height=width, label='Almond Milk', color='sandybrown')
bars2 = ax.barh(y_pos - width, soy_milk, height=width, label='Soy Milk', color='lightgreen')
bars3 = ax.barh(y_pos, oat_milk, height=width, label='Oat Milk', color='wheat')
bars4 = ax.barh(y_pos + width, coconut_milk, height=width, label='Coconut Milk', color='lightblue')
bars5 = ax.barh(y_pos + 2*width, rice_milk, height=width, label='Rice Milk', color='tan')

# Customizing the plot
ax.set_yticks(y_pos)
ax.set_yticklabels(countries)
ax.set_xlabel('Liters per Capita', fontsize=12)
ax.set_title('Global Trends in Plant-Based Milk Consumption\nAcross Countries in 2023', fontsize=14, fontweight='bold')

# Adding grid lines for x-axis
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Adding legend
ax.legend(title='Milk Types', fontsize=10, loc='lower right')

# Annotate consumption values on each bar
def add_values(bars):
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 0.1, bar.get_y() + bar.get_height()/2, f'{width:.1f}', va='center', fontsize=9)

add_values(bars1)
add_values(bars2)
add_values(bars3)
add_values(bars4)
add_values(bars5)

# Adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()