import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2026)

# Synthetic data for EV adoption in different regions (cumulative percentage)
region_a = [2, 3, 5, 8, 12, 18, 25, 35, 45, 60, 70, 80, 88, 92, 95, 97]
region_b = [1, 2, 3, 5, 10, 16, 24, 33, 44, 57, 68, 75, 82, 88, 90, 93]
region_c = [0, 1, 2, 4, 6, 10, 14, 20, 28, 37, 48, 58, 70, 80, 87, 90]
region_d = [3, 5, 7, 9, 15, 22, 30, 40, 50, 62, 72, 82, 90, 94, 96, 98]
region_e = [1, 2, 4, 6, 9, 12, 18, 27, 39, 50, 64, 76, 84, 89, 92, 95]

# Compute annual growth rates for Region A (as an example for the line plot)
growth_rate_a = [region_a[i] - region_a[i - 1] for i in range(1, len(region_a))]

# Create a figure with two subplots side by side
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Plot the stacked area chart
axs[0].fill_between(years, 0, region_a, label='Region A', color='#ff9999', alpha=0.6)
axs[0].fill_between(years, region_a, np.array(region_a) + np.array(region_b), label='Region B', color='#66b3ff', alpha=0.6)
axs[0].fill_between(years, np.array(region_a) + np.array(region_b), np.array(region_a) + np.array(region_b) + np.array(region_c), 
                    label='Region C', color='#99ff99', alpha=0.6)
axs[0].fill_between(years, np.array(region_a) + np.array(region_b) + np.array(region_c), 
                    np.array(region_a) + np.array(region_b) + np.array(region_c) + np.array(region_d), 
                    label='Region D', color='#ffcc99', alpha=0.6)
axs[0].fill_between(years, np.array(region_a) + np.array(region_b) + np.array(region_c) + np.array(region_d), 
                    np.array(region_a) + np.array(region_b) + np.array(region_c) + np.array(region_d) + np.array(region_e), 
                    label='Region E', color='#c2c2f0', alpha=0.6)
axs[0].set_title("Cumulative Electric Vehicle Adoption\nAcross Various Regions (2010-2025)", fontsize=14, fontweight='bold')
axs[0].set_xlabel("Year", fontsize=12)
axs[0].set_ylabel("Cumulative % of Electric Vehicles", fontsize=12)
axs[0].legend(title="Regions", loc='upper left', fontsize=10)
axs[0].grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
axs[0].set_xticks(years)
axs[0].tick_params(axis='x', rotation=45)

# Plot the line chart for annual growth rates
axs[1].plot(years[1:], growth_rate_a, marker='o', color='navy', linestyle='-', linewidth=2, label='Region A Growth Rate')
axs[1].set_title("Annual Growth Rate of EV Adoption\nfor Region A (2010-2025)", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Year", fontsize=12)
axs[1].set_ylabel("Annual Growth Rate (%)", fontsize=12)
axs[1].legend(loc='upper right', fontsize=10)
axs[1].grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
axs[1].set_xticks(years)
axs[1].tick_params(axis='x', rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()