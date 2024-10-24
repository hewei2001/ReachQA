import matplotlib.pyplot as plt
import numpy as np

# Define cities and their average prices per square foot for apartments and houses
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Toronto', 'Vancouver', 'San Francisco', 
          'Boston', 'Seattle', 'Atlanta', 'Dallas', 'Miami', 'Phoenix', 'San Diego']
avg_price_per_sqft_apartments = [675, 550, 325, 200, 475, 525, 700, 650, 600, 300, 275, 450, 250, 400]
avg_price_per_sqft_houses = [800, 650, 400, 300, 575, 600, 850, 750, 650, 350, 325, 550, 275, 500]
std_dev_apartments = [50, 40, 30, 20, 35, 40, 60, 55, 50, 25, 20, 45, 20, 40]
std_dev_houses = [60, 50, 45, 35, 45, 50, 70, 65, 55, 30, 30, 60, 25, 50]

# Set up the grouped bar chart
width = 0.35
bar_positions = np.arange(len(cities))

plt.figure(figsize=(16, 10))
bars1 = plt.bar(bar_positions - width/2, avg_price_per_sqft_apartments, width=width, yerr=std_dev_apartments, 
                color='#377eb8', capsize=5, label='Apartments')
bars2 = plt.bar(bar_positions + width/2, avg_price_per_sqft_houses, width=width, yerr=std_dev_houses, 
                color='#ff7f00', capsize=5, label='Houses')

# Add grid lines along the y-axis
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate each bar with the average price per square foot
for bar_set in [bars1, bars2]:
    for bar in bar_set:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height,
                 f"${height:,.0f}",
                 ha='center', va='bottom', rotation=0, fontsize=10)

# Adjust x-axis labels for clarity
plt.xticks(bar_positions, cities, rotation=45, ha='right', fontsize=12)

# Set the title and axis labels
plt.title("Average Price per Square Foot in Major Cities\nFirst Quarter of 2023",
          fontsize=18, pad=20)

plt.xlabel("City", fontsize=14)
plt.ylabel("Average Price per Square Foot (USD)", fontsize=14)

# Add a legend
plt.legend(fontsize=12)

# Adjust the layout to avoid overlapping
plt.tight_layout()

# Show the bar chart
plt.show()