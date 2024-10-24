import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Financial events and their impacts
events = ['Initial Funding', 'Sales Revenue', 'Operational Costs', 
          'Marketing Expenses', 'Cyber Breach', 'Legal Settlements', 
          'Misc. Income', 'Net Income']
values = [500, 300, -200, -150, -50, -30, 20]

# Calculate cumulative values
cumulative_values = np.cumsum(values)
cumulative_values = np.insert(cumulative_values, 0, 0)  # Add starting point
final_net_income = cumulative_values[-1]

# Enhanced color mapping: gradient based on magnitude
base_color = np.array([0.6, 0.2, 0.2])
colors = [(base_color * (1 - (value / max(abs(np.array(values)))))) + 0.4 for value in values]
colors = [tuple(np.clip(color, 0, 1)) for color in colors]

# Add transparency to bars for depth
alpha_levels = np.linspace(0.6, 1.0, num=len(values))

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 7))

# Plot the bars with gradient and transparency
for idx, (event, value, color, alpha) in enumerate(zip(events[:-1], cumulative_values[1:], colors, alpha_levels)):
    ax.bar(event, value, color=color, alpha=alpha, edgecolor='black', zorder=3)

# Highlight the final net income in blue
ax.bar(events[-1], final_net_income, color='blue', edgecolor='black', zorder=3)

# Add grid for better readability, only major lines
ax.yaxis.grid(True, linestyle='--', zorder=0)

# Annotate bars with value and percentage change
for i, (value, prev_value) in enumerate(zip(cumulative_values[1:], cumulative_values[:-1]), 1):
    percent_change = ((value - prev_value) / abs(prev_value) * 100) if prev_value != 0 else 0
    annotation_text = f"{value:.0f}K\n({percent_change:+.1f}%)"
    ax.annotate(annotation_text, (i-1, value), textcoords="offset points", xytext=(0, 10), 
                ha='center', fontsize=10, fontweight='bold', color='black')

# Set labels and title
ax.set_title("InnovateTech's Financial Journey\nA Year in Review", fontsize=16, fontweight='bold')
ax.set_xlabel("Financial Events", fontsize=12)
ax.set_ylabel("Amount in $K", fontsize=12)

# Rotate x-tick labels to prevent overlap
ax.set_xticks(range(len(events)))
ax.set_xticklabels(events, rotation=45, ha='right', fontsize=10)

# Add legend for color coding
handles = [mpatches.Patch(color='blue', label='Final Net Income')]
ax.legend(handles=handles, loc='upper left', fontsize=10)

# Connect bars with curved lines
for i in range(len(cumulative_values) - 2):
    x_vals = [i, i + 1]
    y_vals = [cumulative_values[i + 1]] * 2
    ax.plot(x_vals, y_vals, color='grey', linestyle='dashed', linewidth=1, zorder=2)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()