import matplotlib.pyplot as plt
import numpy as np

# Define the countries and their renewable energy adoption rates
countries = ['USA', 'Germany', 'China', 'India', 'Brazil']
adoption_rates = [17, 45, 23, 15, 66]

# Define colors for each bar to enhance visual distinction
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create a bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Create bars with distinct colors
bars = ax.bar(countries, adoption_rates, color=colors, edgecolor='black', width=0.6)

# Annotate each bar with the corresponding percentage value
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%', 
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Offset the text above the bar
                textcoords="offset points",
                ha='center', va='bottom', fontsize=11, fontweight='bold')

# Set chart title and labels
ax.set_title("Global Renewable Energy Adoption Rates - 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Countries", fontsize=14)
ax.set_ylabel("Percentage of Total Energy from Renewables (%)", fontsize=14)
ax.set_ylim(0, 80)  # Set y-axis limit to give space for annotations

# Add y-axis gridlines for improved readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust layout to prevent label overlap
plt.xticks(rotation=30, ha='right')  # Rotate x-tick labels for better fit
plt.tight_layout()

# Display the chart
plt.show()