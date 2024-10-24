import matplotlib.pyplot as plt
import numpy as np

# Define the data
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
e_reader_adoption = np.array([10, 15, 22, 28, 35, 40, 46, 50, 55, 58, 62])
digital_subscription_adoption = np.array([5, 8, 12, 18, 25, 30, 35, 42, 50, 56, 60])
audiobook_adoption = np.array([2, 3, 4, 5, 6, 10, 12, 15, 20, 24, 30])

# Error margins for the adoption rates
e_reader_error = np.array([1, 2, 3, 3, 4, 3, 3, 2, 2, 2, 3])
digital_subscription_error = np.array([2, 2, 2, 3, 3, 3, 4, 3, 3, 3, 4])

# Create the figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 7))

# First subplot: Line plot with error bars
axs[0].errorbar(
    years, e_reader_adoption, yerr=e_reader_error, label='E-Reader Adoption',
    fmt='-o', color='blue', linestyle='-', linewidth=2, marker='s', markersize=6, capsize=5, alpha=0.8
)
axs[0].errorbar(
    years, digital_subscription_adoption, yerr=digital_subscription_error, label='Digital Subscription',
    fmt='-o', color='green', linestyle='--', linewidth=2, marker='^', markersize=6, capsize=5, alpha=0.8
)

# Add title, labels, and grid to the first subplot
axs[0].set_title("Adoption Rates of Digital Reading Platforms\n(2010-2020)", fontsize=14, fontweight='bold', color='darkred')
axs[0].set_xlabel("Year", fontsize=12)
axs[0].set_ylabel("Adoption Rate (%)", fontsize=12)
axs[0].set_xlim(2009, 2021)
axs[0].set_ylim(0, 70)
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].legend(loc="upper left", frameon=False, fontsize=11)

# Second subplot: Stacked bar chart
axs[1].bar(years, e_reader_adoption, color='blue', label='E-Reader', alpha=0.7)
axs[1].bar(years, digital_subscription_adoption, bottom=e_reader_adoption, color='green', label='Digital Subscription', alpha=0.7)
axs[1].bar(years, audiobook_adoption, bottom=e_reader_adoption+digital_subscription_adoption, color='orange', label='Audiobook', alpha=0.7)

# Add title, labels, and grid to the second subplot
axs[1].set_title("Cumulative Adoption of Digital Platforms\n(2010-2020)", fontsize=14, fontweight='bold', color='darkred')
axs[1].set_xlabel("Year", fontsize=12)
axs[1].set_ylabel("Cumulative Adoption Rate (%)", fontsize=12)
axs[1].set_xlim(2009, 2021)
axs[1].set_ylim(0, 150)
axs[1].grid(True, linestyle='--', alpha=0.6)
axs[1].legend(loc="upper left", frameon=False, fontsize=11)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()