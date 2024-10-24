import matplotlib.pyplot as plt
import numpy as np

# Extended data samples for multiple departments over two months
departments = [
    'Development', 'Marketing', 'Sales', 'Customer Support',
    'HR', 'Finance', 'Operations', 'IT'
]

# Simulated weekly working hours for two months for each department
jan_hours = [
    [38, 40, 42, 45, 50, 48, 60, 55, 58, 40, 43, 47, 49, 45, 44, 46],
    [35, 36, 40, 38, 42, 39, 34, 37, 33, 31, 40, 38, 36, 35, 37, 39],
    [30, 32, 35, 40, 38, 45, 50, 60, 55, 41, 42, 44, 46, 35, 37, 31],
    [25, 30, 35, 40, 45, 50, 55, 60, 32, 34, 36, 38, 33, 31, 29, 28],
    [20, 25, 28, 30, 32, 30, 33, 35, 40, 30, 29, 31, 30, 30, 28, 25],
    [15, 20, 25, 28, 30, 32, 35, 37, 33, 31, 28, 26, 25, 22, 24, 27],
    [25, 30, 35, 38, 40, 45, 48, 50, 52, 48, 47, 43, 45, 40, 42, 38],
    [28, 30, 32, 35, 37, 39, 41, 44, 46, 48, 45, 42, 40, 38, 36, 34],
]
feb_hours = [
    [40, 42, 44, 47, 52, 50, 62, 57, 60, 42, 45, 49, 51, 47, 46, 48],
    [37, 38, 42, 40, 44, 41, 36, 39, 35, 33, 42, 40, 38, 37, 39, 41],
    [32, 34, 37, 42, 40, 47, 52, 62, 57, 43, 44, 46, 48, 37, 39, 33],
    [27, 32, 37, 42, 47, 52, 57, 62, 34, 42, 40, 44, 39, 37, 35, 34],  # Fixed line 25
    [22, 27, 30, 32, 34, 32, 35, 37, 42, 32, 31, 33, 32, 32, 30, 27],
    [17, 22, 27, 30, 32, 34, 37, 39, 35, 33, 30, 28, 27, 24, 26, 29],
    [27, 32, 37, 40, 42, 47, 50, 52, 54, 50, 49, 45, 47, 42, 44, 40],
    [30, 32, 34, 37, 39, 41, 43, 46, 48, 50, 47, 44, 42, 40, 38, 36],
]

# Setting up the plots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 10), sharex=True)
fig.suptitle('Distribution of Weekly Working Hours Across Departments in a Tech Company\nOver Two Months', fontsize=16, fontweight='bold')

# Colors for each department
colors = ['lightcoral', 'lightskyblue', 'lightgreen', 'lightyellow', 'lightpink', 'lightgray', 'lightcyan', 'wheat']

for ax, data, month in zip(axes, [jan_hours, feb_hours], ['January', 'February']):
    bp = ax.boxplot(data, vert=False, patch_artist=True, notch=True)
    
    # Customizing the box plots
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
    
    # Adding titles and labels
    ax.set_title(f'{month} Data', fontsize=14, fontweight='bold')
    ax.set_xlabel('Hours Worked per Week', fontsize=12)
    ax.set_yticklabels(departments)
    ax.set_yticks(np.arange(1, len(departments) + 1))
    ax.grid(True, linestyle='--', alpha=0.6, axis='x')
    
    # Adding annotations for statistical metrics
    for i, hours in enumerate(data, start=1):
        median = np.median(hours)
        mean = np.mean(hours)
        ax.annotate(f'Median: {median:.1f} hrs', xy=(median, i), xytext=(median + 2, i + 0.1),
                    arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
        ax.annotate(f'Mean: {mean:.1f} hrs', xy=(mean, i), xytext=(mean + 2, i - 0.2),
                    arrowprops=dict(facecolor='green', arrowstyle='->'), fontsize=10, color='green')

# Automatically adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Show the plot
plt.show()