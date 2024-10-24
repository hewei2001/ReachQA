import matplotlib.pyplot as plt
import numpy as np

# Define departments and their corresponding participation rates
departments = ['Human Resources', 'Sales', 'Engineering', 'Marketing', 'Administration']
participation_rates = [75, 60, 55, 40, 65]

# Related but distinct data: Historical participation rates (as an example)
years = ['2018', '2019', '2020', '2021', '2022']
historical_rates = {
    'Human Resources': [70, 72, 74, 75, 77],
    'Sales': [50, 55, 58, 60, 62],
    'Engineering': [60, 62, 64, 55, 57],
    'Marketing': [35, 37, 39, 40, 42],
    'Administration': [63, 65, 67, 65, 68],
}

# Set up the subplot grid
fig, axs = plt.subplots(1, 2, figsize=(15, 7))

# Plot the bar chart
positions = np.arange(len(departments))
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#92A8D1', '#F7CAC9']
bars = axs[0].bar(positions, participation_rates, color=colors, edgecolor='black', width=0.6)

# Add annotations for bar chart
for bar in bars:
    yval = bar.get_height()
    axs[0].text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval}%', ha='center', va='bottom', fontsize=11, fontweight='bold', color='darkblue')

# Set titles and labels for the bar chart
axs[0].set_title('Participation Rates by Department', fontsize=14, fontweight='bold', pad=10)
axs[0].set_xlabel('Department', fontsize=12)
axs[0].set_ylabel('Participation Rate (%)', fontsize=12)
axs[0].set_xticks(positions)
axs[0].set_xticklabels(departments, rotation=45, ha='right', fontsize=11)
axs[0].grid(axis='y', linestyle='--', alpha=0.7)
axs[0].set_ylim(0, 100)

# Plot the line chart for historical rates
for dept, rates in historical_rates.items():
    axs[1].plot(years, rates, marker='o', label=dept)

# Set titles and labels for the line chart
axs[1].set_title('Historical Participation Rates (2018-2022)', fontsize=14, fontweight='bold', pad=10)
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Participation Rate (%)', fontsize=12)
axs[1].set_ylim(0, 100)
axs[1].legend(title='Departments', fontsize=10, title_fontsize='11')
axs[1].grid(axis='y', linestyle='--', alpha=0.7)

# Ensure layout is tight to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()