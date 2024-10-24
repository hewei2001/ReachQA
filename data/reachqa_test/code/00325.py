import matplotlib.pyplot as plt
import numpy as np

# Define the years for the study (more granular and extensive range)
years = [str(year) for year in range(1990, 2060, 10)]

# Percentage data for each type of vehicle energy source
gasoline_percentages = [90, 85, 75, 55, 40, 20, 10]  # Gradual decline of gasoline vehicles
electric_percentages = [5, 10, 15, 35, 50, 60, 65]   # Rapid adoption of electric vehicles
hydrogen_percentages = [5, 5, 10, 10, 10, 10, 15]    # Slow, steady adoption of hydrogen
hybrid_percentages = [0, 0, 0, 0, 0, 10, 10]          # Introduction and growth of hybrid vehicles

# Assert that the percentages sum to 100 for each year
assert all(g + e + h + hy == 100 for g, e, h, hy in zip(gasoline_percentages, electric_percentages, hydrogen_percentages, hybrid_percentages)), "Percentages must sum to 100."

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 9))

# Create the stacked bar chart
p1 = ax.bar(years, gasoline_percentages, label='Gasoline', color='lightcoral', width=0.6)
p2 = ax.bar(years, electric_percentages, bottom=gasoline_percentages, label='Electric', color='lightgreen', width=0.6)
p3 = ax.bar(years, hydrogen_percentages, bottom=np.array(gasoline_percentages) + np.array(electric_percentages), label='Hydrogen', color='lightblue', width=0.6)
p4 = ax.bar(years, hybrid_percentages, bottom=np.array(gasoline_percentages) + np.array(electric_percentages) + np.array(hydrogen_percentages), label='Hybrid', color='gold', width=0.6)

# Annotate each segment with percentage values for clarity
for bars in (p1, p2, p3, p4):
    for bar in bars:
        height = bar.get_height()
        if height > 3:  # Avoid clutter by not annotating very small sections
            ax.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                        xytext=(0, 0), textcoords='offset points', ha='center', va='center', fontsize=10, color='black')

# Customize the plot details
ax.set_title("Transformation of Vehicle Energy Sources in Transitaria\n1990-2050: Transitioning to Sustainable Mobility", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Percentage of Total Vehicles (%)", fontsize=12)
ax.set_ylim(0, 100)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Configure x-ticks and labels
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, rotation=45, ha='right')

# Add a legend and make layout adjustments
ax.legend(title='Energy Type', fontsize=10, title_fontsize=11, loc='upper right')

# Tighten layout to prevent overlap
plt.tight_layout()

# Display the completed chart
plt.show()