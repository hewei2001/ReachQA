import matplotlib.pyplot as plt
import numpy as np

# Years of interest
years = np.arange(2012, 2023)

# Mode of transport percentages over the years
public_transport = np.array([30, 32, 34, 35, 36, 38, 40, 42, 45, 48, 50])
cycling = np.array([5, 6, 7, 9, 11, 13, 15, 17, 20, 22, 25])
walking = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
electric_vehicles = np.array([2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 20])
conventional_vehicles = np.array([53, 48, 43, 38, 33, 26, 19, 12, 2, 1, 0])

# Compute the total sustainable transport usage (Cycling + Walking + Electric Vehicles)
sustainable_transport = cycling + walking + electric_vehicles

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 9))

# Stack the bar chart
bars1 = ax.bar(years, public_transport, label='Public Transport', color='#4d88ff')
bars2 = ax.bar(years, cycling, bottom=public_transport, label='Cycling', color='#ff9933')
bars3 = ax.bar(years, walking, bottom=public_transport + cycling, label='Walking', color='#66c266')
bars4 = ax.bar(years, electric_vehicles, bottom=public_transport + cycling + walking,
               label='Electric Vehicles', color='#cc66ff')
bars5 = ax.bar(years, conventional_vehicles, bottom=public_transport + cycling + walking + electric_vehicles,
               label='Conventional Vehicles', color='#ff6666')

# Overlay a line plot for sustainable transport
ax.plot(years, sustainable_transport, label='Total Sustainable Transport', color='gold', linewidth=2.5, marker='o', markersize=8)

# Title and labels
ax.set_title("Shift in Urban Transport Modes Towards Sustainability\nUrban City X (2012-2022)",
             fontsize=16, fontweight='bold', loc='left')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Percentage of Usage (%)", fontsize=12)
ax.set_xticks(years)
ax.set_yticks(range(0, 101, 10))
ax.set_ylim(0, 100)

# Annotate each segment of the bars with percentage values
def annotate_bars(bars):
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.annotate(f'{height}%', 
                        xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                        xytext=(0, 0), 
                        textcoords='offset points',
                        ha='center', va='center',
                        fontsize=9, color='black', weight='bold')

annotate_bars(bars1)
annotate_bars(bars2)
annotate_bars(bars3)
annotate_bars(bars4)
annotate_bars(bars5)

# Annotate the sustainable transport line plot
for (x, y) in zip(years, sustainable_transport):
    ax.annotate(f'{y}%', xy=(x, y), xytext=(-10, 10), textcoords='offset points',
                fontsize=10, color='darkgoldenrod', weight='bold',
                arrowprops=dict(arrowstyle="->", color='darkgoldenrod', lw=1))

# Legend
ax.legend(title="Transport Mode", loc='upper right', bbox_to_anchor=(1.2, 1))

# Remove y-axis grid lines for clarity
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()