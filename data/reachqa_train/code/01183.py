import matplotlib.pyplot as plt
import numpy as np

# Define the data
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
e_reader_adoption = np.array([10, 15, 22, 28, 35, 40, 46, 50, 55, 58, 62])
digital_subscription_adoption = np.array([5, 8, 12, 18, 25, 30, 35, 42, 50, 56, 60])

# Error margins for the adoption rates
e_reader_error = np.array([1, 2, 3, 3, 4, 3, 3, 2, 2, 2, 3])
digital_subscription_error = np.array([2, 2, 2, 3, 3, 3, 4, 3, 3, 3, 4])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot E-Reader Adoption Rate with error bars
ax.errorbar(
    years, e_reader_adoption, yerr=e_reader_error, label='E-Reader Adoption Rate',
    fmt='-o', color='blue', linestyle='-', linewidth=2, marker='s', markersize=6, capsize=5, alpha=0.8
)

# Plot Digital Subscription Adoption Rate with error bars
ax.errorbar(
    years, digital_subscription_adoption, yerr=digital_subscription_error, label='Digital Subscription Adoption Rate',
    fmt='-o', color='green', linestyle='--', linewidth=2, marker='^', markersize=6, capsize=5, alpha=0.8
)

# Titles and labels
ax.set_title("Exploring the Popularity of Digital Reading Platforms:\nA Decade of Transition (2010-2020)", fontsize=16, fontweight='bold', color='darkred')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Adoption Rate (%)", fontsize=12)
ax.set_xlim(2009, 2021)
ax.set_ylim(0, 70)
ax.grid(True, linestyle='--', alpha=0.6)

# Legend
ax.legend(loc="upper left", frameon=False, fontsize=11)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()