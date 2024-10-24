import matplotlib.pyplot as plt
import numpy as np

# Define the data
languages = ["QuantumScript", "BioCode", "NeuroByte", "AI-DSL", "NanoLang"]
adoption_rates = [34, 29, 22, 15, 8]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the bar chart
bars = ax.bar(languages, adoption_rates, 
              color=['#2E8B57', '#4682B4', '#D2691E', '#FF8C00', '#9400D3'], 
              alpha=0.8, width=0.5)

# Set title and labels
ax.set_title("Rise of Future Programming Languages:\nAdoption Trends in 2050", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Programming Languages", fontsize=12)
ax.set_ylabel("Adoption Rate (%)", fontsize=12)

# Annotate bars with data values
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%', 
                xy=(bar.get_x() + bar.get_width() / 2, height), 
                xytext=(0, 3),  # Offset text above the bar
                textcoords="offset points", 
                ha='center', va='bottom', 
                fontsize=10, fontweight='bold', color='black')

# Add gridlines to improve readability
ax.yaxis.grid(True, linestyle='--', which='both', linewidth=0.7, alpha=0.7)

# Adjust the x-axis labels for better visibility
plt.xticks(rotation=45, ha='right', fontsize=10)

# Set limits for the y-axis
ax.set_ylim(0, 40)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()