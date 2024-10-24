import matplotlib.pyplot as plt
import numpy as np

# Define time period: months over 5 years
months = np.arange(1, 61)  # 1 to 60 representing 5 years (12 months each)

# Monthly sales data in units (arbitrary)
sales_data = np.array(
    [120, 130, 125, 150, 160, 180, 175, 190, 195, 210, 220, 230,  # Year 1
     240, 250, 245, 270, 280, 300, 290, 310, 320, 330, 340, 350,  # Year 2
     360, 370, 365, 390, 410, 430, 420, 450, 460, 480, 490, 500,  # Year 3
     510, 520, 515, 540, 560, 580, 570, 600, 610, 630, 650, 670,  # Year 4
     680, 700, 690, 720, 740, 770, 760, 790, 800, 820, 840, 860]  # Year 5
)

# Milestones annotations
milestones = {
    12: "Year 1\nMilestone",
    24: "Year 2\nMilestone",
    36: "Year 3\nMilestone",
    48: "Year 4\nMilestone",
    60: "Year 5\nMilestone"
}

# Create the line chart
plt.figure(figsize=(12, 6))
plt.plot(months, sales_data, color='green', linestyle='-', linewidth=2, marker='o', markersize=5, label='Monthly EV Sales')

# Adding milestone annotations
for month, text in milestones.items():
    plt.annotate(text, (month, sales_data[month-1]), textcoords="offset points", xytext=(-15,10), ha='center',
                 arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.5))

# Define plot details
plt.title("The Rise of Electric Vehicles:\nMonthly Sales Growth Over 5 Years", fontsize=16, weight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Number of EVs Sold", fontsize=12)
plt.xticks(np.arange(0, 61, step=6), 
           ['M0', 'M6', 'M12', 'M18', 'M24', 'M30', 'M36', 'M42', 'M48', 'M54', 'M60'], fontsize=10)
plt.yticks(fontsize=10)

# Adding a legend
plt.legend(loc='upper left', fontsize=10)

# Adding grid lines for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()