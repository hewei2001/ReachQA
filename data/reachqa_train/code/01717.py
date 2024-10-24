import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2000, 2021)

# Define the proliferation of different digital devices in millions
pcs = [50, 52, 55, 58, 62, 66, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140]
tvs = [70, 73, 75, 78, 81, 84, 88, 92, 96, 100, 104, 108, 112, 116, 120, 125, 130, 135, 140, 145, 150]
smartphones = [5, 10, 20, 35, 50, 70, 95, 120, 150, 180, 215, 255, 300, 350, 410, 480, 560, 650, 750, 860, 980]
tablets = [0, 0, 0, 0, 0, 5, 10, 20, 35, 50, 70, 90, 115, 140, 170, 200, 235, 270, 310, 350, 390]
smart_home_devices = [0, 0, 0, 0, 0, 2, 5, 8, 15, 25, 40, 60, 85, 115, 150, 190, 235, 285, 340, 400, 470]

# Plotting the stacked area chart
plt.figure(figsize=(14, 8))

# Create stacked area plot
plt.stackplot(years, pcs, tvs, smartphones, tablets, smart_home_devices, 
              labels=['Personal Computers', 'Televisions', 'Smartphones', 'Tablets', 'Smart Home Devices'],
              colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], alpha=0.8)

# Add title and labels
plt.title("Digital Device Proliferation in Households\nTwo-Decade Overview (2000 - 2020)", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Devices in Households (Millions)", fontsize=12)

# Add legend
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0., title='Device Types')

# Add grid for better readability
plt.grid(linestyle='--', alpha=0.7)

# Highlight a significant trend change
plt.annotate('Smartphones become ubiquitous', xy=(2010, 250), xytext=(2005, 700),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, backgroundcolor='w')

# Ensure layout is neat without overlapping
plt.tight_layout()

# Display the plot
plt.show()