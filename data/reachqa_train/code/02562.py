import matplotlib.pyplot as plt
import numpy as np

# Data: Monthly revenue (in thousands USD) for each startup over the year 2023
months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])
ai_innovators_revenue = np.array([120, 130, 145, 160, 155, 165, 175, 180, 195, 210, 220, 240])
greentech_pioneers_revenue = np.array([95, 100, 110, 125, 130, 140, 150, 160, 170, 175, 190, 200])
fintech_wizards_revenue = np.array([110, 115, 125, 130, 140, 145, 155, 165, 170, 180, 190, 205])
healthtech_heroes_revenue = np.array([130, 135, 145, 155, 150, 160, 170, 175, 180, 185, 195, 210])

# Create a line chart
plt.figure(figsize=(14, 8))
plt.plot(months, ai_innovators_revenue, marker='o', label='AI Innovators', linestyle='-', linewidth=2, color='#FF5733')
plt.plot(months, greentech_pioneers_revenue, marker='v', label='GreenTech Pioneers', linestyle='--', linewidth=2, color='#33FF57')
plt.plot(months, fintech_wizards_revenue, marker='s', label='FinTech Wizards', linestyle='-.', linewidth=2, color='#3357FF')
plt.plot(months, healthtech_heroes_revenue, marker='d', label='HealthTech Heroes', linestyle=':', linewidth=2, color='#FF33C4')

# Title and labels
plt.title('Tech Startups Growth Journey:\nMonthly Revenue Analysis in 2023', fontsize=16, weight='bold', pad=20)
plt.xlabel('Months', fontsize=12)
plt.ylabel('Revenue (in thousands USD)', fontsize=12)

# Customize legend
plt.legend(title='Startups', title_fontsize='13', fontsize='11', loc='upper left', frameon=True)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Add annotations at the end of the year for each startup
for revenue, label, color in zip(
    [ai_innovators_revenue, greentech_pioneers_revenue, fintech_wizards_revenue, healthtech_heroes_revenue],
    ['AI Innovators', 'GreenTech Pioneers', 'FinTech Wizards', 'HealthTech Heroes'],
    ['#FF5733', '#33FF57', '#3357FF', '#FF33C4']
):
    plt.annotate(
        f'{label}: ${revenue[-1]}k', 
        xy=(11, revenue[-1]), 
        xytext=(0, 10),
        textcoords='offset points',
        arrowprops=dict(facecolor=color, shrink=0.05),
        fontsize=10, color=color, ha='center'
    )

# Automatically adjust the layout to prevent overlaps
plt.tight_layout()

# Show the plot
plt.show()