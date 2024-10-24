import matplotlib.pyplot as plt
import numpy as np

# Define the decades and the corresponding adoption numbers (in thousands)
decades = ["2000s", "2010s", "2020s", "2030s", "2040s", "2050s", "2060s"]
adoption_numbers = [5, 20, 45, 120, 180, 300, 500]  # In thousands

# Create a cumulative sum for additional insights
cumulative_adoption = np.cumsum(adoption_numbers)

# Set up the figure and axes for subplots
fig, ax1 = plt.subplots(figsize=(14, 8))

# Create bar chart with color gradient
colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(decades)))
bars = ax1.bar(decades, adoption_numbers, color=colors, edgecolor='black', linewidth=1.2)

# Add annotations to the bar chart
for bar, label in zip(bars, adoption_numbers):
    height = bar.get_height()
    ax1.annotate(f'{label}k',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=10, fontweight='bold')

# Configure grid, labels, and title for the bar chart
ax1.set_title("Futuristic Technology Adoption in Future City 2077\nA Decadal Overview from 2000 to 2060", fontsize=16, weight='bold', pad=20)
ax1.set_xlabel("Decade", fontsize=12)
ax1.set_ylabel("Number of Adopters (Thousands)", fontsize=12)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.set_ylim(0, max(adoption_numbers) + 50)

# Adding a second Y axis for cumulative adoption
ax2 = ax1.twinx()
ax2.plot(decades, cumulative_adoption, color='darkorange', marker='o', linestyle='-', linewidth=2, markersize=8, label='Cumulative Adoption')
ax2.set_ylabel("Cumulative Adopters (Thousands)", fontsize=12)
ax2.set_ylim(0, sum(adoption_numbers))
ax2.legend(loc='upper left')

# Tight layout to adjust layout and prevent overlap
plt.tight_layout()

# Display the plot
plt.show()