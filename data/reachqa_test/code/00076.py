import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2023
years = np.arange(2000, 2024)

# Hypothetical AI Intelligence Index values
ai_index = [
    10, 15, 20, 25, 32, 38, 45, 53, 62, 70,
    80, 92, 105, 119, 134, 150, 167, 185,
    204, 224, 245, 267, 290, 314
]

# Error margins (± in index points)
index_errors = [
    2, 3, 3, 4, 4, 5, 5, 6, 7, 7,
    8, 9, 10, 10, 11, 11, 12, 13,
    13, 14, 15, 16, 17, 18
]

# Calculate annual growth rate in percentage
ai_growth_rate = [0]  # No growth for the first year as it's the base
for i in range(1, len(ai_index)):
    growth = ((ai_index[i] - ai_index[i-1]) / ai_index[i-1]) * 100
    ai_growth_rate.append(growth)

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# First subplot: AI Intelligence Index with error bars
axs[0].errorbar(years, ai_index, yerr=index_errors, fmt='-o', capsize=5, color='tab:blue', 
                label='AI Intelligence Index', alpha=0.8, ecolor='lightgray', elinewidth=2)
axs[0].set_title("Evolution of AI Capabilities (2000-2023)\nTracking Growth in AI Intelligence Index", 
                 fontsize=14, fontweight='bold')
axs[0].set_xlabel("Year", fontsize=12)
axs[0].set_ylabel("AI Intelligence Index", fontsize=12)
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].legend(loc='upper left', fontsize=10)
axs[0].annotate('AI Surpasses Human-Level in Specific Tasks', 
                xy=(2020, ai_index[20]), xytext=(2005, ai_index[20] + 40),
                arrowprops=dict(facecolor='grey', arrowstyle='->'), fontsize=10, color='black')

# Second subplot: Annual growth rate in AI Intelligence Index
axs[1].bar(years, ai_growth_rate, color='tab:orange', alpha=0.7)
axs[1].set_title("Year-over-Year Growth Rate of AI Intelligence Index\n(2000-2023)", 
                 fontsize=14, fontweight='bold')
axs[1].set_xlabel("Year", fontsize=12)
axs[1].set_ylabel("Growth Rate (%)", fontsize=12)
axs[1].grid(True, linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap and ensure readability
plt.tight_layout()

# Display the plot
plt.show()