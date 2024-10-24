import matplotlib.pyplot as plt
import numpy as np

# Define months and ticket sales data for two cinema franchises
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ticket_sales_moviemagic = np.array([1500, 1800, 2000, 2300, 3000, 2500, 2700, 3500, 4000, 3700, 3600, 4200])
ticket_sales_screenspectacle = np.array([1300, 1600, 1900, 2500, 2800, 2700, 3100, 3300, 3900, 3900, 3500, 4300])

# Calculate additional data: difference and cumulative ticket sales
ticket_sales_difference = ticket_sales_moviemagic - ticket_sales_screenspectacle
cumulative_sales_moviemagic = np.cumsum(ticket_sales_moviemagic)
cumulative_sales_screenspectacle = np.cumsum(ticket_sales_screenspectacle)

# Initialize a subplot layout with two plots
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# First Subplot: Line chart for ticket sales comparison
ax[0].plot(months, ticket_sales_moviemagic, marker='o', linestyle='-', color='blue', label='MovieMagic', linewidth=2)
ax[0].plot(months, ticket_sales_screenspectacle, marker='s', linestyle='-', color='red', label='ScreenSpectacle', linewidth=2)

for i, month in enumerate(months):
    ax[0].annotate(f'{ticket_sales_moviemagic[i]}', xy=(month, ticket_sales_moviemagic[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='blue')
    ax[0].annotate(f'{ticket_sales_screenspectacle[i]}', xy=(month, ticket_sales_screenspectacle[i]), textcoords="offset points", xytext=(0,-15), ha='center', fontsize=8, color='red')

ax[0].set_title("Monthly Ticket Sales Comparison\nfor Cinema Franchises in 2023", fontsize=14, weight='bold', pad=10)
ax[0].set_xlabel("Months", fontsize=12)
ax[0].set_ylabel("Ticket Sales", fontsize=12)
ax[0].grid(visible=True, linestyle='--', alpha=0.5)
ax[0].legend(title="Cinema Franchises", loc='upper left', fontsize=10)

# Second Subplot: Bar chart for cumulative sales
ax[1].bar(months, cumulative_sales_moviemagic, color='blue', alpha=0.6, label='Cumulative MovieMagic')
ax[1].bar(months, cumulative_sales_screenspectacle, color='red', alpha=0.6, label='Cumulative ScreenSpectacle')

ax[1].set_title("Cumulative Ticket Sales\nfor 2023", fontsize=14, weight='bold', pad=10)
ax[1].set_xlabel("Months", fontsize=12)
ax[1].set_ylabel("Cumulative Sales", fontsize=12)
ax[1].grid(visible=True, linestyle='--', alpha=0.5)
ax[1].legend(title="Cinema Franchises", loc='upper left', fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()