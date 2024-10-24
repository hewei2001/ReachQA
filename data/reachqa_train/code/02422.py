import matplotlib.pyplot as plt
import numpy as np

# Define the countries and expanded energy types
countries = ['USA', 'Germany', 'China', 'Brazil', 'India', 'Japan', 'UK', 'France']
energy_types = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass']

# Define the adoption rates for each country and energy type
adoption_rates = [
    [25, 30, 20, 10, 15],  # USA: Solar, Wind, Hydroelectric, Geothermal, Biomass
    [40, 35, 15, 5, 10],   # Germany
    [30, 20, 50, 10, 5],   # China
    [20, 25, 55, 5, 10],   # Brazil
    [35, 30, 20, 5, 10],   # India
    [15, 40, 30, 10, 5],   # Japan
    [25, 20, 35, 15, 5],   # UK
    [30, 15, 40, 10, 5]    # France
]

# Define colors for each energy type
colors = ['#FFA07A', '#20B2AA', '#4682B4', '#8A2BE2', '#D2691E']

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Define positions for the bars
x_positions = np.arange(len(countries))
bar_width = 0.15

# Plot each energy type with stacked bars and data annotations
cumulative_rates = np.zeros(len(countries))
for i, (energy_type, color) in enumerate(zip(energy_types, colors)):
    current_rates = [rate[i] for rate in adoption_rates]
    ax.bar(x_positions, current_rates, bar_width, bottom=cumulative_rates, label=energy_type, color=color)
    cumulative_rates += current_rates

    # Annotate data values on the bars
    for j in range(len(countries)):
        ax.text(x_positions[j], cumulative_rates[j] - current_rates[j] / 2, f"{current_rates[j]}%", ha='center', va='center', fontsize=8, color='white')

# Overlay line graph for average adoption rate per country
average_rates = np.mean(adoption_rates, axis=1)
ax.plot(x_positions, average_rates, color='black', marker='o', linestyle='--', linewidth=1.5, label='Average Rate')

# Customize the plot
ax.set_xlabel('Country', fontsize=12)
ax.set_ylabel('Adoption Rate (%)', fontsize=12)
ax.set_title('Global Adoption of Sustainable Energy\nExpanded Analysis for 2025', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x_positions)
ax.set_xticklabels(countries, rotation=45, ha='right')
ax.legend(title='Energy Type & Average Rate', bbox_to_anchor=(1.05, 1), loc='upper left')

# Enhance layout for clarity and avoid overlap
plt.tight_layout()

# Display the plot
plt.show()