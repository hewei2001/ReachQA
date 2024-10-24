import matplotlib.pyplot as plt
import numpy as np

# Years from 2015 to 2025
years = np.arange(2015, 2026)

# Engagement scores for each department (on a scale from 0 to 100)
sales_engagement = [65, 67, 70, 72, 75, 78, 77, 76, 80, 83, 85]
it_engagement = [60, 62, 64, 68, 70, 73, 75, 76, 78, 80, 81]
hr_engagement = [70, 72, 73, 74, 76, 78, 79, 77, 78, 80, 82]
finance_engagement = [68, 70, 69, 70, 72, 73, 75, 74, 76, 78, 79]

# Plot configuration
plt.figure(figsize=(14, 8))

# Plot each department's engagement scores
plt.plot(years, sales_engagement, marker='o', linestyle='-', linewidth=2, label='Sales', color='tab:blue')
plt.plot(years, it_engagement, marker='s', linestyle='--', linewidth=2, label='IT', color='tab:green')
plt.plot(years, hr_engagement, marker='^', linestyle='-.', linewidth=2, label='HR', color='tab:red')
plt.plot(years, finance_engagement, marker='d', linestyle=':', linewidth=2, label='Finance', color='tab:purple')

# Titles and labels
plt.title("Trends in Employee Engagement Across Departments\n(2015-2025)", fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Engagement Score', fontsize=14)

# Annotate significant trends
plt.annotate('Sales Boost\nNew Incentive', xy=(2020, 83), xytext=(2017, 87),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, ha='center', va='bottom', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='wheat', alpha=0.8))

plt.annotate('IT Advancement\nTech Initiatives', xy=(2021, 80), xytext=(2018, 74),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, ha='center', va='top', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightsteelblue', alpha=0.8))

# Add data labels for each point
for year, sales, it, hr, finance in zip(years, sales_engagement, it_engagement, hr_engagement, finance_engagement):
    plt.text(year, sales, str(sales), color='tab:blue', fontsize=9, ha='center', va='bottom')
    plt.text(year, it, str(it), color='tab:green', fontsize=9, ha='center', va='bottom')
    plt.text(year, hr, str(hr), color='tab:red', fontsize=9, ha='center', va='bottom')
    plt.text(year, finance, str(finance), color='tab:purple', fontsize=9, ha='center', va='bottom')

# Legend placement
plt.legend(title='Departments', loc='lower right', fontsize=12, frameon=True)

# Grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Adjust layout for clear visualization
plt.tight_layout()

# Display the plot
plt.show()