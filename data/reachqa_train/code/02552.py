import numpy as np
import matplotlib.pyplot as plt

# Define the years
years = np.arange(2010, 2021)

# Coffee consumption data (average cups per day)
teenagers_consumption = np.array([0.5, 0.6, 0.7, 0.8, 0.8, 0.9, 1.0, 1.0, 1.1, 1.2, 1.3])
adults_consumption = np.array([2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5])
seniors_consumption = np.array([1.0, 1.0, 1.1, 1.1, 1.2, 1.3, 1.2, 1.1, 1.1, 1.1, 1.2])

# Coffee expenditure data (dollars per day)
teenagers_expenditure = np.array([0.5, 0.6, 0.75, 0.8, 0.85, 0.9, 1.0, 1.05, 1.15, 1.3, 1.4])
adults_expenditure = np.array([2.7, 2.8, 2.85, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 3.8])
seniors_expenditure = np.array([0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.3, 1.35])

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting the consumption data
ax1.plot(years, teenagers_consumption, color='blue', marker='o', linestyle='-', linewidth=2, label='Teenagers (13-19)')
ax1.plot(years, adults_consumption, color='green', marker='s', linestyle='-', linewidth=2, label='Adults (20-39)')
ax1.plot(years, seniors_consumption, color='red', marker='^', linestyle='-', linewidth=2, label='Seniors (40+)')

# Adding title and labels for the consumption plot
ax1.set_title('Trends in Coffee Consumption and Expenditure\nAcross Different Age Groups (2010-2020)', fontsize=16, fontweight='bold', color='brown')
ax1.set_xlabel('Year', fontsize=12, color='darkblue')
ax1.set_ylabel('Average Cups of Coffee per Day', fontsize=12, color='darkblue')

# Configure x-ticks
ax1.set_xticks(years)
ax1.tick_params(axis='x', rotation=45)

# Adding a grid for better readability
ax1.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Highlight a specific year (e.g., 2015) and add text annotation
ax1.axvline(x=2015, linestyle='--', color='purple', linewidth=1.5)
ax1.text(2015.5, 3.2, 'Significant\nYear', verticalalignment='center', horizontalalignment='left', color='purple', fontsize=10)

# Annotations for specific years on the teenager's line
for year, cups in zip(years, teenagers_consumption):
    if year in [2010, 2015, 2020]:
        ax1.annotate(f'{cups} cups', xy=(year, cups), textcoords='offset points', xytext=(-30, 10), ha='center', fontsize=9, color='blue')

# Set axis limits for better visualization
ax1.set_xlim(2010, 2020)
ax1.set_ylim(0, 4)

# Add a legend and position it appropriately
ax1.legend(loc='upper left', fontsize=10)

# Creating secondary y-axis for expenditure plot
ax2 = ax1.twinx()
ax2.bar(years - 0.2, teenagers_expenditure, width=0.2, color='lightblue', alpha=0.6, label='Teenagers Expenditure', align='center')
ax2.bar(years, adults_expenditure, width=0.2, color='lightgreen', alpha=0.6, label='Adults Expenditure', align='center')
ax2.bar(years + 0.2, seniors_expenditure, width=0.2, color='lightcoral', alpha=0.6, label='Seniors Expenditure', align='center')

# Adding labels for the expenditure plot
ax2.set_ylabel('Average Expenditure on Coffee ($)', fontsize=12, color='darkblue')

# Add legends for the secondary y-axis
ax2.legend(loc='upper right', fontsize=10)

# Automatically adjust the layout
fig.tight_layout()

# Show the plot
plt.show()