import matplotlib.pyplot as plt
import numpy as np

# Years of interest
years = np.arange(2012, 2023)

# Mode of transport percentages over the years (adjusted to ensure all sums equal 100)
public_transport = [30, 32, 34, 35, 36, 38, 40, 42, 45, 48, 50]
cycling = [5, 6, 7, 9, 11, 13, 15, 17, 20, 22, 25]
walking = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
electric_vehicles = [2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 20]
conventional_vehicles = [53, 48, 43, 38, 33, 26, 19, 12, 2, 1, 0]

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Stack the bar chart
bars1 = ax.bar(years, public_transport, label='Public Transport', color='skyblue')
bars2 = ax.bar(years, cycling, bottom=public_transport, label='Cycling', color='orange')
bars3 = ax.bar(years, walking, bottom=np.add(public_transport, cycling), label='Walking', color='lightgreen')
bars4 = ax.bar(years, electric_vehicles, bottom=np.add(np.add(public_transport, cycling), walking),
               label='Electric Vehicles', color='purple')
bars5 = ax.bar(years, conventional_vehicles, bottom=np.add(np.add(np.add(public_transport, cycling), walking),
                                                          electric_vehicles),
               label='Conventional Vehicles', color='red')

# Title and labels
ax.set_title("Sustainable Modes of Transport: A Shift Towards Green Travel\nUrban City X (2012-2022)",
             fontsize=16, fontweight='bold')
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

# Legend
ax.legend(title="Transport Mode", loc='upper left')

# Remove y-axis grid lines for clarity
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()