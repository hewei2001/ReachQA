import matplotlib.pyplot as plt
import numpy as np

# Years from 2024 to 2034
years = np.arange(2024, 2035)

# Artificial data for vehicle sales (in millions)
ev_sales = np.array([1.2, 1.8, 2.5, 3.3, 4.0, 5.0, 6.2, 7.5, 8.9, 10.4, 12.0])
ice_sales = np.array([25.0, 23.5, 22.1, 20.7, 19.4, 18.2, 17.0, 15.9, 14.9, 14.0, 13.2])
hybrid_sales = np.array([2.0, 2.5, 3.0, 3.5, 4.0, 4.6, 5.3, 6.0, 6.8, 7.7, 8.7])

# Derived metrics: Year-over-Year growth rates
ev_growth_rate = np.diff(ev_sales) / ev_sales[:-1] * 100
ice_growth_rate = np.diff(ice_sales) / ice_sales[:-1] * 100
hybrid_growth_rate = np.diff(hybrid_sales) / hybrid_sales[:-1] * 100

# Create a figure with two subplots
fig, axs = plt.subplots(2, 1, figsize=(14, 12))

# Plotting EV, ICE, and Hybrid sales
axs[0].plot(years, ev_sales, label='Electric Vehicle Sales', marker='o', linestyle='-', color='limegreen', linewidth=2)
axs[0].plot(years, ice_sales, label='Internal Combustion Engine Sales', marker='x', linestyle='-', color='firebrick', linewidth=2)
axs[0].plot(years, hybrid_sales, label='Hybrid Vehicle Sales', marker='s', linestyle='-', color='royalblue', linewidth=2)

# Title, labels, and legend for the first plot
axs[0].set_title("The Decade of Electric Transition:\nVehicle Sales Shift and Growth (2024-2034)", fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel("Year", fontsize=12)
axs[0].set_ylabel("Vehicle Sales (Millions)", fontsize=12)
axs[0].legend(loc='upper left', fontsize=10, title="Vehicle Type", frameon=True)
axs[0].grid(True, which='major', linestyle='--', linewidth=0.5, alpha=0.7)

# Annotations and additional elements
axs[0].annotate('EV Sales Surpass ICE', xy=(2029, 16), xytext=(2026, 20),
                arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
                fontsize=10, fontweight='bold', color='darkgreen')
axs[0].axvline(x=2030, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)
axs[0].text(2030.1, 1, '2030 Milestone', rotation=90, verticalalignment='center', fontsize=10, color='gray')

# Plotting the Year-over-Year growth rates
axs[1].plot(years[1:], ev_growth_rate, label='EV Growth Rate (%)', marker='o', linestyle='-', color='limegreen', linewidth=2)
axs[1].plot(years[1:], ice_growth_rate, label='ICE Growth Rate (%)', marker='x', linestyle='-', color='firebrick', linewidth=2)
axs[1].plot(years[1:], hybrid_growth_rate, label='Hybrid Growth Rate (%)', marker='s', linestyle='-', color='royalblue', linewidth=2)

# Title, labels, and legend for the second plot
axs[1].set_title("Year-over-Year Growth Rate of Vehicle Sales", fontsize=14, fontweight='bold', pad=15)
axs[1].set_xlabel("Year", fontsize=12)
axs[1].set_ylabel("Growth Rate (%)", fontsize=12)
axs[1].legend(loc='upper left', fontsize=10, title="Growth Rate", frameon=True)
axs[1].grid(True, which='major', linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()