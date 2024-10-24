import matplotlib.pyplot as plt
import numpy as np

# Vintage car models and their corresponding restoration costs in USD
car_models = [
    '1965 Ford Mustang',
    '1970 Chevrolet Chevelle',
    '1971 Dodge Charger',
    '1967 Pontiac GTO',
    '1985 Ferrari Testarossa'
]
restoration_costs_2023 = np.array([35000, 45000, 42000, 38000, 75000])

# Historical restoration costs over 5 years (2019-2023) for each model
historical_costs = np.array([
    [32000, 33000, 34000, 34000, 35000],  # 1965 Ford Mustang
    [41000, 42000, 43000, 44000, 45000],  # 1970 Chevrolet Chevelle
    [40000, 41000, 41500, 41800, 42000],  # 1971 Dodge Charger
    [36000, 37000, 37500, 37700, 38000],  # 1967 Pontiac GTO
    [70000, 71000, 72000, 74000, 75000]   # 1985 Ferrari Testarossa
])

# Years for historical data
years = np.arange(2019, 2024)

# Color configuration for the bars
colors = ['#FFD700', '#C0C0C0', '#CD7F32', '#4682B4', '#FF6347']

# Create positions for each bar along the x-axis
x_positions = np.arange(len(car_models))

# Initialize the figure with 1 row and 2 columns of subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Create the bar chart in the first subplot
bars = axes[0].bar(x_positions, restoration_costs_2023, color=colors, alpha=0.8)
axes[0].set_title('Vintage Car Restoration Costs in 2023', fontsize=14, pad=20)
axes[0].set_xlabel('Vintage Car Models', fontsize=12)
axes[0].set_ylabel('Average Restoration Cost ($USD)', fontsize=12)
axes[0].set_xticks(x_positions)
axes[0].set_xticklabels(car_models, rotation=30, ha='right')
axes[0].yaxis.grid(True, linestyle='--', alpha=0.5)

# Annotate each bar with its height (the cost)
for bar in bars:
    yval = bar.get_height()
    axes[0].text(bar.get_x() + bar.get_width() / 2.0, yval, f'${yval:,}', 
                 va='bottom', ha='center', fontsize=10, fontweight='bold', color='darkgreen')

# Create the line plot in the second subplot
for i, model_costs in enumerate(historical_costs):
    axes[1].plot(years, model_costs, marker='o', label=car_models[i], linewidth=2)

axes[1].set_title('5-Year Restoration Cost Trend', fontsize=14, pad=20)
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Restoration Cost ($USD)', fontsize=12)
axes[1].legend(loc='upper left', fontsize=9)
axes[1].grid(True, linestyle='--', alpha=0.5)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()