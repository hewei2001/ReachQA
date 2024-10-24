import matplotlib.pyplot as plt
import numpy as np

# Simulated brightness data for Nova Stellaris over 12 months
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
brightness = np.array([5.1, 5.6, 6.0, 5.8, 5.3, 5.2, 5.7, 6.2, 5.9, 5.4, 5.1, 5.3])

# Creating the line chart
plt.figure(figsize=(10, 6))
plt.plot(months, brightness, marker='o', linestyle='-', color='#FF6347', linewidth=2, markersize=8, label='Brightness Level')

# Titles and labels
plt.title('Yearly Brightness Variability\nof Nova Stellaris', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Brightness (arbitrary units)', fontsize=12)
plt.xticks(months, rotation=45)
plt.yticks(np.arange(5.0, 6.5, 0.5))

# Adding a grid
plt.grid(True, color='grey', linestyle='--', linewidth=0.5, alpha=0.7)

# Annotating the data points
for month, bright in zip(months, brightness):
    plt.text(month, bright + 0.05, f'{bright:.1f}', ha='center', va='bottom', fontsize=9)

# Adding a legend
plt.legend(loc='upper right')

# Automatically adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.show()