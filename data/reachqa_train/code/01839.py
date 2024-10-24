import matplotlib.pyplot as plt
import numpy as np

# Data for the chart: Global Usage of Programming Languages from 2020 to 2023
languages = ['Python', 'JavaScript', 'Java', 'C#', 'Ruby', 'Go', 'Swift', 'PHP', 'C++', 'Others']
usage_percentages_2023 = [28, 23, 16, 12, 8, 5, 4, 3, 3, 8]
usage_percentages_2022 = [26, 22, 15, 11, 8, 5, 5, 4, 3, 6]
usage_percentages_2021 = [24, 21, 14, 10, 7, 4, 4, 5, 4, 7]
usage_percentages_2020 = [20, 19, 13, 9, 6, 4, 3, 6, 5, 10]

# Growth Rate Data (2020 to 2023)
growth_rate = [40, 21, 23, 33, 33, 25, 33, -50, -40, -20]

# Create figure with subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

# Bar positions
x_pos = np.arange(len(languages))

# Create the bar chart for usage percentage
bars_2023 = ax1.bar(x_pos - 0.3, usage_percentages_2023, width=0.2, label='2023')
bars_2022 = ax1.bar(x_pos - 0.1, usage_percentages_2022, width=0.2, label='2022')
bars_2021 = ax1.bar(x_pos + 0.1, usage_percentages_2021, width=0.2, label='2021')
bars_2020 = ax1.bar(x_pos + 0.3, usage_percentages_2020, width=0.2, label='2020')

# Customize the first plot
ax1.set_title("Global Usage of Programming Languages (2020-2023)\nwith Growth Rate Analysis", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Programming Languages", fontsize=12)
ax1.set_ylabel("Usage Percentage (%)", fontsize=12)
ax1.set_ylim(0, 35)
ax1.set_xticks(x_pos)
ax1.set_xticklabels(languages, rotation=45, ha='right', fontsize=10)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.legend()

# Annotate percentage values on the bars of 2023 for clarity
for bar in bars_2023:
    height = bar.get_height()
    ax1.annotate(f'{height}%', 
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=9, color='black')

# Secondary plot for growth rate
ax2.plot(languages, growth_rate, color='tab:red', marker='o', linewidth=2, label='Growth Rate (2020-2023)')

# Customize the second plot
ax2.set_title("Growth Rate of Programming Languages (2020-2023)", fontsize=14, fontweight='bold', pad=20)
ax2.set_ylabel("Growth Rate (%)", fontsize=12)
ax2.set_ylim(-60, 50)
ax2.set_xticks(x_pos)
ax2.set_xticklabels(languages, rotation=45, ha='right', fontsize=10)
ax2.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)
ax2.legend()

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Show the plot
plt.show()