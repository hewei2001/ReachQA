import matplotlib.pyplot as plt
import numpy as np

# Data: Internet Penetration Rates (% of population) in various countries
countries = ['Norway', 'South Korea', 'United States', 'Germany', 'United Kingdom', 
             'Brazil', 'India', 'Nigeria', 'Indonesia', 'Kenya']
penetration_rates = [98, 96, 88, 84, 92, 73, 45, 39, 61, 52]

# Colors for each country
colors = ['#3366CC', '#DC3912', '#FF9900', '#109618', '#990099', 
          '#0099C6', '#DD4477', '#66AA00', '#B82E2E', '#316395']

# Create the horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.barh(countries, penetration_rates, color=colors, edgecolor='black', height=0.6)

# Set chart title and axis labels
ax.set_title('Internet Penetration Rates by Country\n(2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Internet Penetration Rate (% of population)', fontsize=12)
ax.set_xlim(0, 100)
ax.invert_yaxis()  # Highest penetration at the top
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Adding data labels on each bar
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 1
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width}%', va='center', fontsize=10)

# Highlight countries with less than 50% penetration using a distinct color and label
for i, rate in enumerate(penetration_rates):
    if rate < 50:
        bars[i].set_color('#FF4500')
        ax.text(rate + 1, i, '<50%', color='white', va='center', fontsize=10, fontweight='bold', ha='right')

# Highlighting the country with the highest penetration rate
ax.annotate('Leading Internet Penetration', xy=(98, 0), xytext=(70, 2),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Ensure layout is adjusted to avoid overlaps
plt.tight_layout()

# Display the plot
plt.show()