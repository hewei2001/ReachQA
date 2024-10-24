import matplotlib.pyplot as plt
import numpy as np

# Define the browsers and age groups
browsers = ["Chrome", "Firefox", "Edge"]
age_groups = ["Teens (13-19)", "Adults (20-39)", "Seniors (40+)"]

# Fictional data representing browser usage percentage by age group
usage_data = np.array([
    [60, 25, 15],  # Teens
    [50, 30, 20],  # Adults
    [45, 35, 20]   # Seniors
])

# Colors for each browser
browser_colors = ['#FF5733', '#4285F4', '#34A853']

# Initialize the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Cumulative sum for stacking bars
cumulative_usage = np.zeros(len(age_groups))

# Plot each browser's usage percentage
for idx, browser in enumerate(browsers):
    bars = ax.bar(age_groups, usage_data[:, idx], bottom=cumulative_usage, 
                  label=browser, color=browser_colors[idx])
    
    # Add data labels
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}%', 
                    xy=(bar.get_x() + bar.get_width() / 2, height + bar.get_y()),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10)
    
    cumulative_usage += usage_data[:, idx]

# Add labels and title
ax.set_ylabel('Usage Percentage (%)', fontsize=12)
ax.set_title('Web Browsing Habits in 2023:\nThe Battle of Browsers', fontsize=16, weight='bold', pad=20)

# Fixed range for x-axis to ensure consistency
ax.set_ylim(0, 100)

# Add a legend
ax.legend(title='Browsers', fontsize=10)

# Customize the grid and make x-axis labels readable
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.xaxis.grid(False)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()