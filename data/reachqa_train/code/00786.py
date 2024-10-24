import matplotlib.pyplot as plt
import numpy as np

# Data: Number of employees and their coffee preferences at InnovateTech
coffee_types = ['Espresso', 'Americano', 'Cappuccino', 'Latte', 'Macchiato', 'Mocha']
preferences = [50, 30, 40, 60, 25, 45]

# Create the bar plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(coffee_types, preferences, 
       color=['#6f4e37', '#d2691e', '#8b4513', '#deb887', '#cd853f', '#a0522d'], 
       edgecolor='black', alpha=0.8)

# Customizing the plot
ax.set_title("Coffee Consumption Preferences at InnovateTech", fontsize=16, fontweight='bold')
ax.set_xlabel("Type of Coffee", fontsize=12)
ax.set_ylabel("Number of Employees", fontsize=12)
ax.set_xticklabels(coffee_types, rotation=45, ha='right')

# Add grid lines for readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add data labels above the bars
for i, v in enumerate(preferences):
    ax.text(i, v + 1, str(v), ha='center', va='bottom', fontweight='bold', fontsize=10)

# Automatically adjust subplot parameters to give the plot a cleaner look
plt.tight_layout()

# Show the plot
plt.show()