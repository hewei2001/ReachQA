import matplotlib.pyplot as plt
import numpy as np

# Define the data
languages = ["QuantumScript", "BioCode", "NeuroByte", "AI-DSL", "NanoLang"]
adoption_rates = [34, 29, 22, 15, 8]
projected_growth = [5, 7, 12, 10, 15]  # Projected growth rates from 2050 to 2060

# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the bar chart for adoption rates
bars = ax1.bar(languages, adoption_rates, 
               color=['#2E8B57', '#4682B4', '#D2691E', '#FF8C00', '#9400D3'], 
               alpha=0.8, width=0.5, label='Adoption Rate (%)')

# Set title and labels for the primary axis
ax1.set_title("Future Programming Languages in 2050:\nAdoption vs. Projected Growth Rate", 
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Programming Languages", fontsize=12)
ax1.set_ylabel("Adoption Rate (%)", fontsize=12, color='black')
ax1.tick_params(axis='y', labelcolor='black')

# Annotate bars with adoption rates
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}%', 
                 xy=(bar.get_x() + bar.get_width() / 2, height), 
                 xytext=(0, 3),  # Offset text above the bar
                 textcoords="offset points", 
                 ha='center', va='bottom', 
                 fontsize=10, fontweight='bold', color='black')

# Create a secondary axis for projected growth rates
ax2 = ax1.twinx()
ax2.plot(languages, projected_growth, color='red', marker='o', linestyle='--', linewidth=2, label='Projected Growth (%)')
ax2.set_ylabel("Projected Growth Rate (%)", fontsize=12, color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Annotate line plot with growth rates
for i, txt in enumerate(projected_growth):
    ax2.annotate(f'{txt}%', 
                 (languages[i], projected_growth[i]), 
                 textcoords="offset points", xytext=(0, 10), 
                 ha='center', fontsize=10, color='red', fontweight='bold')

# Add gridlines to improve readability
ax1.yaxis.grid(True, linestyle='--', which='both', linewidth=0.7, alpha=0.7)

# Adjust the x-axis labels for better visibility
plt.xticks(rotation=45, ha='right', fontsize=10)

# Set limits for the y-axes
ax1.set_ylim(0, 40)
ax2.set_ylim(0, 20)

# Add legend
fig.legend(loc='upper right', bbox_to_anchor=(1, 1), bbox_transform=ax1.transAxes)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()