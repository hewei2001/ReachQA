import matplotlib.pyplot as plt
import numpy as np

# Original data for bar chart
specializations = [
    'AI Ethics & Policy',
    'Autonomous Systems\nEngineering',
    'NLP Development',
    'AI-Driven Healthcare\nSolutions',
    'Machine Vision Experts'
]
employment_numbers = np.array([12500, 18300, 21000, 19700, 15400])

# Related data for the second subplot
# Represent the projected growth rate in percentage
growth_rates = np.array([10, 15, 12, 18, 14])

# Color configuration
colors = ['#6A5ACD', '#4682B4', '#32CD32', '#FF8C00', '#DA70D6']

# Create positions for each bar along the x-axis
x_positions = np.arange(len(specializations))

# Initialize the figure with two subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# First subplot: Bar chart
ax1 = axes[0]
bars = ax1.bar(x_positions, employment_numbers, color=colors, alpha=0.8)
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2.0, yval, f'{yval:,}', va='bottom', ha='center', fontsize=10, fontweight='bold', color='darkblue')

ax1.set_title('The Rise of AI Specializations:\nEmployment Trends in 2030', fontsize=14, pad=10)
ax1.set_xlabel('AI Specializations', fontsize=12)
ax1.set_ylabel('Number of Professionals', fontsize=12)
ax1.set_xticks(x_positions)
ax1.set_xticklabels(specializations, rotation=30, ha='right')
ax1.yaxis.grid(True, linestyle='--', alpha=0.5)

# Second subplot: Line chart
ax2 = axes[1]
ax2.plot(specializations, growth_rates, marker='o', linestyle='-', color='#FF4500', linewidth=2, markersize=8)

# Annotating the growth rates
for i, rate in enumerate(growth_rates):
    ax2.text(i, rate, f'{rate}%', fontsize=10, ha='center', va='bottom', color='darkred')

ax2.set_title('Projected Growth Rate:\nAI Specializations 2023-2030', fontsize=14, pad=10)
ax2.set_xlabel('AI Specializations', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.set_xticks(x_positions)
ax2.set_xticklabels(specializations, rotation=30, ha='right')
ax2.yaxis.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the combined plot
plt.show()