import matplotlib.pyplot as plt
import numpy as np

# Years for the x-axis
years = np.arange(2018, 2023)

# Synthetic monthly sales data (in thousands) with more variation
tesla_sales = [120, 135, 125, 160, 140, 170, 185, 220, 190, 215, 230, 245,
               260, 245, 280, 270, 300, 290, 320, 310, 350, 370, 365, 380,
               400, 395, 420, 430, 460, 470, 480, 495, 500, 520, 540, 560,
               580, 600, 610, 620, 635, 640, 660, 675, 680, 700, 720, 730,
               750, 770, 780, 800, 815, 830, 840, 850, 860, 875, 890, 910]

nissan_sales = [80, 85, 95, 100, 90, 110, 130, 135, 125, 140, 145, 150,
                160, 170, 165, 180, 175, 195, 185, 200, 210, 220, 215, 230,
                240, 245, 250, 260, 270, 275, 280, 290, 300, 310, 315, 320,
                330, 340, 350, 355, 360, 375, 380, 390, 395, 400, 410, 420,
                430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540]

bmw_sales = [50, 60, 65, 70, 75, 85, 90, 95, 100, 105, 115, 120,
             130, 125, 140, 145, 150, 160, 165, 175, 185, 190, 200, 210,
             220, 225, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320,
             330, 340, 350, 360, 370, 380, 385, 390, 400, 410, 420, 430,
             440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550]

ford_sales = [60, 70, 75, 85, 80, 90, 95, 105, 100, 110, 115, 120,
              130, 135, 140, 145, 150, 160, 170, 175, 180, 190, 195, 205,
              210, 220, 230, 240, 245, 255, 265, 275, 285, 295, 305, 310,
              320, 330, 340, 345, 355, 365, 375, 385, 395, 405, 415, 425,
              435, 445, 455, 465, 475, 485, 495, 505, 515, 525, 535, 545]

rivian_sales = [10, 20, 25, 30, 35, 40, 45, 50, 55, 65, 60, 75,
                80, 85, 90, 95, 100, 110, 105, 120, 125, 135, 140, 150,
                160, 170, 180, 190, 195, 205, 215, 225, 230, 240, 250, 260,
                270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380,
                390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500]

# Calculate annual sales for each brand
def calculate_annual_sales(monthly_sales):
    return [sum(monthly_sales[i:i+12]) for i in range(0, len(monthly_sales), 12)]

tesla_annual = calculate_annual_sales(tesla_sales)
nissan_annual = calculate_annual_sales(nissan_sales)
bmw_annual = calculate_annual_sales(bmw_sales)
ford_annual = calculate_annual_sales(ford_sales)
rivian_annual = calculate_annual_sales(rivian_sales)

# Plot setup
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Line plot (Monthly Sales)
ax = axes[0]
time = np.arange(len(tesla_sales))
ax.plot(time, tesla_sales, label='Tesla', marker='o', linestyle='-', linewidth=2, color='#E74C3C')
ax.plot(time, nissan_sales, label='Nissan', marker='s', linestyle='--', linewidth=2, color='#3498DB')
ax.plot(time, bmw_sales, label='BMW', marker='^', linestyle=':', linewidth=2, color='#2ECC71')
ax.plot(time, ford_sales, label='Ford', marker='D', linestyle='-.', linewidth=2, color='#F1C40F')
ax.plot(time, rivian_sales, label='Rivian', marker='*', linestyle='-', linewidth=2, color='#9B59B6')

# Adjusted annotations for clarity
ax.annotate('Tesla Model Y Launch', xy=(14, 280), xytext=(5, 330),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, fontweight='bold', color='red')
ax.annotate('Rivian Debuts', xy=(12, 80), xytext=(15, 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, fontweight='bold', color='purple')

ax.set_title("Monthly Sales Trend\nof Leading EV Brands (2018-2022)", fontsize=14, fontweight='bold')
ax.set_xlabel('Month (from Jan 2018 to Dec 2022)', fontsize=12, fontweight='bold')
ax.set_ylabel('Monthly Sales (in thousands)', fontsize=12, fontweight='bold')

ax.set_xticks(np.arange(0, len(tesla_sales), step=12))
ax.set_xticklabels(years)

ax.legend(title='EV Brands', fontsize=10, title_fontsize='12', loc='upper left')
ax.grid(True, linestyle='--', alpha=0.7)

for year_pos in range(0, len(tesla_sales), 12):
    ax.axvline(year_pos, color='grey', linestyle='--', linewidth=1, alpha=0.5)

# Bar plot (Annual Sales)
ax = axes[1]
bar_width = 0.12  # Narrower bars to avoid overlap
x = np.arange(len(years))

# Adjust spacing and transparency for clarity
ax.bar(x - 2*bar_width, tesla_annual, width=bar_width, label='Tesla', color='#E74C3C', alpha=0.85)
ax.bar(x - bar_width, nissan_annual, width=bar_width, label='Nissan', color='#3498DB', alpha=0.85)
ax.bar(x, bmw_annual, width=bar_width, label='BMW', color='#2ECC71', alpha=0.85)
ax.bar(x + bar_width, ford_annual, width=bar_width, label='Ford', color='#F1C40F', alpha=0.85)
ax.bar(x + 2*bar_width, rivian_annual, width=bar_width, label='Rivian', color='#9B59B6', alpha=0.85)

ax.set_title("Annual Sales Overview\nfor Electric Vehicle Brands", fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Annual Sales (in thousands)', fontsize=12, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(years)

ax.legend(title='EV Brands', fontsize=10, title_fontsize='12', loc='upper left')
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()

plt.show()