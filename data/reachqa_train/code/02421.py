import matplotlib.pyplot as plt
import numpy as np

# Define the countries and energy types
countries = ['USA', 'Germany', 'China', 'Brazil', 'India']
energy_types = ['Solar', 'Wind', 'Hydroelectric']

# Define the adoption rates for each country and energy type
adoption_rates = [
    [25, 30, 20],  # USA: Solar, Wind, Hydroelectric
    [40, 35, 15],  # Germany: Solar, Wind, Hydroelectric
    [30, 20, 50],  # China: Solar, Wind, Hydroelectric
    [20, 25, 55],  # Brazil: Solar, Wind, Hydroelectric
    [35, 30, 20]   # India: Solar, Wind, Hydroelectric
]

# Colors for each energy type
colors = ['#FFA07A', '#20B2AA', '#4682B4']

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Define positions for the bars
x_positions = np.arange(len(countries))
bar_width = 0.2

# Plot each energy type with bars and add data annotations
for i, (energy_type, color) in enumerate(zip(energy_types, colors)):
    bar_positions = x_positions + i * bar_width
    ax.bar(bar_positions, [rate[i] for rate in adoption_rates], bar_width, label=energy_type, color=color)

    # Annotate data values on top of the bars
    for j in range(len(countries)):
        ax.text(bar_positions[j], adoption_rates[j][i] + 1, f"{adoption_rates[j][i]}%", ha='center', va='bottom', fontsize=9)

# Customize the plot
ax.set_xlabel('Country', fontsize=12)
ax.set_ylabel('Adoption Rate (%)', fontsize=12)
ax.set_title('Global Adoption of Sustainable Energy\nA Comparative Analysis of 2025', fontsize=14, fontweight='bold', pad=15)
ax.set_xticks(x_positions + bar_width)
ax.set_xticklabels(countries, rotation=45, ha='right')
ax.legend(title='Energy Type')

# Enhance layout for clarity and avoid overlap
plt.tight_layout()

# Display the plot
plt.show()